class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
    
    def __repr__(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.__repr__()


class Book:
    def __init__(self, title: str, author: Person):
        self.title = title
        self.author = author
    
    def __repr__(self):
        return f"{self.title} ({self.author})"
    
    def __str__(self):
        return self.__repr__()


class LibraryError(Exception):
    """Base class for Library errors"""


class Library:
    def __init__(self, name: str):
        self.name = name
        self._books = []
        self._members = set()
        self._borrowed_books = {}

    def __repr__(self):
        return f"Library(name='{self.name}')"

    def __str__(self):
        return f"{self.name} ({len(self._books)} livres, {len(self._members)} membres)"

    def is_book_available(self, book: Book) -> bool:
        if book not in self._books:
            raise LibraryError(f"Le livre {book.title} n'existe pas dans le catalogue")
        
        return book not in self._borrowed_books

    def borrow_book(self, book: Book, person: Person) -> None:
        if person not in self._members:
            raise LibraryError(f"{person} n'est pas membre de la bibliothèque")
        
        if book not in self._books:
            raise LibraryError(f"Le livre {book.title} n'existe pas dans le catalogue")
        
        if book in self._borrowed_books:
            raise LibraryError(f"Le livre {book.title} est déjà emprunté")
        
        self._borrowed_books[book] = person

    def return_book(self, book: Book) -> None:
        if book not in self._borrowed_books:
            raise LibraryError(f"Le livre {book.title} n'était pas emprunté")
        
        del self._borrowed_books[book]

    def add_new_member(self, person: Person) -> None:
        """Ajoute un nouveau membre à la bibliothèque"""
        if person in self._members:
            raise LibraryError(f"{person} est déjà membre de la bibliothèque")
        self._members.add(person)

    def add_new_book(self, book: Book) -> None:
        """Ajoute un nouveau livre au catalogue de la bibliothèque"""
        if book in self._books:
            raise LibraryError(f"Le livre {book.title} existe déjà dans le catalogue")
        self._books.append(book)

    def print_status(self) -> None:
        """Affiche l'état actuel de la bibliothèque"""
        print(f"\n{self.name} status:")
        print(f"Books catalogue: {self._books}")
        print(f"Members: {self._members}")
        
        
        available_books = [book for book in self._books if book not in self._borrowed_books]
        print(f"Available books: {available_books}")
        
        print(f"Borrowed books: {self._borrowed_books}")
        print("-----")



def main():
    """Test your code here"""
    antoine = Person("Antoine", "Dupont")
    print(antoine)

    julia = Person("Julia", "Roberts")
    print(julia)

    rugby_book = Book("Jouer au rugby pour les nuls", Person("Louis", "BB"))
    print(rugby_book)

    novel_book = Book("Vingt mille lieues sous les mers", Person("Jules", "Verne"))
    print(novel_book)

    library = Library("Public library")
    library.print_status()

    library.add_new_book(rugby_book)
    library.add_new_book(novel_book)
    library.add_new_member(antoine)
    library.add_new_member(julia)
    library.print_status()

    print(f"Is {rugby_book} available? {library.is_book_available(rugby_book)}")
    library.borrow_book(rugby_book, antoine)
    library.print_status()

    try:
        library.borrow_book(rugby_book, julia)
    except LibraryError as error:
        print(error)

    try:
        library.borrow_book(Book("Roméo et Juliette", Person("William", "Shakespeare")), julia)
    except LibraryError as error:
        print(error)

    try:
        library.borrow_book(novel_book, Person("Simone", "Veil"))
    except LibraryError as error:
        print(error)

    try:
        library.return_book(novel_book)
    except LibraryError as error:
        print(error)

    library.return_book(rugby_book)
    library.borrow_book(novel_book, julia)
    library.print_status()

    library.borrow_book(rugby_book, julia)
    library.print_status()


if __name__ == "__main__":
    main()