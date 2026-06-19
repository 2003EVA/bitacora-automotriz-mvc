import json
import os
from app.models.vehiculo import Vehiculo

class GestorBitacora:
    """Clase encargada de gestionar la persistencia y operaciones principales de los vehículos."""

    def __init__(self, archivo="bitacora.json"):
        self.archivo = archivo
        self.vehiculos = {}
        self.cargar_datos()

    def registrar_vehiculo(self, vehiculo):
        """Almacena un nuevo vehículo y sincroniza con el archivo persistente."""
        self.vehiculos[vehiculo.placa] = vehiculo
        self.guardar_datos()

    def eliminar_vehiculo(self, placa):
        """Elimina un vehículo por placa y actualiza el archivo JSON."""
        if placa in self.vehiculos:
            del self.vehiculos[placa]
            self.guardar_datos()
            return True
        return False

    def buscar_vehiculo(self, placa):
        """Busca un vehículo en memoria; lanza excepción si no existe."""
        if placa not in self.vehiculos:
            raise KeyError(f"No se encontró ningún vehículo con la placa {placa}.")
        return self.vehiculos[placa]

    def guardar_datos(self):
        """Serializa los objetos a un diccionario simple y los guarda en un archivo JSON."""
        # Convertimos la estructura de objetos a un formato plano (dict)
        datos = {p: v.to_dict() for p, v in self.vehiculos.items()}
        with open(self.archivo, 'w') as f:
            json.dump(datos, f, indent=4)

    def cargar_datos(self):
        """Lee el archivo JSON al iniciar el programa para recuperar el estado anterior."""
        # Verificamos si existe el archivo antes de intentar abrirlo
        if os.path.exists(self.archivo):
            with open(self.archivo, 'r') as f:
                datos = json.load(f)
                for placa, v_dict in datos.items():
                    # Reconstruimos la instancia de Vehiculo con los datos almacenados
                    v = Vehiculo(v_dict["placa"], v_dict["marca"], v_dict["kilometraje_actual"], v_dict["tipo"])
                    self.vehiculos[placa] = v