from datetime import datetime

from dagster import graph, hourly_partitioned_config, in_process_executor

from MSPCRunnerDAG.ops.search import search
from MSPCRunnerDAG.ops.MASIC import quant
from MSPCRunnerDAG.ops.gpGrouper import gpGroup
from MSPCRunnerDAG.ops.mokapot import mokapot  # brew?


# etc etc
DEFAULT_TAGS = {
    "toplevel": {"container_config": {"parameters": {"search": {"ramalloc": 8400}}}}
}


@graph
def process_default():
    quant_res = quant()
    search_res = search()
    moka_res = mokapot()
    gpg_res = gpGroup()


# see https://github.com/dagster-io/dagster/blob/master/examples/hacker_news/hacker_news/jobs/hacker_news_api_download.py
# template guide for defining jobs

search_test = process_default.to_job(
    resource_defs=dict(
        **{
            "partition_bounds": partition_bounds,
            "hn_client": hn_api_subsample_client.configured({"sample_rate": 10}),
        },
        **RESOURCES_PROD,
    ),
    tags=DOWNLOAD_TAGS,
    config=hourly_download_config,
)
