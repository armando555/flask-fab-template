from .user import CustomUserRestAPI
from .auth_helper import AuthHelperAPI
from app import appbuilder




# CRUD SECTION
appbuilder.add_api(AuthHelperAPI)
appbuilder.add_api(CustomUserRestAPI)