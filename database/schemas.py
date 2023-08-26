# from typing import Union

from pydantic import BaseModel


# class PlayerBase(BaseModel):
#     full_name: str
#     play_position: Union[str, None] = None


# class PlayerCreate(PlayerBase):
#     pass


# class Player(PlayerBase):
#     id: int
#     manager_id: int

#     class Config:
#         orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    # players: list[Player] = []

    class Config:
        orm_mode = True