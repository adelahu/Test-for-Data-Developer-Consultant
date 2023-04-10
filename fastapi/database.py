#database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./titanic.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# import csv
# from sqlalchemy.orm import Session
# from models import Titanic
# #from database import engine, Base
#
# def load_titanic_data():
#     with open('titanic.csv', 'r') as f:
#         reader = csv.reader(f)
#         next(reader)  # Skip header row
#         for row in reader:
#             passenger = Titanic(
#                 PassengerId=row[0],
#                 Survived=row[1],
#                 Pclass=row[2],
#                 Name=row[3],
#                 Sex=row[4],
#                 Age=row[5],
#                 SibSp=row[6],
#                 Parch=row[7],
#                 Ticket=row[8],
#                 Fare=row[9],
#                 Cabin=row[10],
#                 Embarked=row[11]
#             )
#             db.add(passenger)
#         db.commit()
#
# if __name__ == "__main__":
#     Base.metadata.create_all(bind=engine)
#     db = Session(bind=engine)
#     load_titanic_data()
