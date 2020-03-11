__version__ = 0.1

import pandas as pd
import sqlalchemy
import json

from . import query
from . import columns

def get_credentials(credentials):
    """Get credentials to access SQL server

    Args:
        credentials(str): Json formatted files with credentials for accessing Pandora
    Returns:
        dict: {host:'server_address', login:'login', password:'pwd'}
    """

    with open(credentials, 'r') as c:
        cred = json.load(c)
    return(cred)


def retrieve_samples(host, login, password, projects, tags, output):
    """Retrive samples having projects or tags from Pandora DB

    Args:
        host(str): Address of SQL server
        login(str): login
        password(str): password
        projects(str): File listing projects to include (one per line)
        tags(str): File listing projects tags to include (one per line)
    Returns:
        csv file of all samples retrieved

    """

    projects_list = []
    with open(projects, 'r') as p:
        for line in p:
            projects_list.append(line.rstrip())

    tags_list = []
    with open(tags, 'r') as t:
        for line in t:
            tags_list.append(line.rstrip())


    engine = sqlalchemy.create_engine(f"mysql+pymysql://{login}:{password}@{host}/pandora")
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
