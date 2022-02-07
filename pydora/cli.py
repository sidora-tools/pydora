import click
from pydora import __version__
from pydora import get_credentials
from pydora import retrieve_samples


@click.command()
@click.version_option(__version__)
@click.option(
    "-c",
    "--credentials",
    type=click.Path(exists=True, readable=True, resolve_path=True),
    default="credentials.json",
    show_default=True,
)
@click.option(
    "-p",
    "--projects",
    help="File listing projects to include (one per line)",
    type=click.Path(readable=True, resolve_path=True),
    default=None,
)
@click.option(
    "-t",
    "--tags",
    help="File listing tags to include (one per line)",
    type=click.Path(readable=True, resolve_path=True),
    default=None,
)
@click.option(
    "--join",
    type=click.Choice(["sql", "pandas"], case_sensitive=False),
    default="sql",
    show_default=True,
    help="Join method",
)
@click.option(
    "-o",
    "--output",
    default="pandora_samples.csv",
    type=click.Path(file_okay=True, writable=True, resolve_path=True),
    show_default=True,
    help="Warinner samples metadata information",
)
def cli(no_args_is_help=True, **kwargs):
    """\b
    PyDora: Retrieve samples and metadata from MPI-EVA Pandora internal database
    Author: Maxime Borry
    Contact: <maxime_borry[at]eva.mpg.de>
    Homepage: https://gitlab.gwdg.de/paleobiotech/pydora
    \b
    """

    credentials = kwargs["credentials"]
    kwargs.pop("credentials", None)

    cred = get_credentials(credentials)
    retrieve_samples(**kwargs, **cred)
