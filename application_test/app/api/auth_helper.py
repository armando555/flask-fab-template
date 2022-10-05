from flask_appbuilder.api import BaseApi, expose
from flask_login import current_user
from flask_appbuilder.security.decorators import protect
from flask_jwt_extended import get_current_user
from flask import redirect



class AuthHelperAPI(BaseApi):
    apispec_parameter_schemas = {
        "greeting_schema": "kagsdas"
    }


    @expose('/current_user/', methods=['POST'])
    @protect()
    def current_user_pk(self):
        """Send a greeting
        ---
        post:
          parameters:
            - $ref: '#/components/parameters/greeting_schema'
          responses:
            200:
              description: Get Id from the current user
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      message:
                        type: string
        """
        try:
            return self.response(200, message=get_current_user().id)
        except Exception as e:
            print(e)
            return self.response_401()
    
    @expose('/backend/', methods=['POST'])
    @protect()
    def redirect_back(self):
        return redirect('/')

