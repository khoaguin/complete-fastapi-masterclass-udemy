from sqlalchemy.orm.session import Session

from db.hash import Hash
from db.models import DBUser
from schemas import UserBase


def create_user(db: Session, requests: UserBase):
    new_user = DBUser(
        username=requests.username,
        email=requests.email,
        password=Hash.bcrypt(requests.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # to get the id (automatically generated) for the new user
    return new_user


def get_all_users(db: Session):
    return db.query(DBUser).all()


def get_user(db: Session, id: int):
    return db.query(DBUser).filter(DBUser.id == id).first()


def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DBUser).filter(DBUser.id == id)
    user.update(
        {
            DBUser.username: request.username,
            DBUser.email: request.email,
            DBUser.password: Hash.bcrypt(request.password),
        }
    )
    db.commit()
    return "user updated"


def delete_user(db: Session, id: int):
    user = db.query(DBUser).filter(DBUser.id == id).first()
    db.delete(user)
    db.commit()
    return "user deleted"
