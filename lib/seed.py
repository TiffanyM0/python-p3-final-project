from models import *
from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

fake = Faker()
if __name__ == '__main__':
    pass
    
    engine = create_engine('sqlite:///library.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # session.query(Book).delete()
    # session.query(User).delete()

    
    books = []

    for i in range(50):
        book = Book(
            title=fake.company(),
            author=fake.name(),
            published=random.randint(4, 2024),
        )

        # add and commit individually to get IDs back
        session.add(book)
        books.append(book)
        session.commit()

    users = []
    list_of_domains = (
        'com',
        'net',
        'org'
    )
    for i in range(50):  

        first = fake.unique.first_name()

        last = fake.unique.last_name()

        dns_org = fake.random_choices(
            elements=list_of_domains,
            length=1
        )[0]

        email = f"{first}.{last}.{dns_org}".lower()

        user = User(
            first_name=first,
            last_name=last,
            email=email
        )
        session.add(user)
        users.append(user)
        session.commit()
        
    session.query(Book)
    session.query(User)



