# import sqlite3

# def helper_1():
#     print("Performing useful function #1.")

# def display_books():
#     try:
#         conn = sqlite3.connect('create.db')
#         cursor = conn.cursor()

#         cursor.execute("SELECT title, author, genre FROM books")
#         books = cursor.fetchall()

#         if books:
#             print("\nBooks in the database:")
#             for book in books:
#                 print(f"Title: {book[0]}, Author: {book[1]}, Genre: {book[2]}")
#         else:
#             print("No books found in the database.")

#     except sqlite3.Error as e:
#         print(f"An error occurred: {e}")
    
#     finally:
#         if conn:
#             conn.close()

# def exit_program():
#     print("Goodbye!")
#     exit()

from models import Author, Book, SessionLocal

def exit_program():
    print("Bye Bye!")
    exit()

def display_books():
    session = SessionLocal()
    books = session.query(Book).all()
    if books:
        print("\nBooks in the database:")
        for book in books:
            author_name = book.author.name if book.author else "Unknown"
            print(f"Title: {book.title}, Author: {author_name}, Genre: {book.genre}")
    else:
        print("No books found in the database.")
    session.close()

def display_authors():
    session = SessionLocal()
    authors = session.query(Author).all()
    if authors:
        print("\nAuthors in the database:")
        for author in authors:
            print(f"Name: {author.name}")
    else:
        print("No authors found in the database.")
    session.close()

def add_author():
    name = input("Enter author's name: ")
    new_author = Author(name=name)
    session = SessionLocal()
    session.add(new_author)
    session.commit()
    print(f"Author '{name}' added.")
    session.close()

def add_book():
    title = input("Enter book title: ")
    genre = input("Enter book genre: ")
    display_authors()
    author_id = int(input("Enter author ID: "))
    session = SessionLocal()
    author = session.query(Author).get(author_id)
    if author:
        new_book = Book(title=title, genre=genre, author_id=author_id)
        session.add(new_book)
        session.commit()
        print(f"Book '{title}' added.")
    else:
        print(f"No author found {author_id}. Book not added.")
    session.close()

def delete_book():
    display_books()
    book_id = int(input("Enter book number to delete: "))
    session = SessionLocal()
    book_to_delete = session.query(Book).get(book_id)
    if book_to_delete:
        session.delete(book_to_delete)
        session.commit()
        print(f"Book '{book_to_delete.title}' deleted.")
    else:
        print("Book not found.")
    session.close()

def find_books_by_author():
    display_authors()
    author_id = int(input("Enter author number to view their books: "))
    session = SessionLocal()
    author = session.query(Author).get(author_id)
    if author and author.books:
        print(f"\nBooks by {author.name}:")
        for book in author.books:
            print(f"Title: {book.title}, Genre: {book.genre}")
    else:
        print("No books found for this author.")
    session.close()
