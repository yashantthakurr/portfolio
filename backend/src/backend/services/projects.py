
from backend.exceptions.projects import PROJECT_WITH_TITLE_ALREADY_EXISTS_EXCEPTION, CANNOT_FIND_PROJECT_BY_ID_EXCEPTION
from backend.models.projects import Project
from backend.schemas.projects import ProjectCreate, ProjectUpdate
from sqlalchemy.orm import Session
from typing import List

def add_project(db: Session, data: ProjectCreate) -> Project:
    if db.query(Project).filter(Project.title==data.title).first():
        raise PROJECT_WITH_TITLE_ALREADY_EXISTS_EXCEPTION
    project = Project(**data.model_dump())
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

def fetch_all_projects(db: Session) -> List[Project]:
    return db.query(Project).all()

def update_experience(db: Session, id: int, data: ProjectUpdate) -> Project:
    project = db.query(Project).filter(Project.id == id).first()
    if not project:
        raise CANNOT_FIND_PROJECT_BY_ID_EXCEPTION
    if data.title is not None:
        if db.query(Project).filter(Project.title == data.title, Project.id!=project.id).first():
            raise PROJECT_WITH_TITLE_ALREADY_EXISTS_EXCEPTION
        project.title=data.title
    if data.description is not None:
        project.description=data.description
    if data.technologies is not None:
        project.technologies=data.technologies
    if data.github is not None:
        project.github=data.github
    if data.live_demo is not None:
        project.live_demo=data.live_demo
    db.commit()
    db.refresh(project)
    return project

def delete_project(db: Session, id: int) -> None:
    exp = db.query(Project).filter(Project.id==id).first()
    if not exp:
        raise CANNOT_FIND_PROJECT_BY_ID_EXCEPTION
    db.delete(exp)
    db.commit()
