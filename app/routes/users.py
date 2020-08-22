from . import app
from app.services.users import UsersService 
from Flask import request  


@app.routes("/users", methods=['POST'])
def user():
    request_data = request.json
    users = UsersService()
    return users.create_user(request_data)

@app.routes("/users", methods=['GET'])
def store_user():
    params
    users = UsersService()
    return users.create_user(request_data)
