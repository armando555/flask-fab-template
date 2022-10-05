from ..models.module import Module

def set_module(control_info):
    default_modules = [
        Module(type_state_name='Maestros', **control_info),
        Module(type_state_name='Administrativos', **control_info),
        Module(type_state_name='Listas de control', **control_info),
        Module(type_state_name='Prospecto', **control_info),
        Module(type_state_name='Calendario', **control_info),
        Module(type_state_name='Casos', **control_info),
        Module(type_state_name='Vehículos', **control_info),
        Module(type_state_name='Eventos', **control_info),
        Module(type_state_name='Facturas', **control_info),
        Module(type_state_name='Campañas', **control_info),
        Module(type_state_name='Contratos de servicio', **control_info),
        Module(type_state_name='Tareas de proyectos',**control_info),
        Module(type_state_name='Proyectos',**control_info),
        Module(type_state_name='Inventario',**control_info),
        Module(type_state_name='Orden de compra',**control_info),
        Module(type_state_name='Residual',**control_info),
    ]
    return default_modules