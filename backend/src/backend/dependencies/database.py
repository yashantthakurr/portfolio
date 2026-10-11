
from backend.auth.security import hash_password
from backend.constants.config import secrets
from backend.database.session import engine, SessionLocal
from backend import models
from collections.abc import Generator
from sqlalchemy import text
from sqlalchemy.orm import Session

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db() -> None:
    db = SessionLocal()
    if not db.query(models.User).filter(models.User.username==secrets.ADMIN_USERNAME).first():
        db.add(models.User(username=secrets.ADMIN_USERNAME, hashed_password=hash_password(secrets.ADMIN_PASSWORD)))
        db.commit()
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
    except Exception as e:
        print(f"AN error occurred while connecting to the Database: {e}")
