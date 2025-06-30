class Book:
    def __init__(self,title,author,year,available):
        self.title=title
        self.author=author
        self.year=year
        self.available = available

    def __str__(self):
        if self.available==True:
            return f"{self.title} by {self.author} ({self.year}) - Available"
        else:
            return f"{self.title} by {self.author} ({self.year}) - Unavailable"



class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        if book not in self.books:
            self.books.append(book)
            print("Succesfully added book")
        else:
            print("This book is already in the library")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.available:
                    print("This book is already borrowed.")
                    return
                book.available = False
                print("Book borrowed.")
                return
        print("No book found.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.available:
                    print("This book was not borrowed.")
                    return
                book.available = True
                print("Book returned.")
                return
        print("No book found.")

    def list_books(self):
        print("\n --- ALL BOOKS ---")
        for book in self.books:
           print( book.__str__())


library = Library()
hobbit  = Book("Hobbit","J.R.R Tolkien",1937,True)
gOrwel = Book("1984","George Orwell",1949,True)
pride = Book("Pride and Prejudice","Jane Austen",1813,True)

library.add_book(hobbit)
library.add_book(gOrwel)
library.add_book(pride)

while True:
    print("1.View all books.")
    print("2. Borrow a book.")
    print("3.Return a book.")
    print("4.Exit.")

    action = int(input("Choose an action: "))

    if action == 1:
        library.list_books()

    elif action == 2:
        book_title = input("Enter the title of the book to borrow: ")
        library.borrow_book(book_title)

    elif action == 3:
        book_title = input("Enter the title of the book to return: ")
        library.return_book(book_title)

    elif action == 4:
        break
    else:
        print("Invalid option!")

    goagain = input("Continue? (y/n): ").strip().lower()
    if goagain != "y":
        break






