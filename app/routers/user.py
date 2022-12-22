from .. import models, schemas, utils
from fastapi import FastAPI, Path, Response, status, HTTPException, Depends, APIRouter
from ..database_pg_local import get_db
from sqlalchemy.orm import Session
#per importare app non fare come nel main app = FastAPI() ma usare APIRouter in lib fastapi

router = APIRouter(prefix="/users", tags=["Users"])
#users

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.OutUser)
def create_user(user: schemas.CreateUser, db:Session = Depends(get_db)):
    #hash password
    hashed_password = utils.hash(user.password)
    user.password=hashed_password
    new_user = models.User(**user.dict())
    # istruzioni per inserire fiels
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    # pubblica la post per eventua


@router.get("/{id}", response_model=schemas.OutUser)
def get_user(id: int, db:Session = Depends(get_db)):
    user= db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} does not exist')
    return user