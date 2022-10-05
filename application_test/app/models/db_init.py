import os
from logging import getLogger

from datetime import datetime

#Import models
from .user import CustomUser as User
from .module import Module

#Import set
from app.set.set_module import set_module


def set_db_defaults(db_session):
    """
    Sets some default roles and other tables that need to be prefilled
    """
    
    user = db_session.query(User).filter(User.email == os.environ.get('ADMIN_EMAIL', 'NULL')).first()
    log = getLogger(__name__)
    if not user:
        log.error(f'No administrator user with email = "{os.environ.get("ADMIN_EMAIL", "NULL")}" was found, no tables will be populated!')
        return
    control_info=dict(created_by_fk=user.id, changed_by_fk=user.id, created_on=datetime.now(), changed_on=datetime.now())
   
    # Module
    i = db_session.query(Module).first()

    if not i:
        log.log(20, 'No data found for "Module", creating default rows.')
        
        default_task_types = set_module(control_info) 
        
        db_session.bulk_save_objects(default_task_types)
    db_session.commit()