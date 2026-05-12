from modelos.cliente import Cliente
from modelos.servicios_concretos import (
    ReservaSala,
    AlquilerEquipo,
    Asesoria
)

from modelos.reserva import Reserva
from modelos.excepciones import *
from modelos.logger import log_info, log_error

print("\n          SOFTWARE FJ         \n")

try:
    # Crear cliente
    cliente1 = Cliente(
        "Miguel",
        "miguel@gmail.com",
        20
    )

    print(cliente1.mostrar_informacion())
    print("\n-------------------------\n")

    # Crear servicios
    sala = ReservaSala(3)
    equipo = AlquilerEquipo(2)
    asesoria = Asesoria(1)

    # Mostrar servicios
    print(sala.descripcion())
    print("Costo:", sala.calcular_costo())
    print()

    print(equipo.descripcion())
    print("Costo:", equipo.calcular_costo())
    print()

    print(asesoria.descripcion())
    print("Costo:", asesoria.calcular_costo())

    print("\n-------------------------\n")

    # Crear reserva
    reserva1 = Reserva(cliente1, sala)

    print("Estado reserva:", reserva1.estado)

    reserva1.confirmar()

    print("Nuevo estado:", reserva1.estado)
    print()

    total = reserva1.calcular_total()

    print("Total reserva:", total)
    print()

    total_completo = reserva1.calcular_total_reserva(
        descuento=10000,
        impuesto=0.19,
        cargo_extra=5000
    )

    print("Total con impuestos:", total_completo)

    log_info(
        "OP1: Operacion completa exitosa - cliente Miguel, sala 3h"
    )

except Exception as e:
    log_error(f"OP1: {e}")
    print("ERROR:", e)


# OPERACIÓN 2: Cliente con correo inválido
print("\n--- OP2: Cliente con correo inválido ---")

try:
    cliente_mal = Cliente(
        "Laura",
        "correo-sin-arroba",
        25
    )

except CorreoInvalidoError as e:
    log_error(f"OP2: {e}")
    print("CorreoInvalidoError capturado:", e)

except ClienteInvalidoError as e:
    log_error(f"OP2: {e}")
    print("ClienteInvalidoError capturado:", e)


# OPERACIÓN 3: Cliente con edad fuera de rango
print("\n--- OP3: Cliente con edad inválida (15 años) ---")

try:
    cliente_joven = Cliente(
        "Pedro",
        "pedro@gmail.com",
        15
    )

except ClienteInvalidoError as e:
    log_error(f"OP3: {e}")
    print("ClienteInvalidoError capturado:", e)


# OPERACIÓN 4: Cliente con nombre vacío
print("\n--- OP4: Cliente con nombre vacío ---")

try:
    cliente_sin_nombre = Cliente(
        "",
        "vacio@gmail.com",
        30
    )

except ClienteInvalidoError as e:
    log_error(f"OP4: {e}")
    print("ClienteInvalidoError capturado:", e)


# OPERACIÓN 5: Servicio con parámetro inválido (horas = 0)
print("\n--- OP5: ReservaSala con 0 horas ---")

try:
    sala_mala = ReservaSala(0)

except ServicioError as e:
    log_error(f"OP5: {e}")
    print("ServicioError capturado:", e)


# OPERACIÓN 6: Servicio con parámetro negativo
print("\n--- OP6: AlquilerEquipo con días negativos ---")

try:
    equipo_malo = AlquilerEquipo(-3)

except ServicioError as e:
    log_error(f"OP6: {e}")
    print("ServicioError capturado:", e)


# OPERACIÓN 7: Reserva con cliente válido y cancelación
print("\n--- OP7: Reserva de asesoría y cancelación ---")

try:
    cliente2 = Cliente(
        "Sofía",
        "sofia@gmail.com",
        32
    )

    asesoria2 = Asesoria(2)

    reserva2 = Reserva(
        cliente2,
        asesoria2
    )

    print("Estado inicial:", reserva2.estado)

    reserva2.cancelar()

    print("Estado tras cancelar:", reserva2.estado)
    print("Costo servicio:", asesoria2.calcular_costo())

    log_info(
        "OP7: Reserva de asesoria creada y cancelada correctamente"
    )

except Exception as e:
    log_error(f"OP7: {e}")
    print("ERROR:", e)


# OPERACIÓN 8: Reserva con descuento mayor al costo (inválido)
print("\n--- OP8: Descuento mayor al costo de la reserva ---")

try:
    cliente3 = Cliente(
        "Carlos",
        "carlos@gmail.com",
        45
    )

    equipo2 = AlquilerEquipo(1)

    reserva3 = Reserva(
        cliente3,
        equipo2
    )

    reserva3.confirmar()

    total_invalido = reserva3.calcular_total(
        descuento=999999
    )

except ReservaError as e:
    log_error(f"OP8: {e}")
    print("ReservaError capturado:", e)

except Exception as e:
    log_error(f"OP8: {e}")
    print("ERROR:", e)


# OPERACIÓN 9: Múltiples servicios, cálculo total con impuestos
print(
    "\n--- OP9: Cliente con equipo, total con impuesto y cargo extra ---"
)

try:
    cliente4 = Cliente(
        "Ana",
        "ana@empresa.com",
        28
    )

    equipo3 = AlquilerEquipo(5)

    reserva4 = Reserva(
        cliente4,
        equipo3
    )

    reserva4.confirmar()

    print(cliente4.mostrar_informacion())

    print(
        equipo3.descripcion(),
        "| Costo base:",
        equipo3.calcular_costo()
    )

    total4 = reserva4.calcular_total_reserva(
        descuento=5000,
        impuesto=0.19,
        cargo_extra=8000
    )

    print("Total final con impuesto y cargo:", total4)

    log_info(
        "OP9: Reserva equipo 5 dias con impuesto y cargo extra procesada"
    )

except Exception as e:
    log_error(f"OP9: {e}")
    print("ERROR:", e)


# OPERACIÓN 10: Cliente mayor de 100 años (inválido)
print("\n--- OP10: Cliente con edad 110 años ---")

try:
    cliente_viejo = Cliente(
        "Hugo",
        "hugo@gmail.com",
        110
    )

except ClienteInvalidoError as e:
    log_error(f"OP10: {e}")
    print("ClienteInvalidoError capturado:", e)

print("\n          FIN DEL SISTEMA         \n")