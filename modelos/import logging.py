import logging

# Funciones de registro para que no marquen error en el editor
def log_error(mensaje):
    logging.error(mensaje)

def log_info(mensaje):
    logging.info(mensaje)

def calcular_total_reserva(self, descuento=0, impuesto=0, cargo_extra=0):
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
            raise Exception("El cálculo de la reserva resultó en un valor negativo.")

        return round(total_final, 2)

    except Exception as e:
        log_error(f"Fallo en el cálculo sobrecargado de la reserva: {e}")
        raise Exception("Error al procesar el total de la reserva") from e
