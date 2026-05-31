# OOP Practice Challenge
# You're building a simple Book tracker.
# Build a Book class that:
# Stores title, author and pages

class Books:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

# Has a __str__ method that prints like:
# The Alchemist by Paulo Coelho (208 pages)

    def __str__(self):
        return (f"{self.title} by {self.author} ({self.pages} pages)")

# Has a method called is_long() that returns True if the book is over 300 pages, False if not

    def is_long(self):
        return self.pages > 300

# Outside the class:
# Create a list of 4 books — at least 2 over 300 pages

books = [
    Books("The Alchemist", "Paulo Coelho", 208),
    Books("The Myth of Sisyphus", "Albert Camus", 600),
    Books("The Stranger", "Albert Camus", 350),
    Books("The Incompetent", "Fumani Mabasa", 11),
]

# Loop through and print each book using print()

for book in books:
    print(book)

# Print only the titles of long books using a list comprehension

long_reads = [n.title for n in books if n.is_long()]
print(long_reads)

