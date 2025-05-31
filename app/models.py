
from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    company = Column(String, index=True)
    position = Column(String)
    application_date = Column(Date)
    status = Column(String, default="applied")
    interviews = relationship("Interview", back_populates="job")

class Interview(Base):
    __tablename__ = "interviews"
    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey("jobs.id"))
    date = Column(Date)
    stage = Column(String)
    feedback = Column(Text)
    result = Column(String)
    job = relationship("Job", back_populates="interviews")
