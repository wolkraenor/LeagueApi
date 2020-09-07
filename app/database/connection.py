import sys
import json2table
import pymssql
import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import find_dotenv, load_dotenv


def __get_data_by_query(query):
    connection_string = '{engine}://{user}:{pswd}@{host}:{port}/{base}'.format(
                                                                                engine=MYSQL_ENGINE,
                                                                                user=MYSQL_USER,
                                                                                pswd=MYSQL_PASSWORD,
                                                                                host=MYSQL_HOST,
                                                                                port=MYSQL_PORT,
                                                                                base=MYSQL_BASE)
    engine = create_engine(connection_string, echo=False)
    data = pd.read_sql(query, engine)
    engine.dispose()
    return data
                                                                            
    