import click
from . import __version__
from . import get_credentials
from . import retrieve_samples

@click.command()
@click.version_option(__version__)
@click.argument('credentials', type=click.Path(exists=True, 
                                            readable=True, 
                                            resolve_path=True))
@click.argument('projects', type=click.Path(exists=True, 
                                            readable=True, 
                                            resolve_path=True))
@click.argument('tags', type=click.Path(exists=True, 
                                            readable=True, 
                                            resolve_path=True))
@click.option('-o',
              '--output',
              default='warinner_samples.csv',
              type=click.Path(file_okay=True, writable=True, resolve_path=True),
              show_default=True,
              help='Warinner samples metadata information')
                            
def cli(no_args_is_help=True, **kwargs):
    """\b
    warinner_samples: retrieve samples metadata and informations from MPI-SHH internal database
    Author: Maxime Borry
    Contact: <borry[at]shh.mpg.de>
    Homepage: https://gitlab.gwdg.de/paleobiotech/warinner-samples
    \b
    CREDENTIALS: Json formatted files with credentials for accessing Pandora
    PROJECTS: List of projects to include
    TAGS: List of tags to include
    """
    
    credentials = kwargs['credentials']
    kwargs.pop('credentials', None)
    
    cred = get_credentials(credentials)
    retrieve_samples(**kwargs, **cred)