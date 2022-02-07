from pydora import sql_query
from pydora import table_join_keys as table_info
from tqdm import tqdm
import pandas as pd


def build_join_query(tags, projects, engine):
    all_tables = {}
    print("Downloading tables")
    for t in tqdm(table_info.tables):
        thequery = sql_query.build_single_query(t)
        all_tables[t] = pd.read_sql_query(thequery, engine).add_suffix(
            table_info.tables[t]
        )

    join_table = all_tables["TAB_Analysis_Result_String"]
    print("Joining tables with Pandas")
    for t in tqdm(table_info.join_keys):
        left_table = all_tables[t[0]]
        right_table = all_tables[t[1]]
        left_key = t[2]
        right_key = t[3]
        join_table = join_table.merge(
            right_table, left_on=left_key, right_on=right_key, how="outer"
        )

    res_table = pd.DataFrame()
    if tags:
        for t in tags:
            res_table = res_table.append(
                join_table[
                    join_table.Tags_Sample.str.contains(t, regex=False, na=False)
                ]
            )
    if projects:
        for p in projects:
            res_table = res_table.append(
                join_table[
                    join_table.Projects_Sample.str.contains(p, regex=False, na=False)
                ]
            )
    if not tags and not projects:
        res_table = join_table

    return res_table
