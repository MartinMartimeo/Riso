# This script comes without any warranty or support.
# Use on own risk and fun.

import sqlalchemy
import sqlalchemy.orm

from sqlalchemy import Column, ForeignKey
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import relationship

from classes.dbbase import DbBase

"""
    Represents a Room with his Objects and Directions
"""

class DbRoom(DbBase):
    __tablename__ = "room"

    id = Column(Integer, primary_key=True, nullable=False)

    title = Column(Text, nullable=False)

    def __init__(self, title):
        self.title = title

class DbRoomDirection(DbBase):
    __tablename__ = "room_direction"

    char = Column(String(1), primary_key=True, nullable=False)

    room_id = Column(Integer, ForeignKey("room.id"), nullable=False)
    room = relationship("DbRoom", backref="directions")

    to_id = Column(Integer, ForeignKey("room.id"), nullable=True)

    def __init__(self, char, room, to=None):

        self.char = char
        self.room_id = room

class DbRoomObject(DbBase):
    __tablename__ = "rom_object"

    id = Column(Integer, primary_key=True, nullable=False)

    room_id = Column(Integer, ForeignKey("room.id"), nullable=False)
    room = relationship("DbRoom", backref="directions")

    name = Column(Text, nullable=False)

    def __init__(self, room, name):

        self.room_id = room
        self.name = name

