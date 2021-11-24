from typing import List

from fastapi import APIRouter, Depends
import requests
from sqlalchemy.orm import Session

from api import models, schemas
from api.db.session import get_db


router = APIRouter()


@router.get("/", response_model=List[schemas.Resource])
async def get_resources(db: Session = Depends(get_db)):
    try:
        request = requests.get("https://fjhlfkjkj.com")
    except requests.ConnectionError:
        pass

    return db.query(models.Resource).all()
