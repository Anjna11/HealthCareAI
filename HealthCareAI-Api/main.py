from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Integer, String, Column, DateTime
from typing import List
from sqlalchemy import select
from datetime import date, time, datetime

#SQLite: indicate SQLite database, If the file doesn't exist, SQLite will automatically create it once you use it.
DB_URL = "sqlite:///./patients.db"


engine = create_engine(DB_URL, connect_args={"check_same_thread":False}, echo=True)
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
    patient_id = Column(Integer, primary_key=True, index=True)
    fname = Column(String)
    lname = Column(String)
    gender = Column(String)
    dob = Column(String)  
    
class AppointmentSQLAlchemy(Base):
    __tablename__ = "Appointment"
    appointment_id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer)
    visitType_id = Column(Integer)
    startTime = Column(DateTime)
    endTime = Column(DateTime)

class VisitTypeSQLAlchemy(Base):
    __tablename__ = "Visit Type"
    VisitType_id = Column(Integer, primary_key=True, index=True)
    Visit_name = Column(String)
    
#create table
Base.metadata.create_all(bind=engine)

#Pydantic Model
class Patient(BaseModel):
    id:int | None = None
    fname: str
    lname:str
    gender:str
    dob:str

class MakeAppointment(BaseModel):
    patient_id: int
    visitType_id: int
    startTime: datetime 
    

# Patients = []

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
    return {"message": "Patient registered", "id": new_patient.patient_id}

@app.get("/patients")
def get_patients():
    db = Session()
    patients = db.query(PatientSQLAlchemy).all()
    db.close()
    return patients

@app.get("/activePatients")
def get_activePatients():
    db = Session()
    stmt = (
        select(
            PatientSQLAlchemy.patient_id,
            PatientSQLAlchemy.fname,
            PatientSQLAlchemy.lname,
            PatientSQLAlchemy.gender,
            PatientSQLAlchemy.dob,
            VisitTypeSQLAlchemy.Visit_name,
            AppointmentSQLAlchemy.startTime
        ).join(AppointmentSQLAlchemy, PatientSQLAlchemy.patient_id == AppointmentSQLAlchemy.patient_id
        ).join(VisitTypeSQLAlchemy, AppointmentSQLAlchemy.visitType_id == VisitTypeSQLAlchemy.VisitType_id)
    )
    results = db.execute(stmt).all()
    db.close()
    
    patients = []
    for row in results:
        # patients.append(list(row._tuple()))
        row_dict = row._asdict()
        # TODO: Cover this condition as where in above step.
        if row_dict['startTime'].date() == datetime.today().date():
            patients.append(row_dict)

    return patients

@app.post("/makeAppointment")
def makeAppointment(a: MakeAppointment):
    db = Session()
    new_appointment = AppointmentSQLAlchemy(
        patient_id = a.patient_id,
        visitType_id = a.visitType_id,
        startTime = a.startTime,
        endTime=None    
    )
    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)
    db.close()
    return {"message": "New Appointment registered", "id": new_appointment.appointment_id}
