from app.infrastructure.api.routes import router
from app.infrastructure.db.models import Base
from app.infrastructure.db.session import engine
from fastapi import FastAPI

app = FastAPI(title="Orders Service")

Base.metadata.create_all(bind=engine)

app.include_router(router)
