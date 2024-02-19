def main ():
    print ('Hello!!')
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

class Library:
    def __init__(self) -> None:
        pass


class User:
    def __init__(self):
        self.name = input('Enter the name of the user >>>')
        self.email = input('Enter the email of the user >>>')

        #user tasks; 
        # implement email check on input
        #add user functionality and linking to database

class Book:
    book_list = []
    def __init__(self):
        self._name = input('Enter the name of the book >>>')
        self._author = input('Enter the name of the Author >>>')
        self._pages = input('Enter the number of the Pages >>>')

        #dict or list ??
        Book.book_list.append([self._name, self._author, self._pages])
        print(Book.book_list)




if __name__ == "__main__":
    main()