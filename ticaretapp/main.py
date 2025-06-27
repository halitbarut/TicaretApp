from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import HTMLResponse

from . import crud, models, schemas, config, security
from .database import engine, get_db
from .routers import users, products, cart
from fastapi import FastAPI, Depends, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="TicaretApp API")

app.mount("/static", StaticFiles(directory="ticaretapp/static"), name="static")

templates = Jinja2Templates(directory="ticaretapp/templates")
app.include_router(users.router, prefix="/api")
app.include_router(products.router, prefix="/api")
app.include_router(cart.router, prefix="/api")


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "page_title": "Ana Sayfa"})

@app.get("/cart", response_class=HTMLResponse)
def cart_page(request: Request):
    return templates.TemplateResponse("cart.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/register", response_class=HTMLResponse)
def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/api/token", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = security.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}