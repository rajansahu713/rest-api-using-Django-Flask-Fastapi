from fastapi import FastAPI, Depends
#from fastapi.response import JSONRespose
from schema import Place
from tables import DBPlace
from crud import create_place, update_place, get_place, delete_place, get_places
from database import Base, engine, SessionLocal
# from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Insert the data into database table    
@app.post('/places')
async def create_places_view(place: Place, db: Session = Depends(get_db)):
    db_place = create_place(db, place)
    return db_place

# get all the list of user
@app.get('/places/')
async def get_places_view(db: Session = Depends(get_db)):
    return get_places(db)

# Get the particular value from database
@app.get('/place/{place_id}')
async def get_place_view(place_id: int, db: Session = Depends(get_db)):
    return get_place(db, place_id)


# delete particular object from table
@app.delete('/place/{place_id}')
async def delete_place_view(place_id: int, db: Session = Depends(get_db)):
    return delete_place(db, place_id)

# update particular object 
@app.put('/place/{place_id}')
async def update_place_view(place_id:int,place: Place, db: Session = Depends(get_db)):
    return update_place(db,place_id, place)
