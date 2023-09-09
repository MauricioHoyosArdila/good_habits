from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    name = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    phone_number = Column(String, unique=True)
    user_name = Column(String, unique=True, index=True)
    # players = relationship("Player", back_populates="manager")


class Habitos(Base):
    __tablehabitos__ = "habitos"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    descripcion = Column(String)
    aprendizaje = Column(String)
    dificulta = Column(String)

class Tags(Base):
    __tablehabitos__ = "tags"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    habito = relationship("Habitos", back_populates="manager")


# class Player(Base):
#     __tablename__ = "players"

#     id = Column(Integer, primary_key=True, index=True)
#     full_name = Column(String, index=False)
#     play_position = Column(String, index=True)
#     manager_id = Column(Integer, ForeignKey("users.id"))

#     manager = relationship("User", back_populates="players")