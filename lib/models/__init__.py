from .database import Base, engine, SessionLocal, init_db
from .author import Author
from .book import Book

init_db()
