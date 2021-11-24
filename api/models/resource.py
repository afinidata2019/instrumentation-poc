from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from api.db.base import Base


class Resource(Base):
    __tablename__ = "resource"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
