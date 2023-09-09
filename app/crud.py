from sqlalchemy.orm import Session

from . import schemas

from database import models


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    if user.password == user.password_confirmation:
        db_user = models.User(email=user.email,
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
    else:
        return schemas.ErrorMessage(message="las contraseñas no coinciden", title="malas contraseñas", code_error=403)

def create_calendario(db:Session, calendario: schemas.CreateCalendario, user:int):
    db_calendario = models.Calendario(nombre= calendario.nombre,
                                      user_id= user)
    db.add(db_calendario)
    db.commit()
    db.refresh(db_calendario)
    return db_calendario

# def get_players(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Player).offset(skip).limit(limit).all()


# def create_user_player(db: Session, player: schemas.PlayerCreate, user_id: int):
#     db_player = models.Player(**player.dict(), manager_id=user_id)
#     db.add(db_player)
#     db.commit()
#     db.refresh(db_player)
#     return db_player