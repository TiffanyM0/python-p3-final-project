from sqlalchemy import create_engine,UniqueConstraint, ForeignKey, PrimaryKeyConstraint, Table, Column, Integer, Numeric, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

def main ():
    print ('Welcome to LibraryCLI!!')
    book_list = []
    choice = 0
    while choice != 5:
        print('*** Book Manager ***')
        print('1) Add a book')
        print('2) Lookup a Book')
        print('3) Display books')
        print('4) Add user')
        print('5) Quit')
        choice = int(input())

        if choice == 1:
            print('Adding a book...')
            Book()

        elif choice == 2:
            print('Looking up book')
            keyword = input('Enter search term: ')
            for book in book_list:
                if keyword in book:
                    print(book)
        
        elif choice == 3:
            print('Displaying all books')
            for i in range(len(book_list)):
                print(book_list[i])
        
        elif choice == 4:
            print('--- Setting up User ---')
            User()

        elif choice == 5:
            print('Quiting program...')
    
    print('Program Terminated')

class Book(Base):
    
    book_list = []

    __tablename__ = 'books'
    book_id = Column('book_id', Integer, primary_key=True)
    book_title = Column('Book_Title', String)


    def __init__(self):
        self._name = input('Enter the name of the book >>>')
        self._author = input('Enter the name of the Author >>>')
        self._pages = input('Enter the number of the Pages >>>')

        #dict or list ??
        Book.book_list.append([self._name, self._author, self._pages])
        print(Book.book_list)
    
    def __repr__(self):
        return f'Book is {self._name} '\
        + f'{self._author}' \
        + f'{self._pages}'


class User(Base):
    __tablename__ = 'users'
    __table_args__ = (
        UniqueConstraint(
            'User_Email',
            name='unique_email'
        ),
    )
    id = Column('User_Id', Integer, primary_key=True)
    name = Column('User_Name', String)
    email = Column('User_Email', String)
    # book_borrowed = Column('Borrowed', ForeignKey=('book_id'))


    def __init__(self):
        self.name = input('Enter the name of the user >>>')
        self.email = input('Enter the email of the user >>>')

        #user tasks; 
        # implement email check on input
        #add user functionality and linking to database
    def __repr__(self):
        return f"User {self.name}: " \
        + f"{self.email}"

engine = create_engine("sqlite:///db/library.db", echo=True)
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    Session = sessionmaker(bind=engine)
    session = Session()

    main()
    books = session.query()
    session.commit()