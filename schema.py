from typing import List, Optional
from pydantic import BaseModel, validator, Field

class TitanicSchema(BaseModel):
    PassengerId: int
    Survived: bool
    Pclass: int
    Name: str
    Sex: str
    Age: Optional[float] # to allow for nullable float values
    SibSp: float
    Parch: float
    Ticket: str
    Fare: float
    Cabin: str
    Embarked: str

    @validator('Age', pre=True)  # Add a validator to handle null values
    def validate_age(cls, value):
        if value is None or value == "":
            return None
        return value