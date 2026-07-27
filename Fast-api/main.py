from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud, schemas

from database import Base, engine, SessionLocal


Base.metadata.create_all(bind=engine)

app = FastAPI()

#database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def welcome():
    return "Welcome to Electronics Store!"

#create
@app.post("/electronics", response_model= schemas.ElectronicsResponse)
def create(
    electronics: schemas.ElectronicsCreate,
    dn: Session = Depends(get_db)
):
    return crud.create_electronics(dn, electronics)

#read all
@app.get("/electronics", response_model=list[schemas.ElectronicsResponse])
def read_all(db: Session = Depends(get_db)):
    return crud.get_all_electronics(db)

#read one
@app.get("/electronics/{electronics_id}", response_model= schemas.ElectronicsResponse)
def read_one(electronics_id: int, db: Session = Depends(get_db)):
    electronics = crud.get_electronics(db, electronics_id)
    if not electronics:
        raise HTTPException(status_code=404, detail="Electronics not found")
    return electronics

#Filter by category
@app.get("/electronics/category/{category}", response_model=list[schemas.ElectronicsResponse])
def read_by_category(category: str, db: Session = Depends(get_db)):
    electronics = crud.get_by_category(db, category)
    if not electronics:
        raise HTTPException(status_code=404, detail="Electronics not found in this category")
    return electronics

#update
@app.put("/electronics/{electronics_id}", response_model=schemas.ElectronicsResponse)
def update(
    electronics_id: int,
    electronics: schemas.ElectronicsCreate,
    db: Session = Depends(get_db)
):
    updated = crud.update_electronics(db, electronics_id, electronics)
    if not updated:
        raise HTTPException(status_code=404, detail="Electronics not found")
    return updated

#delete
@app.delete("/electronics/{electronics_id}")
def delete(
    electronics_id: int,
    db: Session = Depends(get_db)
):
    deleted = crud.delete_electronics(db, electronics_id )
    if not deleted :
        raise HTTPException(status_code=404, detail="Electronics not found")
    return {"message": "Electronics deleted successfully"}



