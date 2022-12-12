# Name: Wilson Van Nice
# This program consists of various examples of how to manipulate and display structured data from a sqlite database

import sqlite3
import pandas as pd

connection = sqlite3.connect('books.db')

pd.options.display.max_columns = 10
read_authors = pd.read_sql('SELECT * FROM authors', connection,
            index_col=['id'])
read_titles = pd.read_sql('SELECT * FROM titles', connection)
df = pd.read_sql('SELECT * FROM author_ISBN', connection)
read_first_last = pd.read_sql('SELECT first, last FROM authors', connection)
read_title_copyright = pd.read_sql("""SELECT title, edition, copyright
                            FROM titles
                            WHERE copyright > '2016'""", connection)
read_id_author = pd.read_sql("""SELECT id, first, last
                FROM authors
                WHERE last LIKE 'D%'""",
            connection, index_col=['id'])
read_id_author_rand = pd.read_sql("""SELECT id, first, last
                                    FROM authors
                                    WHERE first LIKE '_b%'""",
                                  connection, index_col=['id'])
tFtOBtA = pd.read_sql('SELECT title FROM titles ORDER BY title ASC',
                      connection)
auth_by_last = pd.read_sql("""SELECT id, first, last
                                            FROM authors
                                            ORDER BY last, first""",
                                         connection, index_col=['id'])
auth_by_first = pd.read_sql("""SELECT id, first, last
                              FROM authors
                              ORDER BY last DESC, first ASC""",
                            connection, index_col=['id'])
where_order_by = pd.read_sql("""SELECT isbn, title, edition, copyright
                                FROM titles
                                WHERE title LIKE '%How to Program'
                                ORDER BY title""", connection)

inner_join = pd.read_sql("""SELECT first, last, isbn
                            FROM authors
                            INNER JOIN author_ISBN
                                ON authors.id = author_ISBN.id
                            ORDER BY last, first""", connection)
cursor = connection.cursor()
cursor = cursor.execute("""INSERT INTO authors (first, last)
                            VALUES ('Sue', 'Red')""")
insert_into = pd.read_sql('SELECT id, first, last FROM authors',
                          connection, index_col=['id'])
cursor = cursor.execute("""UPDATE authors SET last='Black'
                            WHERE last='Red' AND first='Sue'""")
update = pd.read_sql('SELECT id, first, last FROM authors',
                     connection, index_col=['id'])
cursor = cursor.execute('DELETE FROM authors WHERE id=6')
delete = pd.read_sql('SELECT id, first, last FROM authors',
                     connection, index_col=['id'])






