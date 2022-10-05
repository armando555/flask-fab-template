import os
from flask_appbuilder.security.sqla.models import User as FABUser
from sqlalchemy import Column, Float
from werkzeug.security import generate_password_hash


class CustomUser(FABUser):
    __tablename__       = 'ab_user'
    latitude = Column(Float)
    longitude = Column(Float)
    altitude = Column(Float)

    
    def __repr__(self):
        return f'{self.id} | {self.first_name} {self.last_name}'
    
    def generate_key(self):
        self.password = generate_password_hash(self.password)
