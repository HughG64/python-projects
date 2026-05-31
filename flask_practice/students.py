import sqlite3

conn = sqlite3.connect("students.db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    score INTEGER
    )""")

conn.commit()

cursor.execute("INSERT INTO students (name, score) VALUES (?, ?)", ("Bruno", 75))
cursor.execute("INSERT INTO students (name, score) VALUES (?, ?)", ("Fums", 45))
cursor.execute("INSERT INTO students (name, score) VALUES (?, ?)", ("Mila", 98))

conn.commit()
