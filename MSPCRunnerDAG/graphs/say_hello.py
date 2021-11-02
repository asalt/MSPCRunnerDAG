from dagster import graph

from MSPCRunnerDAG.ops.hello import hello

@graph
def say_hello():
    """
    A graph definition. This example graph has a single op.

    For more hints on writing Dagster graphs, see our documentation overview on Graphs:
    https://docs.dagster.io/concepts/ops_graphs/graphs
    """
    hello()

say_hello_job = say_hello.to_job()
