from fastapi import FastAPI,HTTPException

app = FastAPI() 

@app.get('/')  
def root_url():
    return {'mes':'welcome to Api'}
@app.get('/sub')
def internal_url():
    return {"message":"welcome to fastapi internal"}


users = {
    1:{'name':'anil'},
    2:{'name':'phani'}
}

@app.get('/user/{user_id}')
def get_user(user_id:int):
    if user_id not in users: 
        raise HTTPException(status_code=404,detail="user_id not found")
    return users[user_id]
    