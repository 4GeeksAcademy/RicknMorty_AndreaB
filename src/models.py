import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base, relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

character_episode_table = Table(
    "character_episode_table",
    Base.metadata,
    Column("character_id", ForeignKey("character.id")),
    Column("episode_id", ForeignKey("episode.id")),
    )

character_location_table = Table(
    "character_location_table",
    Base.metadata,
    Column("character_id", ForeignKey("character.id")),
    Column("location_id", ForeignKey("location.id")),
    )

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    image = Column(String(250), nullable=False)
    species = Column(String (100), nullable=False)
    status = Column(String(50), nullable=False)
    episode = relationship("Episode", secondary=character_episode_table, back_populates="charaters")
    type = Column(String(50), nullable=False)
    url = Column(String(250), nullable=False)
    location = relationship("Location")
    origin = relationship("Location")



class Episode(Base):
    __tablename__ = 'episode'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    episode = Column(String(50), nullable=False)
    air_date = Column(String(20), nullable=False)
    created = Column(String(50), nullable=False)
    episode = Column(String(50), nullable=False)
    name  =  Column(String(50), nullable=False)
    url = Column(String(250), nullable=False)
    characters = relationship("Character", secondary=character_episode_table, back_populates="episodes")


class Location(Base):
     __tablename__ = 'location'
     id = Column(Integer, primary_key=True)
     created = Column(String(40), nullable=False)
     dimension = Column(String(50), nullable=False)
     name = Column(String(50), nullable=False)
     residents = relationship("Character")
     type = Column(String(50), nullable=False)
     url = Column(String(250), nullable=False)



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
