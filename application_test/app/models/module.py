from flask_appbuilder import Model
from sqlalchemy import Column,  Integer, String
from flask_appbuilder.models.mixins import AuditMixin

class Module(Model, AuditMixin):
    __tablename__ = "modules"
    id = Column(Integer, primary_key=True)
    type_state_name = Column(String(100), nullable=False)
    name_2 = Column(String(100))
    name_1 = Column(String(100))


    def __repr__(self):
        return f'{self.id} | {self.type_state_name}'
