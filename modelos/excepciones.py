# Excepciones personalizadas del sistema

# Clase de excepción utilizada cuando
# los datos generales del cliente son inválidos
class ClienteInvalidoError(Exception):
    """Se lanza cuando los datos del cliente son inválidos"""
    pass

# Clase de excepción utilizada cuando
# el correo electrónico no cumple
# con el formato requerido
class CorreoInvalidoError(Exception):
    """Se lanza cuando el correo no tiene formato válido"""
    pass

# Clase de excepción utilizada cuando
# la edad ingresada no es permitida
class EdadInvalidaError(Exception):
    """Se lanza cuando la edad no es válida"""
    pass