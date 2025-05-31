
from pydantic import BaseModel
from datetime import date
from typing import Optional

class JobCreate(BaseModel):
    company: str
    position: str
    application_date: date
    status: Optional[str] = "applied"

class Job(BaseModel):
    id: int
    company: str
    position: str
    application_date: date
    status: str

    class Config:
        orm_mode = True

class InterviewCreate(BaseModel):
    job_id: int
    date: date
    stage: str
    feedback: Optional[str] = None
    result: Optional[str] = None

class Interview(BaseModel):
    id: int
    job_id: int
    date: date
    stage: str
    feedback: Optional[str]
    result: Optional[str]

    class Config:
        orm_mode = True
