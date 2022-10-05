from flask_appbuilder.security.sqla.manager import SecurityManager as FABSecurityManager
from app.models.user import CustomUser
from .user_db import MyUserDBModelView


class SecurityManager(FABSecurityManager):
    user_model = CustomUser
    userdbmodelview = MyUserDBModelView
