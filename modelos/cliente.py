# Importación de excepciones personalizadas
# utilizadas para validar datos del cliente
from modelos.excepciones import (
    ClienteInvalidoError,
    CorreoInvalidoError,
    EdadInvalidaError
)


# Clase que representa un cliente dentro del sistema
class Cliente:

    # Inicia y valida los datos recibidos
    def __init__(self, nombre, correo, edad):

        try:
            # Validación y asignación del nombre
            self.__nombre = self.validar_nombre(nombre)

            # Validación y asignación del correo
            self.__correo = self.validar_correo(correo)

            # Validación y asignación de la edad
            self.__edad = self.validar_edad(edad)

        # Captura cualquier error durante la creación
        # del cliente y lanza una excepción personalizada
        except Exception as e:
            raise ClienteInvalidoError(
                f"Error al crear cliente: {e}"
            ) from e

    # VALIDACIONES

    # Método encargado de validar el nombre
    def validar_nombre(self, nombre):

        # Verifica que el nombre no esté vacío
        if not nombre or not isinstance(nombre, str):
            raise ClienteInvalidoError(
                "El nombre no puede estar vacío"
            )

        # Convierte el nombre a formato título
        return nombre.title()

    # Método encargado de validar el correo electrónico
    def validar_correo(self, correo):

        # Verifica que el correo contenga
        # caracteres básicos coomo @ y .
        if "@" not in correo or "." not in correo:
            raise CorreoInvalidoError(
                "Correo electrónico inválido"
            )

        return correo

    # Método encargado de validar la edad
    def validar_edad(self, edad):

        # Verifica que la edad esté dentro
        # del rango permitido por el sistema
        if edad < 18 or edad > 100:
            raise EdadInvalidaError(
                "La edad debe estar entre 18 y 100 años"
            )

        return edad

    # Devuelve el nombre del cliente
    def get_nombre(self):
        return self.__nombre

    # Devuelve el correo del cliente
    def get_correo(self):
        return self.__correo

    # Devuelve la edad del cliente
    def get_edad(self):
        return self.__edad

    # Modifica el nombre del cliente
    # aplicando nuevamente validaciones
    def set_nombre(self, nuevo_nombre):
        self.__nombre = self.validar_nombre(nuevo_nombre)

    # Modifica el correo del cliente
    # aplicando nuevamente validaciones
    def set_correo(self, nuevo_correo):
        self.__correo = self.validar_correo(nuevo_correo)

    # Modifica la edad del cliente
    # aplicando nuevamente validaciones
    def set_edad(self, nueva_edad):
        self.__edad = self.validar_edad(nueva_edad)

    # MÉTODOS

    # Devuelve toda la información
    # del cliente en formato texto
    def mostrar_informacion(self):

        return (
            f"Cliente: {self.__nombre} | "
            f"Correo: {self.__correo} | "
            f"Edad: {self.__edad}"
        )