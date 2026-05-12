from .cliente import Cliente  # Importa la clase Cliente para validar el tipo de cliente en la reserva
from .servicio import Servicio  # Importa la clase Servicio para validar el tipo de servicio en la reserva
from .excepciones import *  # Importa las excepciones personalizadas para manejar errores específicos de la reserva
from .logger import log_error, log_info  # Importa funciones del logger


# Clase que representa una reserva realizada por un cliente para un servicio específico
class Reserva:

    def __init__(self, cliente, servicio):

        try:

            if not isinstance(cliente, Cliente):
                raise ClienteInvalidoError("Cliente inválido")

            if not isinstance(servicio, Servicio):
                raise ServicioError("Servicio inválido")

            self.cliente = cliente
            self.servicio = servicio
            self.estado = "Pendiente"

            log_info("Reserva creada correctamente")

        except Exception as e:
            log_error(e)
            raise

    # Métodos para gestionar el estado de la reserva y calcular el costo total

    def confirmar(self):

        try:
            self.estado = "Confirmada"
            log_info("Reserva confirmada")

        except Exception as e:
            log_error(e)

    def cancelar(self):

        try:
            self.estado = "Cancelada"
            log_info("Reserva cancelada")

        except Exception as e:
            log_error(e)

    # Método para calcular el costo total, además de aplicar un descuento si es necesario

    def calcular_total(self, descuento=0):

        try:

            total = self.servicio.calcular_costo() - descuento

            if total < 0:
                raise ReservaError("Descuento inválido")

            return total

        except Exception as e:
            log_error(e)
            raise

    # Método sobrecargado para calcular total con impuestos y cargos extra

    def calcular_total_reserva(
        self,
        descuento=0,
        impuesto=0,
        cargo_extra=0
    ):

        try:

            # Obtener costo base de la reserva
            costo_base = self.servicio.calcular_costo()

            # Aplicar descuento a la reserva
            subtotal = costo_base - descuento

            # Calcular impuesto de la reserva
            valor_impuesto = subtotal * impuesto

            # Calcular total final de la reserva
            total_final = subtotal + valor_impuesto + cargo_extra

            # Validar total de la reserva
            if total_final < 0:
                raise ReservaError(
                    "El cálculo de la reserva resultó en un valor negativo."
                )

            return round(total_final, 2)

        except Exception as e:

            log_error(
                f"Fallo en el cálculo sobrecargado de la reserva: {e}"
            )

            raise ReservaError(
                "Error al procesar el total de la reserva"
            ) from e