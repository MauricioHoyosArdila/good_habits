from sqlalchemy.orm import Session

from . import schemas

from database import models
import re

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

c = r'^(?=.[A-Z])(?=.[a-z])(?=.[^a-zA-Z0-9])(?=.#).+$'





def create_user(db: Session, user: schemas.UserCreate):
    if user.password != user.password_confirmation:
        return schemas.ErrorMessage(message="las contraseñas no coinciden", title="malas contraseñas", code_error=422)
    elif len(user.phone_number) < 10 or len(user.phone_number) > 14:
        return schemas.ErrorMessage(message="El numero de telefono no coincide con la cantidad de digitos necesarios", title="Numero invalido", code_error=422)
    elif user.email == None or user.email == ""  or user.password == None or user.password == "" or user.name == None or user.name == "" or user.lastname == None or user.lastname == "" or user.age == None or user.age == "" or user.phone_number == None or user.phone_number == "" or user.user_name == None or user.user_name == "":   
        return schemas.ErrorMessage(message="Algunos campos estan vacios", title="Espacios vacios", code_error=422)
    elif re.match(c, user.password):
        return True 
    else: db_user = models.User(email=user.email,
        hashed_password=user.password,
        name=user.name,
        lastname=user.lastname,
        age=user.age,
        phone_number=user.phone_number,
        user_name=user.user_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
         
    


# def get_players(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Player).offset(skip).limit(limit).all()


# def create_user_player(db: Session, player: schemas.PlayerCreate, user_id: int):
#     db_player = models.Player(**player.dict(), manager_id=user_id)
#     db.add(db_player)
#     db.commit()
#     db.refresh(db_player)
#     return db_player