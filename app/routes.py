
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import JobCreate, Job, InterviewCreate, Interview
from app.models import Job as JobModel, Interview as InterviewModel
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/jobs/", response_model=Job)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    db_job = JobModel(**job.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

@router.get("/jobs/", response_model=list[Job])
def read_jobs(db: Session = Depends(get_db)):
    return db.query(JobModel).all()

@router.post("/interviews/", response_model=Interview)
def create_interview(interview: InterviewCreate, db: Session = Depends(get_db)):
    db_interview = InterviewModel(**interview.dict())
    db.add(db_interview)
    db.commit()
    db.refresh(db_interview)
    return db_interview

@router.get("/interviews/", response_model=list[Interview])
def read_interviews(db: Session = Depends(get_db)):
    return db.query(InterviewModel).all()
