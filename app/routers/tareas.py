from fastapi import Depends, APIRouter, HTTPException
from typing import Union
from sqlalchemy.orm import Session

from .. import crud, schemas
from database.database import engine, get_db
from database import models

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
  prefix="/tareas",
  tags=["tareas"],
  responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Tareas)
def create_tareas(tarea:schemas.Tareas,  db: Session = Depends(get_db)):
    tareas= crud.create_tareas(db, tarea)
    return schemas.Tareas(name=tareas.name,descripcion=tareas.descripcion,regularidad=tareas.descripcion,dias=tareas.dias,dificultad=tareas.dificultad,id=tareas.id)