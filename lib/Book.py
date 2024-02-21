from __init__ import *
from models import *

class Book(Base):
    __tablename__ = 'books'
    book_list = []
    books_borrowed = []

    book_id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    published = Column(Integer)
    borrowed = Column(Boolean, default=False)

    circulate = relationship('circulate', back_populates='book', uselist=False, cascade="all, delete")

    def __init__(self, title, author, published):
        self.title = title
        self.author = author
        self.published = published

    def update_status(self):
        self.__class__.books_borrowed.append([self.title, self.author, self.published])

    def __repr__(self):
        return f'Book is {self.title} ' \
               + f'{self.author}' \
               + f'{self.published}'
