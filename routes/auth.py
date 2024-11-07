from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials


route = APIRouter()

security = HTTPBasic()

@route.get("/users/me")
def read_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    return {"username": credentials.username, "password": credentials.password}

