import sqlite3


SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS kontakty (
    firstname TEXT,
    lastname TEXT,
    adresy TEXT
    )
"""

SQL_INSERT = """
    INSERT INTO kontakty VALUES (
        firstname =:firstname,
        lastname =:lastname,
        adresy =:adresy
)
"""
ksiazka_adresowa = [
    {
        'firstname': 'Jakub',
        'lastname': 'Kowalski',
        'adresy': 'NASA, street, 33, 90'
    }


]

SQL_SELECT = """
 SELECT * FROM kontakty
"""

with sqlite3.connect('database.sqlite3') as connection:
    connection.row_factory = sqlite3.Row
    connection.execute(SQL_CREATE_TABLE)
    connection.execute(SQL_INSERT)

    cur = connection.cursor()

    for row in cur.execute(SQL_SELECT):
        print(dict(row))
