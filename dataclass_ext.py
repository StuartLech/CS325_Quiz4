from dataclasses import dataclass
from datetime import datetime

@dataclass
class Book:
    title: str
    author: str
    isbn: str
    publication_year: int

    def age(self) -> int:
        """Calculate the age of the book."""
        current_year = datetime.now().year
        return current_year - self.publication_year

if __name__ == "__main__":
    book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "978-0345391803", 1979)
    book2 = Book("1984", "George Orwell", "978-0451524935", 1949)

    print(f"{book1.title} is {book1.age()} years old.")
    print(f"{book2.title} is {book2.age()} years old.")
