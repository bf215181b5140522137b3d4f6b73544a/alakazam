# Std lib
import os
import hashlib

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
    # Auto Fields
    user_id = Column(Integer, primary_key=True)
    # Required Fields
    name = Column(Text)
    username = Column(Text, unique=True)
    password = Column(Text)
    location = Column(Text)
    field = Column(Text)
    # Optional Fields

    def __init__(self, name, username, password, location, field):
        """
        Docstring goes here

        """
        self.name = name
        self.username = username
        self.password = self._encrypt_password(password)
        self.location = location
        self.field = field

    def validate_password(self, password):
        """
        Docstring goes here

        """
        hashed_password = hashlib.sha512(password + self.password[:40])
        return self.password[40:] == hashed_password.hexdigest()

    # "Private" Functions
    ########################################################################
    def _encrypt_password(self, password):
        """
        Docstring goes here

        """
        # Not supporting unicode passwords
        if isinstance(password, unicode):
            password = password.encode('UTF-8')
        # Use a Sha1 salt hash and a Sha512 password hash
        salt = hashlib.sha1(os.urandom(60))
        hash_ = hashlib.sha512(password + salt.hexdigest())
        return salt.hexdigest() + hash_.hexdigest()       


def initialize_sql(engine):
    DBSession.configure(bind=engine)
