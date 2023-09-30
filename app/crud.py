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

def get_lista_habitos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Habitos).offset(skip).limit(limit).all()

def create_tareas(db: Session, tareas: schemas.Tareas):
    db_tareas = models.Tareas(name=tareas.name,
                              descripcion=tareas.descripcion,
                              regularidad=tareas.regularidad,
                              dias=tareas.dias,
                              dificultad=tareas.dificultad)
    db.add(db_tareas)
    db.commit()
    db.refresh(db_tareas)
    return db_tareas




# def get_players(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Player).offset(skip).limit(limit).all()


# def create_user_player(db: Session, player: schemas.PlayerCreate, user_id: int):
#     db_player = models.Player(**player.dict(), manager_id=user_id)
#     db.add(db_player)
#     db.commit()
#     db.refresh(db_player)
#     return db_player