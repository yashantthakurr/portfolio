
from backend.exceptions.certificates import CERTIFICATE_WITH_NAME_ALREADY_EXISTS_EXCEPTION, CANNOT_FIND_CERTIFICATE_BY_ID_EXCEPTION
from backend.models.certifications import Certificate
from backend.schemas.certificate import CertificateCreate, CertificateUpdate
from sqlalchemy.orm import Session
from typing import List

def add_certificate(db: Session, data: CertificateCreate) -> Certificate:
    if db.query(Certificate).filter(Certificate.name==data.name).first():
        raise CERTIFICATE_WITH_NAME_ALREADY_EXISTS_EXCEPTION
    project = Certificate(**data.model_dump())
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

def fetch_all_certificates(db: Session) -> List[Certificate]:
    return db.query(Certificate).all()

def update_certificate(db: Session, id: int, data: CertificateUpdate) -> Certificate:
    certificate = db.query(Certificate).filter(Certificate.id == id).first()
    if not certificate:
        raise CANNOT_FIND_CERTIFICATE_BY_ID_EXCEPTION
    if data.name is not None:
        if db.query(Certificate).filter(Certificate.name == data.name, Certificate.id!=certificate.id).first():
            raise CERTIFICATE_WITH_NAME_ALREADY_EXISTS_EXCEPTION
        certificate.name=data.name
    if data.issued_by is not None:
        certificate.issued_by=data.issued_by
    if data.issued_year is not None:
        certificate.issued_year=data.issued_year
    if data.skills is not None:
        certificate.skills=data.skills
    if data.certificate_link is not None:
        certificate.certificate_link=data.certificate_link
    db.commit()
    db.refresh(certificate)
    return certificate

def delete_certificate(db: Session, id: int) -> None:
    certificate = db.query(Certificate).filter(Certificate.id==id).first()
    if not certificate:
        raise CANNOT_FIND_CERTIFICATE_BY_ID_EXCEPTION
    db.delete(certificate)
    db.commit()
