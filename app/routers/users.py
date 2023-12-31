from fastapi import Depends, APIRouter, HTTPException
from typing import Union
from sqlalchemy.orm import Session

from .. import crud, schemas
from database.database import engine, get_db
from database import models

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
  prefix="/users",
  tags=["users"],
  responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=Union[schemas.User, schemas.ErrorMessage])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@router.get("/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post("/login", response_model=Union[schemas.User, schemas.ErrorMessage])
def login_user(login:schemas.LoginUsers, db: Session = Depends(get_db)):
    users = crud.login_user(db, login=login)
    return users
# @router.post("/{user_id}/players/", response_model=schemas.Player)
# def create_item_for_user(
#     user_id: int, player: schemas.PlayerCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_player(db=db, player=player, user_id=user_id)
