# prestamos/utils.py
from django.contrib.auth.models import User

def obtener_tipo_cliente(usuario):
    # Ejemplo de lógica para determinar el tipo de cliente basado en el nombre de usuario
    if usuario.username.startswith('premium'):
        return 'GOLD'
    elif usuario.username.startswith('black'):
        return 'BLACK'
    else:
        return 'CLASSIC'

def obtener_limite_preaprobacion(tipo_cliente):
    # Ejemplo de lógica para determinar el límite de preaprobación según el tipo de cliente
    if tipo_cliente == 'GOLD':
        return 300000.0
    elif tipo_cliente == 'BLACK':
        return 500000.0
    elif tipo_cliente == 'CLASSIC':
        return 100000.0
    else:
        return 0.0  # Tipo de cliente no reconocido
