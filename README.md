# Doctors & Patients REST API

A simple REST API built with **Python, FastAPI, Pydantic, and Uvicorn** to manage doctors and patients.

## Features

### Doctor APIs

- `POST /doctors` - Create a doctor
- `GET /doctors` - List all doctors
- `GET /doctors/{doctor_id}` - Get a doctor by ID

Doctor fields:

- `name`
- `specialization`
- `email`
- `is_active` (defaults to `true`)

### Patient APIs

- `POST /patients` - Create a patient
- `GET /patients` - List all patients

Patient fields:

- `name`
- `age`
- `phone`

## Validation

- Doctor email must be valid.
- Patient age must be greater than 0.
- Pydantic models are used for request/response validation.
- HTTPException is used for application-level errors such as missing doctors and duplicate doctor emails.

## Project Structure

```text
fastapi_doctors_patients/
├── main.py
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.9+
- pip

## Setup

### 1. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the API

```bash
uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically provides Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

## Example Requests

### Create Doctor

`POST /doctors`

```json
{
  "name": "Dr. John Smith",
  "specialization": "Cardiology",
  "email": "john.smith@example.com",
  "is_active": true
}
```

### Create Patient

`POST /patients`

```json
{
  "name": "Rahul Kumar",
  "age": 30,
  "phone": "9876543210"
}
```

## Notes

This project uses in-memory dictionaries as requested. Data will be cleared whenever the application restarts.

For a production application, the storage layer can be replaced with SQLite/PostgreSQL and authentication can be added.
