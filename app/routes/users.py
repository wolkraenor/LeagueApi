from . import app
from Flask import request
from services.users import UsersService


@app.routes("/users", methods=['POST'])
def user():
    request_data = request.json
    users = UsersService()
    return users.create_user(request_data)


@app.routes("/users", methods=['GET'])
def store_user():
    request_data = request.json
    users = UsersService()
    return users.create_user(request_data)
