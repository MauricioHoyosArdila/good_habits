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
def create_habitos(habitos: schemas.HabitosBase, db: Session = Depends(get_db)):
    db_habitos = crud.get_all_tags_by_habitos(db, habitos=habitos.tags)
def create_tags(tags: schemas.HabitosBase, db: Session = Depends(get_db)) :

