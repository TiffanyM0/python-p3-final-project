from sqlalchemy import create_engine,UniqueConstraint, ForeignKey, PrimaryKeyConstraint, Table, Column, Integer, Boolean, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

engine = create_engine('sqlite:///library.db', echo=True)
Base = declarative_base()
Base.metadata.create_all(bind=engine)

def main ():
    print ('*****Welcome to LibraryCLI!!*****')
    choice = 0
    while choice != 6:
        print('*** Book Manager ***')
        print('1) Add a book')
        print('2) Lookup a Book')
        print('3) Display books')
        print('4) Add user')
        print('5) Borrow a book')
        print('6) Quit')
        choice = int(input())

        if choice == 1:
            print('Adding a book...')
            Book()
            print('Book Added Successfully')
            print(Book.book_list)           

        elif choice == 2:
            print('Looking up book')
            keyword = input('Enter search term: ')
            for book in Book.book_list:
                if keyword in book:
                    print(book)
        
        elif choice == 3:
            print('Displaying all books')
            for i in range(len(Book.book_list)):
                print(Book.book_list[i])
        
        elif choice == 4:
            print('--- Setting up User ---')
            User()
            print('User added successfully')
            print(f'{User.users_list}')
        
        # borrowing book should update book borrowed table.
        elif choice == 5:
            print('Borrowing a book....')
            book_to_borrow=input('Enter title of book to borrow >>> ')
            for book in Book.book_list:
                for item in Book.books_borrowed:
                    if book_to_borrow == item:
                        print("Book is Unavailable")
                    else:
                        Book.books_borrowed.append(book_to_borrow)
                        print(f'<<< Please take {Book._title} at front desk >>>')

        elif choice == 6:
            print('Quiting program...')
    
    print('Program Terminated')

class Book(Base):
    book_list = []
    books_borrowed = []

    __tablename__ = 'books'
    book_id = Column('book_id', Integer, primary_key=True)
    book_title = Column('Book_Title', String)
    book_author = Column('Author', String)
    published = Column('Year Published', Integer)
    borrowed = Column(Boolean(), default=False)

    # child=relationship('Child',back_populates='parent',uselist=False,cascade="all, delete")
    circulate = relationship('circulate',back_populates='books', uselist=False,cascade="all, delete" )

    def __init__(self):
        self._title = input('Enter the name of the book >>>')
        self._author = input('Enter the name of the Author >>>')
        self._published = input('Enter the year of publication >>>')

        #dict or list ??
        Book.book_list.append([self._title, self._author, self._published])
        # print(Book.book_list)
    
    def update_status(self):
        self.__class__.books_borrowed.append([self._title, self._author, self._published])


    def __repr__(self):
        return f'Book is {self._title} '\
        + f'{self._author}' \
        + f'{self._published}'


class User(Base):
    __tablename__ = 'users'
    users_list= []
    # __table_args__ = (
    #     UniqueConstraint(
    #         'User_Email',
    #         name='unique_email'
    #     ),
    # )
    user_id = Column('user_id', Integer, primary_key=True)
    name = Column('user_Name', String)
    email = Column('user_Email', String, unique=True)

    circulate = relationship('circulate', back_populates="users", uselist=False,cascade="all, delete")
    # book_borrowed = Column('Borrowed', ForeignKey=('book_id'))

    def __init__(self):
        self.name = input('Enter the name of the user >>>')
        self.email = input('Enter the email of the user >>>')
        #user tasks; 
        # implement email check on input
        #add user functionality and linking to database
        User.users_list.append([self.name, self.email])

    def __repr__(self):
        return f"User {self.__class__.name}: " \
        + f"{self.__class__.email}"

class circulate(Base):
    __tablename__ = 'circulate'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id', ondelete="CASCADE"), nullable=False, unique=True)
    book_id = Column(Integer, ForeignKey('books.book_id'), nullable=False)

    books = relationship("Book", back_populates='circulate')
    users = relationship("User", back_populates='circulate')
    #parent=relationship('Parent',back_populates='child')

