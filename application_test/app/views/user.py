from flask_appbuilder.models.sqla.interface import SQLAInterface
#from flask_appbuilder import ModelView
from .base import CustomModelView

from app.models import CustomUser


class UserView(CustomModelView):
    datamodel = SQLAInterface(CustomUser)
    list_columns = ['id','first_name','last_name']

    def pre_add(self, item):
        item.generate_key()