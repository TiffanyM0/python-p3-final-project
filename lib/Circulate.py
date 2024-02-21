from __init__ import *
from models import *

class circulate(Base):
    __tablename__ = 'circulate'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id', ondelete="CASCADE"), nullable=False, unique=True)
    book_id = Column(Integer, ForeignKey('books.book_id'), nullable=False)

    user = relationship("User", back_populates='circulate')
    book = relationship("Book", back_populates='circulate')
    #parent=relationship('Parent',back_populates='child')
