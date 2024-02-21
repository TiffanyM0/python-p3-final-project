from __init__ import *
from models import *

class User(Base):
    __tablename__ = 'users'
    users_list= []
    __table_args__ = (
        UniqueConstraint('user_email', name='unique_email'),
    )

    user_id = Column('user_id', Integer, primary_key=True)
    first_name = Column('user_firstname', String)
    last_name = Column('user_lastname', String)
    email = Column('user_email', String, unique=True)

    circulate = relationship('circulate', back_populates="user", uselist=False,cascade="all, delete")
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
        return f"User {self.first_name}: " \
        + f"{self.last_name}" \
        + f"{self.email}"
