from typing import Tuple

class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        with open(self.nombre_archivo, "r") as f:
            datos = f.readlines()

        temperatura_total = 0
        velocidad_viento_total = 0
        temperatura_maxima = -273.15  # Temperatura más baja posible en grados Celsius
        velocidad_viento_maxima = 0
        direcciones_viento = []