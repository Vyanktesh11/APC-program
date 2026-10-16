books = {}

def add_book(book_id, title, author):
    books[book_id] = {"title": title, "author": author, "available": True}

def search_book(book_id):
    return books.get(book_id)

def issue_book(book_id):
    if book_id in books and books[book_id]["available"]:
        books[book_id]["available"] = False
        return "Book issued."
    return "Book not available."

def return_book(book_id):
    if book_id in books:
        books[book_id]["available"] = True
        return "Book returned."
    return "Book not found."

def display_available_books():
    for book_id, book in books.items():
        if book["available"]:
            print(book_id, book)

add_book(1, "Python Basics", "A. Kumar")
add_book(2, "Data Structures", "R. Patil")
print("Search:", search_book(1))
print(issue_book(1))
print(return_book(1))
display_available_books()
