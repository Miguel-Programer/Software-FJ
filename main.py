# Importación de la clase Cliente
from modelos.cliente import Cliente

# Creación de un objeto cliente con datos validos
cliente1 = Cliente(
    "Miguel",
    "miguel@gmail.com",
    20
)

# Muestra en pantalla la información registrada del cliente
print(cliente1.mostrar_informacion())