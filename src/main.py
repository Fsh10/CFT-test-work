from uuid import uuid4

from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse

from sqlalchemy.orm import Session

from src.salary_app.schemas import UserOut, UserAuth, TokenSchema, SystemUser
from src.salary_app.utils import get_hashed_password, create_access_token, verify_password
from src.salary_app.deps import get_current_user

from src.salary_app.models import User
from src.salary_app.utils import get_user_db
from src.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/', response_class=RedirectResponse, include_in_schema=False)
async def docs():
    return RedirectResponse(url='/docs')


@app.post('/sign_up', summary="Create new user", status_code=201, response_model=UserOut)
async def create_user(data: UserAuth, db: Session = Depends(get_user_db)):
    user = db.query(User).filter(User.username == data.username).first()
    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this login already exists"
        )
    user = User(
        id=str(uuid4())
        , username=data.username
        , password=get_hashed_password(data.password)
        , salary=data.salary
        , promotion_date=data.promotion_date

    )
    db.add(user)
    db.commit()
    return UserOut(**{'salary': data.salary, 'promotion_date': data.promotion_date})


@app.post('/sign_in', summary="Create access token for user", response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_user_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    password = user.password
    if not verify_password(form_data.password, password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    return {
        "access_token": create_access_token(user.username)
    }


@app.get('/salary_promotion_info', summary='Get info about user', response_model=UserOut)
async def get_me(user: SystemUser = Depends(get_current_user)):
    return user

