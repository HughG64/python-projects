import sqlite3

conn = sqlite3.connect("phone_book.db")

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS phone_book")
# Creates a contacts table — id, name, phone, email

cursor.execute("""CREATE TABLE IF NOT EXISTS phone_book(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               phone TEXT,
               email TEXT
               )""")

conn.commit()

# Has a Contact class with __str__ that prints nicely
class Contact:
    def __init__(self,name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return (f"Name: {self.name}\n Phone no.:{self.phone}\nEmail: {self.email}\n")

    # Has these functions:
    # add_contact(name, phone, email) — inserts into db
def add_contact(name, phone, email):
    cursor.execute("INSERT INTO phone_book(name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    return conn.commit()


# get_all_contacts() — returns all contacts as Contact objects
def get_all_contacts():
    cursor.execute("SELECT * FROM phone_book")
    contacts = cursor.fetchall()
    return [Contact(name, phone, email) for id, name, phone, email in contacts]

# search_contact(name) — finds a contact by name
def search_contact(name):
    cursor.execute("SELECT * FROM phone_book WHERE name = ?", (name,))
    result = cursor.fetchone()
    if result:
        id, name, phone, email = result
        return Contact(name, phone, email)

# Add 3 contacts
add_contact("Thabo Nkosi", "082 345 6789", "thabo@gmail.com")
add_contact("Lerato Dlamini", "071 234 5678", "lerato@outlook.com")
add_contact("Sipho Mahlangu", "063 456 7890", "sipho@gmail.com")

# Print all contacts
for contact in get_all_contacts():
    print(contact)

# Search for one by name and print it
print(search_contact("Thabo Nkosi"))
