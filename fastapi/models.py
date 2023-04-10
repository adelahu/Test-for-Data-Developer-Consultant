# Define the database model
# Define the schema for the Titanic dataset using SQLAlchemy ORM
from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Titanic(Base):
    __tablename__ = "titanic"
    PassengerId = Column(Integer, primary_key=True)
    Survived = Column(Boolean)
    Pclass = Column(Integer)
    Name = Column(String)
    Sex = Column(String)
    Age = Column(Float)
    SibSp = Column(Float)
    Parch = Column(Float)
    Ticket = Column(String)
    Fare = Column(Float)
    Cabin = Column(String)
    Embarked = Column(String)
