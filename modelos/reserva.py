from .cliente import Cliente # Importa la clase Cliente para validar el tipo de cliente en la reserva
from .servicio import Servicio # Importa la clase Servicio para validar el tipo de servicio en la reserva
from .excepciones import * # Importa las excepciones personalizadas para manejar errores específicos de la reserva
from .logger import log_error # Importa la función de logging para registrar errores en un archivo de texto

# Clase que representa una reserva realizada por un cliente para un servicio específico
class Reserva:
    def __init__(self, cliente, servicio):
        try:
            if not isinstance(cliente, Cliente):
                raise ClienteInvalidoError("Cliente inválido")

            if not isinstance(servicio, Servicio):
                raise Exception("Servicio inválido")

            self.cliente = cliente
            self.servicio = servicio
            self.estado = "Pendiente"

        except Exception as e:
            log_error(e)
            raise

# Métodos para gestionar el estado de la reserva y calcular el costo total
    def confirmar(self):
        try:
            self.estado = "Confirmada"
        except Exception as e:
            log_error(e)

    def cancelar(self):
        try:
            self.estado = "Cancelada"
        except Exception as e:
            log_error(e)

    # Método para calcular el costo total, ademas de aplicar un descuento si es necesario
    def calcular_total(self, descuento=0):
        try:
            total = self.servicio.calcular_costo() - descuento
            if total < 0:
                raise ReservaError("Descuento inválido")
            return total
        except Exception as e:
            log_error(e)
            raise
