from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field
from typing import List

app = FastAPI(
    title="Doctors & Patients REST API",
    description="Simple FastAPI REST API for managing doctors and patients.",
    version="1.0.0",
)

# In-memory storage
doctors = {}
patients = {}

doctor_id_counter = 1
patient_id_counter = 1


class DoctorCreate(BaseModel):
    name: str = Field(..., min_length=1)
    specialization: str = Field(..., min_length=1)
    email: EmailStr
    is_active: bool = True


class Doctor(DoctorCreate):
    id: int


class PatientCreate(BaseModel):
    name: str = Field(..., min_length=1)
    age: int = Field(..., gt=0)
    phone: str = Field(..., min_length=1)


class Patient(PatientCreate):
    id: int


@app.get("/")
def root():
    return {"message": "Doctors & Patients API is running"}


@app.post("/doctors", response_model=Doctor, status_code=201)
def create_doctor(doctor: DoctorCreate):
    global doctor_id_counter

    # Prevent duplicate doctor email addresses
    if any(existing.email == doctor.email for existing in doctors.values()):
        raise HTTPException(
            status_code=400,
            detail="A doctor with this email already exists",
        )

    new_doctor = Doctor(id=doctor_id_counter, **doctor.model_dump())
    doctors[doctor_id_counter] = new_doctor
    doctor_id_counter += 1

    return new_doctor


@app.get("/doctors", response_model=List[Doctor])
def list_doctors():
    return list(doctors.values())


@app.get("/doctors/{doctor_id}", response_model=Doctor)
def get_doctor(doctor_id: int):
    doctor = doctors.get(doctor_id)

    if doctor is None:
        raise HTTPException(
            status_code=404,
            detail="Doctor not found",
        )

    return doctor


@app.post("/patients", response_model=Patient, status_code=201)
def create_patient(patient: PatientCreate):
    global patient_id_counter

    new_patient = Patient(id=patient_id_counter, **patient.model_dump())
    patients[patient_id_counter] = new_patient
    patient_id_counter += 1

    return new_patient


@app.get("/patients", response_model=List[Patient])
def list_patients():
    return list(patients.values())
