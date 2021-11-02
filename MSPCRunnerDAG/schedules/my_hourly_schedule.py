from dagster import schedule

from MSPCRunnerDAG.graphs.say_hello import say_hello_job


@schedule(cron_schedule="0 * * * *", job=say_hello_job, execution_timezone="US/Central")
def my_hourly_schedule(_context):
    run_config = {}
    return run_config
