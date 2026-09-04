# OOP Practice Problem: Library Management System (Mini Version)

# 🎯 Problem Statement:

# Design a simple Book class and a Library class.
# A Book should have:
# title (str)
# author (str)
# available (bool — whether it is currently available or not)

# A Library should:
# Maintain a list of books
# Allow you to add a new book
# Allow you to borrow a book (i.e., mark it unavailable)
# Allow you to return a book (i.e., mark it available again)
# Show the list of available books

class Book():

    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library():

    def __init__(self):
        self.collection_of_books = {}
        self.borrowed_books = {}

    def add_new_book(self, b):
        self.collection_of_books[b.title] = f"{b.title} by {b.author}"
        print(f"{b.title} by {b.author} is added to our library 👍")

    def borrow_book(self, title):
        if title not in self.collection_of_books:
            print()
            print("Book is already borrowed.")
        else:
            self.borrowed_books[title] = self.collection_of_books.pop(title)
            print()
            print(f"{title} has been borrowed.")

    def return_book(self, title):
        if title in self.borrowed_books:
            self.collection_of_books[title] = self.borrowed_books[title]
            print()
            print(f"{title} is returned back.")
        else:
            print()
            print(f"{title} was not borrowed from our library")


    def display_available_books(self):
        print()
        print("Available Books:")
        for key in self.collection_of_books:
            print(self.collection_of_books[key])



b1 = Book("One Piece", "Eiichiro Oda")
b2 = Book("Naruto", "Masashi Kishimoto")

lib = Library() # A Library instance
lib.add_new_book(b1)
lib.add_new_book(b2)

lib.display_available_books()

lib.borrow_book("One Piece")

lib.display_available_books()

lib.borrow_book("One Piece")

lib.return_book("One Piece")

lib.display_available_books()