from tables import DBPlace
from sqlalchemy.orm import Session
from schema import Place

def create_place(db: Session, place: Place):
    # db_place =DBPlace(name=place.name,description=place.description)
    db_place =DBPlace(**place.dict())
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return db_place

def get_places(db: Session):
    return db.query(DBPlace).all()

def get_place(db: Session, place_id: int):
    return db.query(DBPlace).where(DBPlace.id == place_id).first()

def delete_place(db: Session, place_id: int):
    db.delete(db.query(DBPlace).where(DBPlace.id == place_id).first())
    db.commit()
    return "delete successfully"

def update_place(db: Session, place_id: int,place: Place ):
    data=db.query(DBPlace).where(DBPlace.id == place_id).first()
    data.name=place.name
    data.description=place.description
    db.add(data)
    db.commit()
    db.refresh(data)
    return "Update Successfully"