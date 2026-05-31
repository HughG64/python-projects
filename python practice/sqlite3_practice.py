import sqlite3

conn = sqlite3.connect("students.db")

cursor = conn.cursor()


cursor.execute("UPDATE students SET score = ? WHERE name = ?", (75, "Bruno"))
conn.commit()

cursor.execute("DELETE FROM students WHERE name = ?", ("Bruno",))
conn.commit()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for id, name, score in rows:
        print(f"{id}. {name} - {score}")

# # Create the table
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS students (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT,
#         score INTEGER
#     )
# """)

# # Save changes
# conn.commit()
# print("Table created!")

