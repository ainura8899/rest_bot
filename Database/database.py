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


    def fetch(self, query: str, params: tuple = None, fetchall: bool = True):
        with sqlite3.connect(self.path) as conn:
            result = conn.execute(query, params)
            result.row_factory = sqlite3.Row

            if fetchall:
                to_return = result.fetchall()
                return [dict(row) for row in to_return]
            else:
                to_return = result.fetchone()
                return dict(to_return)
