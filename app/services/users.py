from app.models.users import Users
from app import db


class UsersService():
    def create_user(self, data):
        id = data['id']
        fullname = data['fullname']
        country = data['country']
        username = data['username']
        password = data['password']
        model = Users(id, username, fullname, password, country)
        db.session.add(model)
        db.session.commit()
        return model
