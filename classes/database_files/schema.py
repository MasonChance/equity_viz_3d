'''Creates Database Tables for application, if DEBUG=True in .env tables are dropped and recreated on every initialization; Else: data persists and must be manually altered with the methods included in the table classes
'''

# Imports:
import psycopg2 as pg 
import os
import environ
import config
from db_tables import CompanyTickerTable


class DatabaseEquities:
    """[PostgresSQL database Class]
    """
    def __init__(self, config:module):
        self.DB_HOST = config.DB_HOST
        self.DB_NAME = config.DB_NAME
        self.DB_USER = config.DB_USER
        self.DB_PASS = config.DB_PASS
        self.DB_PORT = config.DB_PORT
        self.conn = None

    def connect(self):
        if self.conn is None:
            try:
                self.conn = pg.connect(
                    host=self.DB_HOST,
                    user=self.DB_USER,
                    password=self.DB_PASS,
                    port=self.DB_PORT,
                    dbname=self.DB_NAME,
                )
            except pg.DatabaseError as e:
                raise e
            finally:
                print('Connection opened successfully, waiting for input...')

    def create_table(self,table:object):
        self.connect()
        cur = self.conn.cursor()
        sql = f'CREATE TABLE {table.__class__.__name__}('
        for key in table.keys():
            sql += f'{key}'

        cur.execute()



if __name__ == '__main__':
    pass