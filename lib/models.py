from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///books.db')
Session = sessionmaker(bind=engine)
session = Session()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    books = relationship('Book', back_populates='author', cascade='all, delete, delete-orphan')

    def __repr__(self):
        return f"<Author(name={self.name})>"

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    author = relationship('Author', back_populates='books')

    def __repr__(self):
        return f"<Book(title={self.title}, genre={self.genre})>"

Base.metadata.create_all(engine)
