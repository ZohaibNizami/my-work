from sqlite3 import connect


def get_db_connection():
    return connect("database.db")



def create_table():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
CREATE TABLE IF NOT EXISTS users    
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
              email TEXT NOT NULL UNIQUE,
              password TEXT NOT NULL)
              ''')
    conn.commit()
    conn.close()
    return True