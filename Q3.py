# Name: Wilson Van Nice
# This program consists of various examples of how to manipulate and display structured data from a sqlite database

import sqlite3
import pandas as pd
pd.set_option('display.max_columns',10)

connection = sqlite3.connect('books.db')

last_decs = pd.read_sql("""SELECT id, last
                            FROM authors
                            ORDER BY last DESC""",
                         connection, index_col=['id'])

title_asc = pd.read_sql("""SELECT title
                            FROM titles
                            ORDER BY title ASC""",
                        connection)

cursor = connection.cursor()
cursor.execute("""INSERT INTO authors (first, last) VALUES ('Wilson', 'Van Nice')""")
connection.commit()


# insert a new title for an author. Remember the book must have an entry in the author_ISBN table and an entry in the titles table
cursor.execute("""INSERT INTO titles (isbn,title,edition,copyright) VALUES ('0135412373','Intro to Javascript for Web Design',1,'2022')""")
cursor.execute("""INSERT INTO author_ISBN (id, isbn) VALUES (6, '0135412373')""")
connection.commit()



