from fastapi import FastAPI
from database.routers import players, users

app = FastAPI()

app.include_router(users.router)
app.include_router(players.router)

@app.get('/')
async def hello():
    return {"message": "Hello World"}