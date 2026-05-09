from .servicio import  Servicio # Importa la clase Servicio para heredar sus métodos y atributos
from .excepciones import (ServicioError) # Importa la excepción personalizada para manejar 
# errores específicos de los servicios

class ReservaSala(Servicio): # Clase concreta que representa el servicio de reserva de sala, hereda de Servicio
    def __init__(self, horas):
        super().__init__("Sala")
        self.horas = horas
        self.validar_parametros()

    def validar_parametros(self):
        if self.horas <= 0:
            raise ServicioError("Horas inválidas")

    def calcular_costo(self):
        return self.horas * 50000

    def descripcion(self):
        return f"Sala por {self.horas} horas"

class AlquilerEquipo(Servicio): # Clase concreta que representa el servicio de alquiler de equipo, hereda de Servicio
    def __init__(self, dias):
        super().__init__("Equipo")
        self.dias = dias
        self.validar_parametros()

    def validar_parametros(self):
        if self.dias <= 0:
            raise ServicioError("Días inválidos")

    def calcular_costo(self):
        return self.dias * 30000

    def descripcion(self):
        return f"Equipo por {self.dias} días"

class Asesoria(Servicio): # Clase concreta que representa el servicio de asesoría, hereda de Servicio
    def __init__(self, horas):
        super().__init__("Asesoría")
        self.horas = horas
        self.validar_parametros()

    def validar_parametros(self):
        if self.horas <= 0:
            raise ServicioError("Horas inválidas")
    def calcular_costo(self):
        return self.horas * 80000

    def descripcion(self):
        return f"Asesoría por {self.horas} horas"
