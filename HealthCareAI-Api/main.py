from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Integer, String, Column
from typing import List

#SQLite: indicate SQLite database, If the file doesn't exist, SQLite will automatically create it once you use it.
DB_URL = "sqlite:///./patients.db"


engine = create_engine(DB_URL, connect_args={"check_same_thread":False})
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use specific origin in production
    allow_methods=["*"],
    allow_headers=["*"],
)

# SQLAlchemy model
class PatientSQLAlchemy(Base):
    __tablename__ = "Patients"
    id = Column(Integer, primary_key=True, index=True)
    fname = Column(String)
    lname = Column(String)
    gender = Column(String)
    dob = Column(String)  
    
#create table
Base.metadata.create_all(bind=engine)

#Pydantic Model
class Patient(BaseModel):
    id:int | None = None
    fname: str
    lname:str
    gender:str
    dob:str

Patients = []

@app.post("/register")
def register(p: Patient):
    db = Session()
    new_patient = PatientSQLAlchemy(
        fname=p.fname,
        lname=p.lname,
        gender=p.gender,
        dob=p.dob
    )
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    db.close()
    return {"message": "Patient registered", "id": new_patient.id}

@app.get("/patients")
def get_patients():
    db = Session()
    patients = db.query(PatientSQLAlchemy).all()
    db.close()
    return patients

