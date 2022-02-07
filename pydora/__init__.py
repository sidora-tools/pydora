__version__ = '0.2'

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
        projects(list): list of projects to include (one per line)
        tags(list): list tags to include (one per line)
        join(str): Table join method, either pandas (local) or sql (server)
    Returns:
        (pandas dataframe) Table of retrieved samples and metadata

    """
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
        request = pandas_query.build_join_query(
            tags=tags, projects=projects, engine=engine
        )
    elif join == "sql":
        query_string = sql_query.build_join_query(
            tags=tags, projects=projects
        )
        request = pd.read_sql_query(query_string, engine)
    
    print("All samples and metadata successfully retrived")
    
    if output:
        request.to_csv(output)
        print(f"Samples and metadata have been written to {output}")

    return request