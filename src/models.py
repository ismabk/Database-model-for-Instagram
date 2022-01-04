import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(30), nullable=False)

class Storie(Base):
    __tablename__ = 'stories'
    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey('users.id'))

class Feed(Base):
    __tablename__ = 'feeds'
    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey('users.id'))
    comments = Column(String, nullable=True)

class Direct(Base):
    __tablename__ = 'directs'
    id = Column(Integer, primary_key=True)
    user_orig = Column(Integer, ForeignKey('users.id'))
    user_dest = Column(Integer, ForeignKey('users.id'))
    dir_storie = Column(Integer, ForeignKey('stories.id'))
    dir_feed = Column(Integer, ForeignKey('feeds.id'))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')