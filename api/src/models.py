from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from .database import Base

association_table = Table(
    "books_to_authors",
    Base.metadata,
    Column("book_id", Integer, ForeignKey("books.work_id")),
    Column("author_id", Integer, ForeignKey("authors.ol_id")),
)


class Book(Base):
    __tablename__ = "books"

    work_id = Column(String, primary_key=True, index=True)
    edition_id = Column(String, index=True)
    title = Column(String, unique=True, index=True)
    image_id = Column(String)

    authors = relationship("Author", secondary=association_table)
    reads = relationship("Read", back_populates="book")


class Author(Base):
    __tablename__ = "authors"

    ol_id = Column(String, primary_key=True, index=True)
    name = Column(String)

    books = relationship("Book", secondary=association_table)


class Read(Base):
    __tablename__ = "reads"

    date = Column(Date, primary_key=True, index=True)
    ol_book_id = Column(
        String, ForeignKey("books.work_id"), primary_key=True, index=True
    )
    submitter_comment = Column(String)
    initials = Column(String)

    book = relationship("Book", back_populates="reads")
