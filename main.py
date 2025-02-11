from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from crud import UserCRUD

app = FastAPI()

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = UserCRUD(db).get_all_users()
    return [{"id": u.id, "name": u.name, "email": u.email} for u in users]

@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = UserCRUD(db).get_user_by_id(user_id)
    if not user:
        return {"error": "User not found"}
    return {"id": user.id, "name": user.name, "email": user.email}

@app.post("/users")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    user = UserCRUD(db).create_user(name, email)
    return {"id": user.id, "name": user.name, "email": user.email}
