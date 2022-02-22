from settings.config import BaseSettings
from sqlalchemy.engine import Engine
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from datetime import datetime
import pandas as pd


def _get_engine() -> Engine:
    """
    :return: Created base SQL engine w/ provided params
    """
    conf = BaseSettings()
    params = f'DRIVER={conf.DATABASE_DRIVER};' \
             f'SERVER={conf.DATABASE_HOST};' \
             f'DATABASE={conf.DATABASE_DATABASE};' \
             f'UID={conf.DATABASE_USERNAME};' \
             f'PWD={conf.DATABASE_PASSWORD};' \
             f'MARS_Connection=Yes'
    odbc = quote_plus(params)
    return create_engine(f'mssql+pyodbc:///?odbc_connect={odbc}', pool_size=1000, max_overflow=100)


def _write_to_sql(table_name, payload):
    """

    :param payload: JSON object returned from API
    :param table_name: Where to write the data to
    :return:
    """
    engine = _get_engine()
    with engine.connect() as conn:
        df = pd.read_json(payload)
        df.insert(1, 'Last_Updated', datetime.now())
        df.to_sql(table_name,
                  con=conn,
                  schema='source',
                  if_exists='append',
                  index=False,
                  chunksize=1000)
        conn.close()
    return
