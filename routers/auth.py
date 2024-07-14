from fastapi import FastAPI, status, APIRouter
from fastapi.exceptions import HTTPException
import schemas
from models import User
from database import session, engine

router = APIRouter(
    prefix='/auth'
)
session = session(bind=engine)


@router.post('/blog')
async def create_blog(user: schemas.CreateBlog):
    db_user = session.query(User).filter(User.username == user.username).first()
    if db_user is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")
    new_user = User(username=user.username, title=user.title, text=user.text)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user


@router.delete('/delete', status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog(user: schemas.DeleteBlog):
    db_user = session.query(User).filter(User.username == user.username).first()
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    session.query(User).delete(synchronize_session="auto")

    return {'message': 'User is deleted'}


@router.post('/update', status_code=status.HTTP_200_OK)
async def update_blog(user: schemas.UpdateBlog):
    db_user = session.query(User).filter(User.username == user.username).first()
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    new_user = User(username=user.username, title=user.title, text=user.text)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user
