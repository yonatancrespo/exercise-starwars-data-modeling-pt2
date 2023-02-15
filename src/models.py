import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

user_favorite = Table('user_favorite', Base.metadata,
                      Column('user_id', Integer, ForeignKey('user.id')),
                      Column('favorite_id', Integer, ForeignKey('favorite.id'))
                      )


# User table to represent blog users
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    favorites = relationship('Favorite', secondary=user_favorite, back_populates='users')


# Character table
class Character(Base):
    __tablename__ = 'character'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    gender = Column(String(10), nullable=False)
    birth_year = Column(String(10), nullable=False)
    height = Column(Integer, nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=False)
    planet = relationship('Planet', back_populates='characters')


# Planet table
class Planet(Base):
    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    climate = Column(String(50), nullable=False)
    terrain = Column(String(50), nullable=False)
    population = Column(Integer, nullable=False)
    characters = relationship('Character', back_populates='planet')


# Favorite table
class Favorite(Base):
    __tablename__ = 'favorite'

    id = Column(Integer, primary_key=True)
    type = Column(String(10), nullable=False)
    name = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    users = relationship('User', secondary=user_favorite, back_populates='favorites')


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
