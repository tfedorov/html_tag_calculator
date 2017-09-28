import pickle
import sqlite3
import time

conn = sqlite3.connect(':memory:')


def init():
    c = conn.cursor()
    c.execute('CREATE TABLE tags (date text, url text, data text)')
    conn.commit()


def save(url, tags):
    c = conn.cursor()
    serialized = pickle.dumps(tags)
    c.execute("INSERT INTO tags VALUES (?, ?, ?)", [time.strftime("%c"), url, serialized])
    conn.commit()


def load(url):
    c = conn.cursor()
    c.execute('SELECT * FROM tags WHERE url=?', [url])
    raw_results = c.fetchall()
    return [_raw_writer(r) for r in raw_results]


def _raw_writer(row):
    encoded = str(pickle.loads(row[2]))
    return f"{row[0]}, {row[1]}, {encoded}"
