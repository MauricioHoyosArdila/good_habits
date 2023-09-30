from fastapi import Depends, APIRouter, HTTPException
from typing import Union
from sqlalchemy.orm import Session

from .. import crud, schemas
from database.database import engine, get_db
from database import models

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
  prefix="/calendarios",
  tags=["calendarios"],
  responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=Union[schemas.Calendario, schemas.ErrorMessage])
def create_calendario(calendario: schemas.CreateCalendario, db: Session = Depends(get_db)):
    print(calendario)
    db_user = crud.get_user_by_email(db, email=calendario.user_email)
    print(db_user)
    if db_user:
        calendario = crud.create_calendario(db=db,calendario=calendario,user=db_user.id)
        if calendario:
          return schemas.Calendario( nombre=calendario.nombre, id= calendario.id)
        else:
            return schemas.ErrorMessage(message="El calendario ya existe", title="el calendario ya existe", code_error=422 )
    else:
        return schemas.ErrorMessage(message="el usuario no existe", title="el usuario no existe", code_error=422)
    