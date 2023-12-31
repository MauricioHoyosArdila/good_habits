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
    calendario = relationship("Calendario", back_populates="user")
    # players = relationship("Player", back_populates="manager")


class Calendario(Base):
    __tablename__ = "calendarios"    

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="calendario")

class Habitos(Base):
    __tablename__ = "habitos"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    descripcion = Column(String)
    aprendizaje = Column(String)
    dificultad = Column(String)
    habitos_tags = relationship("HabitosTags", back_populates="habitos")


class Tags(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    habitos_tags = relationship("HabitosTags",back_populates="tags")

class HabitosTags(Base):
    __tablename__ = "habitos_tags"
    id = Column(Integer, primary_key=True, index=True)
    habitos_id = Column(Integer, ForeignKey("habitos.id"))
    habitos = relationship("Habitos", back_populates="habitos_tags")
    tags_id = Column(Integer, ForeignKey("tags.id"))
    tags = relationship("Tags", back_populates="habitos_tags")

# class Player(Base):
#     __tablename__ = "players"

#     id = Column(Integer, primary_key=True, index=True)
#     full_name = Column(String, index=False)
#     play_position = Column(String, index=True)
#     manager_id = Column(Integer, ForeignKey("users.id"))

#     manager = relationship("User", back_populates="players")