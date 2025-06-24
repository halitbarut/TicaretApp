from typing import Optional, List

from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    name: str
    description: str
    price: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    products: list[Product] = []

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class CartItemBase(BaseModel):
    product_id : int
    quantity: int = Field(1, gt=0, description="Number of products to add to the cart")

class CartItemCreate(CartItemBase):
    pass

class CartItem(CartItemBase):
    id: int
    product: Product

class Config:
    from_attributes = True

class CartBase(BaseModel):
    pass

class Cart(CartBase):
    id: int
    owner_id: int
    items: List[CartItem] = []

    class Config:
        from_attributes = True