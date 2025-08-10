from fastapi import FastAPI
# from ngrok_asgi import NgrokASGI
from pydantic import BaseModel

app = FastAPI()
# app = NgrokASGI(app)
user_db = {
    1: {
        "name": "John Doe",
        "age": 30,
            } ,
    2: {
        "name": "Jane Smith",
        "age": 25
    },   
    3: {
        "name": "Alice Johnson",
        "age": 28,
    },
}

class User(BaseModel):
    name: str
    age: int

@app.put("/user_db/data/v1/update/{user_id}")
def user_update(user_id: int, user_data: User):
    if user_id in user_db:
        user_db[user_id] = user_data.dict()
        print(user_db)
        return {"message": "User updated successfully", "user": user_db[user_id]}
    else:
        return {"error": "User not found"}

@app.delete("/user_db/data/v1/delete/{user_id}")
def delete_user(user_id: int):
    if user_id in user_db:
        del user_db[user_id]
        print(user_db)
        return {"message": "User deleted successfully", "user_id": user_id}
    else:
        return {"error": f"user {user_id} not found"}
@app.get("/")
def add(a: int, b: int):
    print("total sum is :", a + b)
    return a + b

