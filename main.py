from typing import List
from uuid import UUID
from fastapi import FastAPI
from fastapi import HTTPException, status
from models import User, Gender, Role
app = FastAPI()

db: List[User] = [
    User(
        first_name="Mo",
        last_name="Salah",
        gender=Gender.male,
        roles=[Role.admin, ]
    ),
    User(
        first_name="Sadio",
        last_name="Mane",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]


@app.get("/")
async def root():
    return {"message": "Learning FastAPI"}


@app.get("/api/v1/users")
async def get_users():
    """ Returns all the user information available in the DB 
    """
    return db


@app.post("/api/v1/users")
async def create_user(user: User):
    """ Creates a new user in the DB and returns the user info

    Parameters:
    -----------
    user: User

        A User model instance
    """
    db.append(user)
    return {
        "message": "new user added",
        "user": user
    }


@app.delete("/api/v1/users/{user_id}/remove")
async def remove_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"message": f"User {user_id} is deleted from the record"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"user id: {user_id} does not exists"
                        )
