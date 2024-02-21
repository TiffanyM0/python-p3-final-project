from __init__ import *
from User import User
from Book import Book
from Circulate import circulate



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

                    new_book = Book(title=title, author=author, published=published)

                    session.add(new_book)
                    session.commit()  

                    print('Book Added Successfully')

                elif choice == 2:
                    print('Looking up book')
                    keyword = input('Enter search term: ')
                    books = session.query(Book).filter(Book.title.like(f'%{keyword}%') | Book.author.like(f'%{keyword}%')).all()
                    if books:
                        for book in books:
                            print(f'Book is in the library: {book.title}, {book.author}, {book.published}')
                    else: print('-----! No book found !-----')
                
                elif choice == 3:
                    print('Displaying all books')
                    books = session.query(Book).all()
                    i =1
                    for book in books:
                        print(f'Book {i}: {book.title}, Author: {book.author}, Published in: {book.published}')
                        i+=1
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
                    first_name = input('Enter the first name: ')
                    last_name = input('Enter the last name: ')
                    email = input('Enter the email (format: firstname.lastname@gmail.com): ')

                    try:
                        new_user = User(first_name=first_name, last_name=last_name, email=email)
                        session.add(new_user)
                        session.commit()
                        print('User added successfully')
                        print(f'{User.users_list}')

                    except Exception as e:
                        session.rollback()
                        print('Error:', e)
                        print('User with this email already exists or the email is not in the correct format.')                   

                elif choice == 2:
                    print('Borrowing a book....')
                    book_to_borrow = input('Enter title of book to borrow: ')

                    book = session.query(Book).filter_by(title=book_to_borrow).first()

                    if book:
                        if not book.borrowed:
                            book.borrowed = True
                            session.commit()
                            user_id = int(input('Enter user ID: '))
                            print(f'-----! Please take {book.title} at front desk !-----')
                            new_circulate = circulate(user_id=user_id, book_id=book.book_id)
                            session.add(new_circulate)
                            session.commit()
                        else:
                            print("Book is already borrowed")
                    else:
                        print('-----! Sorry We do not have that book !-----')
                elif choice == 3:
                    pass
                    print('Showcasing Users--> ')
                    users = session.query(User).all()
                    i = 1
                    for user in users:
                        print(f'User {i}: {user.first_name}, {user.last_name}, {user.email}')
                        i +=1

                elif choice == 4:
                    print('--- Going Back.. ---')

        elif choice == 3:
            print('-----! Quiting program !-----')
    print('Program Terminated')


engine = create_engine('sqlite:///library.db')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(bind=engine)

# new_book = Book()
# session.add(new_book)
session.commit()