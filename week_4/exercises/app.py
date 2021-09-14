from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

class User(BaseModel):
    user_id: str
    name: str


app = FastAPI()

users = {'123456789': 'Alex', '789123456': 'Isabella', '321456978': 'Filip'}

@app.get('/')
def home():

    return {'text': 'Hello World!'} 

@app.get('/users')
def get_users():

    return users


@app.post('/users')
def create_user(user: User):
    users[user.user_id] = user.name
    return

@app.put('/users')
def update_user(user: User):
    if user.user_id in users.keys():
        users[user.user_id] = user.name
    return

@app.delete('/users')
def delete_user(user_id):
    users.pop(user_id, None)
    return


if __name__ == '__main__':
    uvicorn.run(app, port=8080)