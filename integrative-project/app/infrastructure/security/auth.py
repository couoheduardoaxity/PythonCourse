from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer

security = HTTPBearer()


def verify_token(credentials=Depends(security)):
    if credentials.credentials != "secrettoken":
        raise HTTPException(status_code=403, detail="Invalid token")
