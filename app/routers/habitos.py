from fastapi import Depends, APIRouter, HTTPException
from typing import Union
from sqlalchemy.orm import Session

from .. import crud, schemas
from database.database import engine, get_db
from database import models

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
  prefix="/habitos",
  tags=["habitos"],
  responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=Union[schemas.HabitosBase, schemas.ErrorMessage])
def create_habitos(habitos: schemas.CrearHabitos, db: Session = Depends(get_db)):
    tags_ids = crud.get_tags_ids_from_name(db, tags=habitos)
    habito=crud.create_habito(db, habito=habitos)
    crud.vincular_habitos_con_tags(db, habito=habito, tags_ids=tags_ids)
    return schemas.HabitosBase(name=habito.name, descripcion= habito.descripcion, aprendizaje=habito.aprendizaje, dificultad=habito.dificultad, id=habito.id)

@router.get("/", response_model=list[schemas.Lista_Habitos])
def lista_habitos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    lista_habitos = crud.get_lista_habitos(db, skip=skip, limit=limit)
    habitos = []
    for habito in lista_habitos:
      habitos.append(schemas.Lista_Habitos(name=habito.name, descripcion=habito.descripcion, aprendizaje=habito.aprendizaje, dificultad=habito.dificultad, id=habito.id))
    return habitos
