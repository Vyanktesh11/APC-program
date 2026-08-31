available_books = {"Python Basics", "Java Programming", "DBMS", "C++"}
requested_books = {"Python Basics", "DBMS", "Operating Systems"}

available_requested = requested_books & available_books

print("Requested books that are available:", available_requested)
