# models.py

# Read titanic.csv and check data info
import pandas as pd

def load_titanic_csv(file_path):
    df = pd.read_csv(file_path)
    return df

titanic_df = load_titanic_csv("C:/Users/ruoni/Desktop/WB FILES/ETC2/Confidential Req21560 – Extended Term Consultant – Data Developer – Practical Test/titanic.csv")

print(titanic_df.head())

print(titanic_df.info())

# Build App
import csv
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from schema import TitanicSchema
from models import Titanic

app = FastAPI()

# Add CORS Middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency to get a database session
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# Exception handling for validation errors
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(content={"detail": exc.errors()}, status_code=400)


@app.post("/titanic", response_model=TitanicSchema)
async def create_titanic_data(titanic_data: TitanicSchema, db: Session = Depends(get_db)):
    # Create a new Titanic record in the database
    titanic = Titanic(**titanic_data.dict())
    db.add(titanic)
    db.commit()
    db.refresh(titanic)
    return titanic


@app.get("/titanic", response_model=list[TitanicSchema])
async def get_titanic_data():
    # Read data from local CSV file and return as list of TitanicSchema objects
    titanic_data = []
    with open("titanic.csv", "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            titanic_data.append(TitanicSchema(**row))
    return titanic_data







