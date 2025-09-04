from fastapi import FastAPI 
from pydantic import BaseModel 


app = FastAPI() 

user_details = {} 
count_id = 1

class User(BaseModel):
    name:str
    phone:int
    email:str 

@app.post('/create')
def create_user(user:User):
    global count_id 
    user_details[count_id] = user
    response = {
        "message":"user created ",
        "user_id":count_id,
        "user":user_details[count_id]
    }
    count_id += 1 
    return response

@app.get('/users')
def get_users():
    return user_details