import csv
import os

from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker


engine = create_engine("postgresql://postgres:YdYwT5rLvC0etfEDp3gU@containers-us-west-22.railway.app:6776/railway")
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("flights.csv")
    reader = csv.reader(f)
    for origin, destination, duration in reader:
        query = text("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)")
        db.execute(query,{"origin": origin, "destination": destination, "duration": duration})
        print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
    db.commit()

if __name__ == "__main__":
    main()