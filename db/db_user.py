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
