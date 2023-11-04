from fastapi import Depends, APIRouter, HTTPException
from typing import Union
from sqlalchemy.orm import Session

from .. import crud, schemas
from database.database import engine, get_db
from database import models

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
  prefix="/eventos",
  tags=["eventos"],
  responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=Union[schemas.Eventos, schemas.ErrorMessage])
def crear_evento (evento: schemas.Eventos, db: Session = Depends(get_db)):
    db_eventos = crud.crear_eventos_calendario(db, evento=evento)
    print(db_eventos)
    print (type(db_eventos))
    if db_eventos and type(db_eventos)==models.Eventos: 
        return schemas.Eventos(nombre_evento=db_eventos.nombre_evento,id=db_eventos.id, descripcion_evento=db_eventos.id, fecha_hora=db_eventos.fecha_hora, id_habito=db_eventos.id_habito, id_calendario=db_eventos.id_calendario)
    elif type(db_eventos) == schemas.ErrorMessage:
        return db_eventos 
    else:
        return schemas.ErrorMessage(message="el usuario no existe", title="el usuario no existe", code_error=422)