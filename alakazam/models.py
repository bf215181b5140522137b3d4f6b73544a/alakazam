# 3rd party
from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class User(Base):
    """
    Docstring goes here

    """
    __tablename__ = 'User'
    id_ = Column(Integer, primary_key=True)
    email = Column(Text, unique=True)
    pass_ = Column(Text)
    
    def __init__(self, email, pass_):
        self.email = email
        self.pass_ = pass_

def initialize_sql(engine):
    DBSession.configure(bind=engine)
