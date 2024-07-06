# from helpers import (
#     exit_program,
#     display_books,
#     display_authors,
#     add_author,
#     add_book,
#     delete_book,
#     find_books_by_author
# )

# def main():
#     while True:
#         menu()
#         choice = input("> ")
#         if choice == "0":
#             exit_program()
#         elif choice == "1":
#             display_books()
#         elif choice == "2":
#             display_authors()
#         elif choice == "3":
#             add_author()
#         elif choice == "4":
#             add_book()
#         elif choice == "5":
#             delete_book()
#         elif choice == "6":
#             find_books_by_author()
#         else:
#             print("Invalid choice")

# def menu():
#     print("Please select an option:")
#     print("0. Exit the program")
#     print("1. Display books")
#     print("2. Display authors")
#     print("3. Add author")
#     print("4. Add book")
#     print("5. Delete book")
#     print("6. Find books by author")

# if __name__ == "__main__":
#     main()

import click
from helpers import (
    exit_program,
    display_books,
    display_authors,
    add_author,
    add_book,
    delete_book,
    find_books_by_author
)

@click.group()
def cli():
    pass

@cli.command(name="exit")
def exit_cmd():
    """Exit the program"""
    exit_program()

@cli.command(name="books")
def books_cmd():
    """Display books"""
    display_books()

@cli.command(name="authors")
def authors_cmd():
    """Display authors"""
    display_authors()

@cli.command(name="add-author")
def add_author_cmd():
    """Add an author"""
    add_author()

@cli.command(name="add-book")
def add_book_cmd():
    """Add a book"""
    add_book()

@cli.command(name="delete-book")
def delete_book_cmd():
    """Delete a book"""
    delete_book()

@cli.command(name="find-books-by-author")
def find_books_by_author_cmd():
    """Find books by author"""
    find_books_by_author()

if __name__ == "__main__":
    cli()
