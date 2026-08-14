from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from sqlalchemy import text

from database import SessionLocal, Base, engine

from schemas import UserResponse
from routers import users, raids, mocks, boss, ranking, attempts, images
import routers.nikkes as nikkes
import models

Base.metadata.create_all(bind=engine)

def seed_nikkes():
    with SessionLocal() as session:
        count = session.execute(
            text("SELECT COUNT(*) FROM nikkes")
        ).scalar()

        if count > 0:
            return

        with open("db/init/nikkes_seed.sql", "r", encoding="utf-8") as f:
            sql = f.read()

        session.execute(text(sql))
        session.commit()


seed_nikkes()

app = FastAPI()

app.include_router(users.router)
app.include_router(raids.router)
app.include_router(mocks.router)
app.include_router(boss.router)
app.include_router(ranking.router)
app.include_router(nikkes.router)
app.include_router(attempts.router)
app.include_router(images.router)

app.mount(
    "/images",
    StaticFiles(directory="images"),
    name="images"
)

@app.get("/")
def root():
    return {"status": "Backend is running"}

