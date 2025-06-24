from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from ticaretapp import schemas, models, crud
from ticaretapp.database import get_db
from ticaretapp.dependencies import get_current_user

router = APIRouter(
    prefix="/cart",
    tags=["Shopping Cart"],
    dependencies=[Depends(get_current_user)]
)

@router.get("/", response_model=schemas.Cart)
def read_user_cart(db: Session = Depends(get_db), current_user : models.User = Depends(get_current_user)):
    cart = crud.get_or_create_cart(db, user_id=current_user.id)
    return cart

@router.post("/items", response_model=schemas.CartItem)
def add_product_to_cart(item : schemas.CartItemCreate, db : Session = Depends(get_db), current_user : models.User = Depends(get_current_user)):
    cart = crud.get_or_create_cart(db, user_id=current_user.id)
    db_product = crud.get_product_by_id(db, product_id=item.product_id)
    if not db_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

    return crud.add_item_to_cart(
        db=db,
        cart_id=cart.id,
        product_id=item.product_id,
        quantity=item.quantity
    )

@router.delete("/items/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_product_from_cart(product_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    cart = crud.get_or_create_cart(db, user_id=current_user.id)
    success = crud.remove_item_from_cart(db, cart.id, product_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not in the cart")
    return None