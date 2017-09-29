import pickle
import sqlite3
import time


class PersistenceStorage:
    def __init__(self):
        self._conn = sqlite3.connect(':memory:')
        self._cursor = self._conn.cursor()
        self._cursor.execute('CREATE TABLE tags (date text, url text, data text)')
        self._conn.commit()

    def save(self, url, tags):

        serialized = pickle.dumps(tags)
        self._cursor.execute("INSERT INTO tags VALUES (?, ?, ?)", [time.strftime("%c"), url, serialized])
        self._conn.commit()

    def load(self, url):
        self._cursor.execute('SELECT * FROM tags WHERE url=?', [url])
        raw_results = self._cursor.fetchall()
        return [PersistenceStorage._raw_writer(r) for r in raw_results]

    @staticmethod
    def _raw_writer(row):
        encoded = str(pickle.loads(row[2]))
        return f"{row[0]}, {row[1]}, {encoded}"
