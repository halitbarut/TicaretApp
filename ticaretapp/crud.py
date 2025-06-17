from sqlalchemy.orm import Session
from . import models, schemas, security
from .schemas import UserCreate, User
from passlib import context as passlib_context

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