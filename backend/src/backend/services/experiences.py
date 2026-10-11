
from backend.exceptions.experiences import CANNOT_FIND_EXPERIENCE_BY_ID_EXCEPTION
from backend.models.experiences import Experience
from backend.schemas.experiences import CreateExperience, UpdateExperience
from sqlalchemy.orm import Session
from typing import List

def add_experience(db: Session, data: CreateExperience) -> Experience:
    experience = Experience(**data.model_dump())
    db.add(experience)
    db.commit()
    db.refresh(experience)
    return experience

def fetch_all_experiences(db: Session) -> List[Experience]:
    return db.query(Experience).all()

def update_experience(db: Session, id: int, data: UpdateExperience) -> Experience:
    exp = db.query(Experience).filter(Experience.id == id).first()
    if not exp:
        raise CANNOT_FIND_EXPERIENCE_BY_ID_EXCEPTION
    if data.organization is not None:
        exp.organization=data.organization
    if data.role is not None:
        exp.role=data.role
    if data.timeline is not None:
        exp.timeline=data.timeline
    if data.description is not None:
        exp.description=data.description
    if data.mode is not None:
        exp.mode=data.mode
    db.commit()
    db.refresh(exp)
    return exp

def delete_experience(db: Session, id: int) -> None:
    exp = db.query(Experience).filter(Experience.id==id).first()
    if not exp:
        raise CANNOT_FIND_EXPERIENCE_BY_ID_EXCEPTION
    db.delete(exp)
    db.commit()
