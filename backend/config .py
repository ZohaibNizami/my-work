from sqlite3 import connect


def get_db_connection():
    return connect("database.db")


