import logging

# Configuración básica del logger para registrar errores en un archivo de texto
logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# Función para registrar errores en el archivo de logs
def log_error(mensaje):
    logging.error(mensaje)


# Función para registrar eventos importantes
def log_info(mensaje):
    logging.info(mensaje)
