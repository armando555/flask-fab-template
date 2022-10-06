from flask_appbuilder.api import ModelRestApi
from app import cache


#This function is based on decorators flows and using the patter class factory
#the ideal is create a new variable with a different timeout and import it to the specific API that we need to use
def CachedModelRestApiFactory(timeout):
    class CachedModelRestApi(ModelRestApi):
        get_list = cache.cached(timeout=timeout)(ModelRestApi.get_list)
        get = cache.cached(timeout=timeout)(ModelRestApi.get)
    return CachedModelRestApi

#This is the default value of the timeout of 50 seconds
CachedModelRestApiDefault = CachedModelRestApiFactory(timeout=50)