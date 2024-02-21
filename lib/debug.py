import os
import sys
# from faker import faker

# fake = faker()

from __init__ import *
from models import main

if __name__ == "__main__":
    Session = sessionmaker(bind=engine)
    session = Session()

    main()

    books = session.query(Column('books'))

    session.commit()
    session.close()