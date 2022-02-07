__version__ = 0.2

import pandas as pd
import sqlalchemy
import json
from tqdm import tqdm
import sys

from pydora import sql_query
from pydora import pandas_query
from pydora import columns


def get_credentials(credentials):
    """Get credentials to access SQL server

    Args:
        credentials(str): Json formatted files with credentials for accessing Pandora
    Returns:
        dict: {host:'server_address', login:'login', password:'pwd'}
    """

    with open(credentials, "r") as c:
        cred = json.load(c)
    return cred


def retrieve_samples(host, port, login, password, projects, tags, output, join):
    """Retrive samples having projects or tags from Pandora DB

    Args:
        host(str): Address of SQL server
        port(int): Port of SQL server
        login(str): login
        password(str): password
        projects(str): File listing projects to include (one per line)
        tags(str): File listing projects tags to include (one per line)
        join(str): Table join method, either pandas (local) or sql (server)
    Returns:
        csv file of all samples retrieved

    """
    if projects:
        projects_list = []
        with open(projects, "r") as p:
            for line in p:
                projects_list.append(line.rstrip())
    else:
        projects_list = None
    if tags:
        tags_list = []
        with open(tags, "r") as t:
            for line in t:
                tags_list.append(line.rstrip())
    else:
        tags_list = None
    sql_connection = f"mysql+pymysql://{login}:{password}@{host}:{port}/pandora"
    engine = sqlalchemy.create_engine(sql_connection)
    try:
        pd.read_sql_query("SELECT 1", engine)
        print("Successfully Connected to Pandora Database")
    except Exception as e:
        print(e)
        print("Error connecting to Pandora Database")
        sys.exit(1)

    print("Making request to Pandora SQL server")
    if join == "pandas":
        wari = pandas_query.build_join_query(
            tags=tags_list, projects=projects_list, engine=engine
        )
    elif join == "sql":
        query_string = sql_query.build_join_query(
            tags=tags_list, projects=projects_list
        )
        wari = pd.read_sql_query(query_string, engine)

    wari.to_csv(output)
    print("Downloaded table")
    print(f"Samples and metadata have been written to {output}")
    # for i, c in enumerate(wari.columns):
    #     print(f"{i}: {c}")
    # print("Retrieving samples and metadata")

    # columns_interest = columns.columns_interest

    # wari_select = wari.iloc[:,list(columns_interest.keys())]
    # wari_select.columns = columns_interest.values()

    # wari_analysis = wari_select.pivot(columns='Title', values='Result')
    # print(wari_analysis.columns)
    # wari_analysis.index = wari_analysis.Full_Analysis_Id

    # wari_meta = wari_select
    # wari_meta.index = wari_meta.Full_Analysis_Id
    # wari_meta = wari_select.drop(['Id','Title','Result'], axis=1).drop_duplicates()

    # wari_full = wari_meta.merge(wari_analysis, left_index=True, right_index=True)
    # wari_full.reset_index(drop=True).to_csv(output)
    # wari_full.to_csv(output)

    # print(f"Samples and metadata have been written to {output}")
