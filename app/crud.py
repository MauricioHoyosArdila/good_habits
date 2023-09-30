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

c = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$'





def create_user(db: Session, user: schemas.UserCreate):
    if user.password != user.password_confirmation:
        return schemas.ErrorMessage(message="las contraseñas no coinciden", title="malas contraseñas", code_error=422)
    elif len(user.phone_number) < 10 or len(user.phone_number) > 14:
        return schemas.ErrorMessage(message="El numero de telefono no coincide con la cantidad de digitos necesarios", title="Numero invalido", code_error=422)
    elif user.email == None or user.email == ""  or user.password == None or user.password == "" or user.name == None or user.name == "" or user.lastname == None or user.lastname == "" or user.age == None or user.age == "" or user.phone_number == None or user.phone_number == "" or user.user_name == None or user.user_name == "":   
        return schemas.ErrorMessage(message="Algunos campos estan vacios", title="Espacios vacios", code_error=422)
    elif not re.match(c, user.password):
        return schemas.ErrorMessage(message="La contraseña debe cumplir con todos los requisitos", title="Contraseña incorrecta", code_error=422) 
    else: db_user = models.User(email=user.email,
        hashed_password=user.password,
        name=user.name,
        lastname=user.lastname,
        age=user.age,
        phone_number=user.phone_number,
        user_name=user.user_name)
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as e:
        print(e)
        return schemas.ErrorMessage(message=str(e), title="Error", code_error=422)
    return db_user
         
    


def get_tags_from_name(db:Session, name:str):
    return db.query(models.Tags).filter(models.Tags.titulo== name).first()

def create_tag(db:Session, tag:schemas.TagsBase):
    db_tag = models.Tags(titulo=tag.titulo)
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

def get_tags_ids_from_name(db: Session, tags: schemas.CrearHabitos):
    lista_tags = set()  # Utilizamos un conjunto para evitar IDs duplicados
    
    for tag in tags.tags:
        db_tag = get_tags_from_name(db=db, name=tag)
        if db_tag:
            lista_tags.add(db_tag.id)  # Usamos add() en lugar de append() para agregar al conjunto
        else:
            db_tag = create_tag(db=db, tag=schemas.TagsBase(titulo=tag))
            lista_tags.add(db_tag.id)
    
    return list(lista_tags)  # Convertimos el conjunto de nuevo en una lista antes de retornarlo


def create_habito(db: Session, habito: schemas.CrearHabitos):
    db_habito = models.Habitos(name=habito.name,
                               descripcion=habito.descripcion,
                               aprendizaje=habito.aprendizaje,
                               dificultad=habito.dificultad
                               )
    db.add(db_habito)
    db.commit()
    db.refresh(db_habito)
    return db_habito

def vincular_habitos_con_tags(db:Session, habito: models.Habitos, tags_ids:list ):
    for tag_id in tags_ids:
        habitos_tags = models.HabitosTags(habitos_id=habito.id,
                                          tags_id= tag_id)
        db.add(habitos_tags)
        db.commit()
        db.refresh(habitos_tags)
    return True
    
def login_user(db:Session, login:schemas.LoginUsers):
    if  login.user_name == None or login.user_name == "" or login.password == None or login.password == "":
        return schemas.ErrorMessage(message="Algunos campos estan vacios", title="Espacios vacios", code_error=422)
    else:
        user = db.query(models.User).filter(models.User.user_name == login.user_name).first()
        if login.password == user.hashed_password:
            return user
        else: 
            return schemas.ErrorMessage(message="Contraseña invalida", title="mala contraseña", code_error=422)
    
    


    # se valida la contraseña del usuario con respecto a la contraseña que nos pasaron

def create_calendario(db:Session, calendario: schemas.CreateCalendario, user:int):
    calendario_existe=db.query(models.Calendario).filter(models.Calendario.user_id == user).first()
    if calendario_existe:
        return None
    else:
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