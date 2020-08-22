from app import db

class Users(db.Model):
    __tablename__ = "users"
    id =  db.Columns(db.Interger, primary_key=True)
    fullname = db.Columns(db.String(100), nullable=False)
    country = db.Columns(db.String(100), nullable=False)
    username = db.Columns(db.String(16), nullable=False)
    password = db.Columns(db.Interger, nullable=False)
    
    def __init__(self, fullname, country, username, password):
        self.country = country
        self.fullname = fullname
        self.username = username
        self.password = password
        
    
