from sqlalchemy.orm import Session
import models
import schemas

#Create
def create_electronics(db: Session, electronics: schemas.ElectronicsCreate):
    db_electronics = models.Electronics(**electronics.model_dump())
    db.add(db_electronics)
    db.commit()
    db.refresh(db_electronics)
    return db_electronics

#read
#Read all
def get_all_electronics(db: Session):
    return db.query(models.Electronics).all()

#read one
def get_electronics(db: Session, electronics_id: int):

    return db.query(models.Electronics).filter(models.Electronics.id == electronics_id).first()

# read by category
def get_by_category(db: Session, category: str):
    return db.query(models.Electronics).filter( models.Electronics.category == category).all()

#update
def update_electronics(db: Session, electronics_id: int, electronics: schemas.ElectronicsCreate):
    db_electronics = get_electronics(db, electronics_id)

    if not db_electronics:
        return None

    db_electronics.name = electronics.name
    db_electronics.category = electronics.category
    db_electronics.brand = electronics.brand
    db_electronics.price = electronics.price
    db_electronics.stock = electronics.stock

    db.commit()
    db.refresh(db_electronics)
    return db_electronics

#delete
def delete_electrnoics(db: Session, electrnoics_id:int):
    db_electronics = get_electronics(db, electrnoics_id)
    if not db_electronics:
        return None
    db.delete(db_electronics)
    db.commit()
    return db_electronics
