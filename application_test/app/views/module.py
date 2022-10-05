#from flask_appbuilder import ModelView
from .base import CustomModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface

from app.models import Module


class ModuleView(CustomModelView):
    datamodel = SQLAInterface(Module)
    #add_exclude_columns = [ 'system_date' ]
    list_columns = ['id','type_state_name']
    add_exclude_columns =  ['changed_on', 'changed_by', 'created_by', 'created_on']
    edit_exclude_columns =  ['changed_on', 'changed_by', 'created_by', 'created_on']
