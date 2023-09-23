import uvicorn
from fastapi import FastAPI
from .routers import users, habitos

app = FastAPI()

app.include_router(users.router)
app.include_router(habitos.router)
# app.include_router(players.router)


@app.get('/')
async def hello():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
