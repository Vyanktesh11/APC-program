books = {}

def add_book(book):
    books[book] = True

def issue_book(book):
    if book in books and books[book]:
        books[book] = False
        print("Book issued")
    else:
        print("Book is not available")

def return_book(book):
    if book in books:
        books[book] = True
        print("Book returned")
    else:
        print("Book not found")

def search_book(book):
    if book in books:
        print("Book found")
    else:
        print("Book not found")

def display_available_books():
    print("Available books:")
    for book, available in books.items():
        if available:
            print(book)

add_book("Python")
add_book("Java")
add_book("C++")

issue_book("Python")
search_book("Java")
return_book("Python")
display_available_books()
