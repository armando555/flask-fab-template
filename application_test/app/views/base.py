from flask_appbuilder import ModelView as FABModelView

class CustomModelView(FABModelView):
    add_exclude_columns =  ['changed_on', 'changed_by', 'created_by', 'created_on']
    edit_exclude_columns = ['changed_on', 'changed_by', 'created_by', 'created_on']
    show_exclude_columns = ['changed_on', 'changed_by', 'created_by', 'created_on']