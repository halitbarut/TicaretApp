from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from . import models, schemas, security
from .schemas import UserCreate, User

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: UserCreate):
    hashed_password = security.get_password_hash(user.password)
    db_user = models.User(
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Product).offset(skip).limit(limit).all()

def get_product_by_id(db: Session, product_id: int, skip: int = 0, limit: int = 10):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if product is not None:
        return product
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")


def create_user_product(db: Session, product: schemas.ProductCreate, user_id: int):
    db_product = models.Product(
        name=product.name,
        description=product.description,
        price=product.price,
        owner_id=user_id
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if product:
        db.delete(product)
        db.commit()
        return {"message": "Product deleted successfully"}
    else:
        return {"message": "Product not found"}

def update_product(db: Session, product_id: int, product: schemas.ProductCreate):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db.commit()
        db.refresh(db_product)
        return db_product
    else:
        return {"message": "Product not found"}

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user or not security.verify_password(password, user.hashed_password):
        return False
    return user