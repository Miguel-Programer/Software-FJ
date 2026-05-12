from abc import ABC, abstractmethod  # Importa las clases necesarias para definir una clase abstracta
# y métodos abstractos


# Clase abstracta que representa un servicio ofrecido por la empresa
class Servicio(ABC):

    # Inicializa el servicio con un nombre y valida los parámetros
    def __init__(self, nombre):
        self._nombre = nombre

    @abstractmethod
    # Define un método abstracto para calcular el costo del servicio,
    # que debe ser implementado por las clases concretas
    def calcular_costo(self):
        pass

    @abstractmethod
    # Define un método abstracto para obtener la descripción del servicio,
    # que debe ser implementado por las clases concretas
    def descripcion(self):
        pass

    @abstractmethod
    # Define un método abstracto para validar los parámetros del servicio,
    # que debe ser implementado por las clases concretas
    def validar_parametros(self):
        pass