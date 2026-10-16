from books.catalog import list_books
from books.search import search_book
from members.registry import member_details
from members.eligibility import can_borrow
from transactions.issue import issue_book
from transactions.return_book import return_book

member = member_details(1)
print("Books:", list_books())
print("Search:", search_book("Python Basics"))
print("Eligible:", can_borrow())
print(issue_book("Python Basics", member["name"]))
print(return_book("Python Basics"))
