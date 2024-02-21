import os
import sys


from models import *

if __name__ == "__main__":
    Session = sessionmaker(bind=engine)
    session = Session()
    book1 = Book('Alice in Wonderland', 'J Schout', 232)
    
    main()
    books = session.query()
    session.commit()
    session.close()