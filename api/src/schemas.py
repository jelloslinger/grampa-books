import datetime
from typing import List

from pydantic import BaseModel


class AuthorBase(BaseModel):
    ol_id: str
    name: str


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    class Config:
        orm_mode = True


class BookBase(BaseModel):
    work_id: str
    edition_id: str = None
    image_id: str = None
    title: str


class BookCreate(BookBase):
    author_ol_ids: List[str]


class Book(BookBase):
    class Config:
        orm_mode = True


class BookWithAuthor(Book):
    authors: List[Author]


class AuthorWithBooks(Author):
    books: List[Book]


class ReadBase(BaseModel):
    date: datetime.date
    ol_book_id: str
    submitter_comment: str = None
    initials: str


class ReadCreate(ReadBase):
    pass


class Read(ReadBase):
    class Config:
        orm_mode = True


class ReadWithBook(Read):
    book: BookWithAuthor
