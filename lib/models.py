from sqlalchemy import create_engine,UniqueConstraint, ForeignKey, PrimaryKeyConstraint, Table, Column, Integer, Boolean, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

engine = create_engine('sqlite:///library.db', echo=True)
Base = declarative_base()

def main ():
    # intro > book or user 
    # book > add, look, borrow, display
    # book.add > title, author, published
    # book.look > search book by title/author
    # book.borrow> if book != book in borrowed-list => user-email and borrow 
    # book.display > list all books, with status of borrowing
    # user > register, book with user
    # user.register > add name, email != email in database 
    # user.book with user > lookup borrowed book by user id

    print ('***** Welcome to LibraryCLI *****')
    choice = 0
    while choice != 3:
        print('--!> Celebrating Words, Ideas and Community <!--')
        print('1) Books Management')
        print('2) User Management')
        print('3) Exit')
        choice = int(input())

        if choice == 1:
            while choice != 4:
                print('*** Book Manager ***')
                print('1) Add a book')
                print('2) Lookup a Book')
                print('3) Display books')
                print('4) Back')
                choice = int(input())

                if choice == 1:
                    print('Adding a book...')
                    title = input('Enter the title of the book: ')
                    author = input('Enter the name of the author: ')
                    published = int(input('Enter the year of publication: '))

                    new_book = Book(book_title=title, book_author=author, published=published)

                    session.add(new_book)
                    session.commit()  

                    print('Book Added Successfully')
                    print(Book.book_list)  

                elif choice == 2:
                    print('Looking up book')
                    keyword = input('Enter search term: ')
                    for book in Book.book_list:
                        if keyword in book:
                            print(book)
                    print('-----! No book found !-----')
                
                elif choice == 3:
                    print('Displaying all books')
                    for i in range(len(Book.book_list)):
                        print(Book.book_list[i])
                elif choice == 4:
                    print('--- Going Back.. ---')

        elif choice == 2:
            while choice != 4:
                print('*** User Manager ***')
                print('1) Register')
                print('2) Borrow a book')
                print('3) View users')
                print('4) Back')
                choice = int(input())

                if choice == 1:
                    print('--- Setting up User ---')
                    first_name = input('Enter the first name of the user: ')
                    last_name = input('Enter the last name of the user: ')
                    email = input('Enter the email of the user: ')

                    new_user = User(first_name=first_name, last_name=last_name, email=email)

                    session.add(new_user)
                    session.commit()                    
                    
                    print('User added successfully')
                    print(f'{User.users_list}')

                elif choice == 2:
                    print('Borrowing a book....')
                    book_to_borrow=input('Enter title of book to borrow >>> ')

                    for book in Book.book_list:
                        if book == book_to_borrow:
                            for item in Book.books_borrowed:
                                if book_to_borrow == item:
                                    print("Book is Unavailable")
                                else:
                                    Book.books_borrowed.append(book_to_borrow)
                                    print(f'-----! Please take {Book._title} at front desk !-----')
                    print('-----! Sorry We do not have that book !-----')
                elif choice == 3:
                    pass
                    print('Showcasing Users--> ')
                    for i in range(len(User.users_list)):
                        print(User.users_list[i])

                elif choice == 4:
                    print('--- Going Back.. ---')

        elif choice == 3:
            print('-----! Quiting program !-----')
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

    def __init__(self, title, author, published):
        self.book_title = title
        self.book_author = author
        self.published = published
        #dict or list ??
        Book.book_list.append([self.book_title, self.book_author, self.published])
        # print(Book.book_list)
    
    def update_status(self):
        self.__class__.books_borrowed.append([self.title, self.author, self.published])


    def __repr__(self):
        return f'Book is {self.title} '\
        + f'{self.author}' \
        + f'{self.published}'


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
    first_name = Column('user_firstname', String)
    last_name = Column('user_lastname', String)
    email = Column('user_email', String, unique=True)

    circulate = relationship('circulate', back_populates="users", uselist=False,cascade="all, delete")
    # book_borrowed = Column('Borrowed', ForeignKey=('book_id'))

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        # user tasks; 
        # implement email check on input
        #add user functionality and linking to database
        User.users_list.append([self.first_name, self.last_name, self.email])

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

engine = create_engine('sqlite:///library.db')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(bind=engine)

# new_book = Book()
# session.add(new_book)
session.commit()