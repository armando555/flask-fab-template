from flask_appbuilder.api import ModelRestApi
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_babel import gettext as __
from app.models import CustomUser
from flask import request
import json
from app.api.utils.cached_model_rest_api import CachedModelRestApiDefault
from app import cache


class CustomUserRestAPI(CachedModelRestApiDefault):
    resource_name = __('ab_user')
    datamodel = SQLAInterface(CustomUser)

    def pre_add(self, item):
        item.generate_key()

    def pre_update(self, item):
        data = request.data.decode()
        data = json.loads(data)
        try:
          password = data["password"]
          if len(password)>0:
            item.generate_key()
        except:
          pass
        
