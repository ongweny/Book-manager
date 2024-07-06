from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    books = relationship('Book', back_populates='author', cascade='all, delete, delete-orphan')

    def __repr__(self):
        return f"<Author(name={self.name})>"
