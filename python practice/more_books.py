import sqlite3

conn = sqlite3.connect("more_books.db")

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS books")
#  Create a books table with: id, title, author, pages
cursor.execute(""" CREATE TABLE IF NOT EXISTS books(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                pages INTEGER
                )""")

# Insert books
cursor.execute("INSERT INTO books(title, author, pages) VALUES (?,?,?)",
    ("The Alchemist", "Paulo Coelho", 208))
cursor.execute("INSERT INTO books(title, author, pages) VALUES (?,?,?)",
    ("Atomic Habits", "James Clear", 320))
cursor.execute("INSERT INTO books(title, author, pages) VALUES (?,?,?)",
    ("The Stranger", "Albert Camus", 123))
cursor.execute("INSERT INTO books(title, author, pages) VALUES (?,?,?)",
    ("Thinking Fast and Slow", "Daniel Kahneman", 499))

conn.commit()

# Query and print only books over 200 pages
cursor.execute("SELECT * FROM books  WHERE pages > 200")
books = cursor.fetchall()

for id, title, author, pages in books:
        print(f"{id}. {title}, {author}, {pages} pages")

# Update The Alchemist's pages to 215
cursor.execute("UPDATE books SET pages = ? WHERE title = ? ", (215, "The Alchemist"))
conn.commit()

# Print all books after the update
cursor.execute("SELECT * FROM books")
books = cursor.fetchall()
for id, title, author, pages in books:
    print(f"{id}. {title}, {author}, {pages} pages")
