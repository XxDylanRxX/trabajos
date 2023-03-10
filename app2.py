import os

from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker



engine = create_engine("postgresql://postgres:YdYwT5rLvC0etfEDp3gU@containers-us-west-22.railway.app:6776/railway")
db = scoped_session(sessionmaker(bind=engine))

def main():
    query = text("SELECT origin, destination, duration FROM flights")
    flights = db.execute(query).fetchall()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

if __name__ == "__main__":
    main()