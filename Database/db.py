import sqlite
from db.queries import Queries


class Database:
    def __init__(self, path:str):
        self.path = path

    def create_tables(self) -> None:
        with sqlite.connect(self.path) as db:
            db.execute(Queries.CREATE_OPROS_TABLE)
            db.commit()

    def execute(self, query: str, params: tuple | None = None) -> None:
        with sqlite.connect(self.path) as db:
            db.execute(query, params or ())
            db.commit()

    def fetch(self, query: str, params: tuple | None = None, fetch_all: bool = True):
        with sqlite.connect(self.path) as db:
            db.row_factory = sqlite.Row
            data = db.execute(query, params or ())

            if fetch_type:
                result = data.fetchall()
                if not result:
                    return None
                return [dict(row) for row in result]
            else:
                result = data.fetchone()
                if not result:
                    return None
                return dict(result)