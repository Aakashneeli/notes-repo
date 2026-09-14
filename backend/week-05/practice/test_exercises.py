"""Local feedback for beginner SQL, using a disposable SQLite database."""
import sqlite3
from sqlalchemy import create_engine, text
import exercises

def database():
    e = create_engine("sqlite://")
    with e.begin() as c:
        c.exec_driver_sql("CREATE TABLE authors (id INTEGER PRIMARY KEY, name TEXT)")
        c.exec_driver_sql("CREATE TABLE articles (id INTEGER PRIMARY KEY, author_id INTEGER, title TEXT, published BOOLEAN)")
        c.exec_driver_sql("INSERT INTO authors VALUES (1,'Asha'),(2,'Ben'),(3,'Chen')")
        c.exec_driver_sql("INSERT INTO articles VALUES (1,1,'SQL notes',1),(2,1,'API notes',0),(3,2,'Testing notes',1),(4,NULL,'Draft',0)")
    return e

def test_page():
    e = database()
    try:
        with e.connect() as c:
            assert c.execute(text(exercises.published_page()), {"published": True}).all() == [(1,"SQL notes"),(3,"Testing notes")]
            assert c.execute(text(exercises.published_page()), {"published": False}).all() == [(2,"API notes"),(4,"Draft")]
    finally:
        e.dispose()

def test_counts():
    e = database()
    try:
        with e.connect() as c:
            assert c.execute(text(exercises.author_counts())).all() == [("Asha",2),("Ben",1),("Chen",0)]
    finally:
        e.dispose()
