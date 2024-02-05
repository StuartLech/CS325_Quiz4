from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    isbn: str
    publication_year: int

if __name__ == "__main__":
    book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "978-0345391803", 1979)
    book2 = Book("1984", "George Orwell", "978-0451524935", 1949)

    print(book1)
    print(book2)
