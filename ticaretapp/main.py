from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import crud
from . import models
from . import schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
def read_root():
    return {"Proje": "TicaretApp"}

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise ValueError("Email already registered")
    return crud.create_user(db=db, user=user)

@app.post("/users/{user_id}/products/", response_model=schemas.Product)
def add_product(product: schemas.ProductCreate, user_id : int, db: Session = Depends(get_db)):
    return crud.create_user_product(db=db, product=product, user_id=user_id)

@app.get("/products/", response_model=list[schemas.Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_products(db, skip=skip, limit=limit)

@app.delete("/products/{product_id}", response_model=dict)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return crud.delete_product(db=db, product_id=product_id)

@app.put("/products/{product_id}", response_model=schemas.Product)
def update_product(product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.update_product(db=db, product_id=product_id, product=product)