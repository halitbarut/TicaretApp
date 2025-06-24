from typing import Optional

from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from . import models, schemas, security
from .schemas import UserCreate, User

def get_user_by_email(db: Session, email: str) -> models.User | None:
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: UserCreate) -> models.User:
    hashed_password = security.get_password_hash(user.password)
    db_user = models.User(
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str) -> models.User | bool:
    user = get_user_by_email(db, email)
    if not user or not security.verify_password(password, user.hashed_password):
        return False
    return user


def get_products(
    db: Session,
    search: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    skip: int = 0,
    limit: int = 100
) -> list[models.Product]:
    query = db.query(models.Product)
    if search:
        search_term = f"%{search}%"
        query = query.filter(models.Product.name.ilike(search_term))

    if min_price is not None:
        query = query.filter(models.Product.price >= min_price)

    if max_price is not None:
        query = query.filter(models.Product.price <= max_price)

    products = query.offset(skip).limit(limit).all()

    return products

def get_product_by_id(db: Session, product_id: int) -> models.Product | None:
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def create_user_product(db: Session, product: schemas.ProductCreate, user_id: int) -> models.Product:
    db_product = models.Product(**product.model_dump(), owner_id=user_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, db_product: models.Product, product_update: schemas.ProductCreate) -> models.Product:
    update_data = product_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_product, key, value)

    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product: models.Product) -> None:
    db.delete(product)
    db.commit()