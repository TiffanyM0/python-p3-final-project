from sqlalchemy import create_engine,UniqueConstraint, ForeignKey, PrimaryKeyConstraint, Table, Column, Integer, Boolean, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine('sqlite:///library.db', echo=True)
Base = declarative_base()