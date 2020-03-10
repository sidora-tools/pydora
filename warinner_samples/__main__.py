import pandas as pd
import sqlalchemy
import json
import click
from . import __version__

from . import query
from . import columns

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

    CREDENTIALS: Json formatted files with credentials for accessing Pandora
    PROJECTS: List of projects to include
    TAGS: List of tags to include
    """
    retrieve_samples(**kwargs)





def retrieve_samples(credentials, projects, tags, output):
    """Retrive samples having projects or tags from Pandora DB

    Args:
        credentials(str): Json formatted files with credentials for accessing Pandora
        projects(str): File listing projects to include (one per line)
        tags(str): File listing projects tags to include (one per line)
    Returns:
        csv file of all samples retrieved

    """
    
    with open(credentials, 'r') as c:
        cred = json.load(c)
    
    
    
    projects_list = []
    with open(projects, 'r') as p:
        for line in p:
            projects_list.append(line.rstrip())

    tags_list = []
    with open(tags, 'r') as t:
        for line in t:
            tags_list.append(line.rstrip())


    engine = sqlalchemy.create_engine(f"mysql+pymysql://{cred['login']}:{cred['password']}@{cred['host']}/pandora")
    print("Connected to Pandora Database")

    query_string = query.build_query(tags = tags_list, projects = projects_list)
    # print(query_string)

    wari = pd.read_sql_query(query_string, engine)

    print("Retrieving samples and metadata")

    columns_interest = columns.columns_interest

    wari_select = wari.iloc[:,list(columns_interest.keys())]
    wari_select.columns = columns_interest.values()
    wari_select.index = wari_select.Full_Analysis_Id
    wari_analysis = wari_select.pivot(columns='Title', values='Result')
    wari_meta = wari_select.drop(['Id','Title','Result'], axis=1).drop_duplicates()
    wari_full = wari_meta.merge(wari_analysis, left_index=True, right_index=True)
    wari_full.reset_index(drop=True).to_csv(output)

    print(f"Samples and metadata have been written to {output}")

