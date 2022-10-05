from flask import render_template

from app import appbuilder, db

from .module import ModuleView
from .user import UserView



def print_dropdown(group: list):
    for widget in group:
        if widget['view'] == 'separator':
            appbuilder.add_separator(widget['category'])
            continue
        
        appbuilder.add_view(
            widget['view'],
            widget['label'],
            icon=widget['icon'],
            category=widget['category']
        )

@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )

appbuilder.add_link("API", href="http://localhost:5000/swagger/v1", icon = "fa-solid fa-gears")

admin_group = [
    {'view':UserView, 'label': 'User', 'icon': 'fa-home', 'category': 'Administration'},
    {'view':'separator','category': 'Administration'},
    {'view':ModuleView, 'label': 'Module', 'icon': 'fa-home', 'category': 'Administration'}
]
print_dropdown(admin_group)
db.create_all()
