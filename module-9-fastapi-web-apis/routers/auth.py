from app.core.security import create_token
from fastapi import APIRouter

router = APIRouter()


@router.post("/login")
def login():
    token = create_token({"sub": "admin"})
    return {"access_token": token, "token_type": "bearer"}
