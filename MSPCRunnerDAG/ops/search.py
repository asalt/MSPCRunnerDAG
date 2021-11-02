import dagster
from dagster import op, Out, Output


# TODO set `io_manager_key`
@op(out=Out(metadata={"table": "search-results"}))
def search(
    context,
    preset=dagster.InputDefinition(None, dagster_type=dagster.Optional),
    ramalloc: float = 1000,  #
    refseq: str = None,
    # preset: Predefined_Search = typer.Option(None, case_sensitive=False),
    paramfile: Optional[Path] = typer.Option(None),
    local_refseq: Optional[Path] = typer.Option(None),
    calibrate_mass: Optional[int] = typer.Option(default=1, min=0, max=2),
    msfragger_conf: Optional[Path] = typer.Option(MSFRAGGER_DEFAULT_CONF),
):
    # build metadata from the input options
    metadata = {}

    result = "<some pandas dataframe / file>"

    return Output(result, "searchres", metadata=metadata)
