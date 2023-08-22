from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from .. import crud, models, schemas
from ..database import engine, get_db

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
  prefix="/players",
  tags=["players"],
  responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[schemas.Player])
def read_players(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    players = crud.get_players(db, skip=skip, limit=limit)
    return players
