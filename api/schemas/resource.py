from datetime import datetime

from pydantic import BaseModel


class Resource(BaseModel):
    id: int
    name: str
    created_at: datetime

    class Config:
        orm_mode = True
