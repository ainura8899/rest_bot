import sqlite3
from Database.queries import Queries

class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute(Queries.CREATE_REVIEW_RESULTS_TABLE)

            conn.commit()

    def execute(self, query: str, params: tuple = None):
        with sqlite3.connect(self.path) as conn:
            conn.execute(query, params)

            conn.commit()

