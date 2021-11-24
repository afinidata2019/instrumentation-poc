from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.core.config import Config


settings = Config()

engine = create_engine(settings.DB_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
