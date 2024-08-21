import sqlite3
from Database.queries import Queries

class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute(Queries.CREATE_REVIEW_RESULTS_TABLE)
            conn.execute(Queries.CREATE_TABLE_CATEGORIES)
            conn.execute(Queries.CREATE_TABLE_DISHES)
            conn.execute(Queries.INSERT_INTO_DISHES)
            conn.execute(Queries.INSERT_INTO_CAT)
            conn.commit()

    def execute(self, query: str, params: tuple = None):
        with sqlite3.connect(self.path) as conn:
            conn.execute(query, params)


    def fetch(self, query: str, params: tuple = None, fetchmany: bool = True):
        with sqlite3.connect(self.path) as conn:
            result = conn.execute(query, params)

            return result.fetchall()

