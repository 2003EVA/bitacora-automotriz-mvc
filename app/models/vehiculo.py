from app.models.servicio import Servicio

class Vehiculo:
    """Representa un vehículo (Auto o Moto) y gestiona su historial de mantenimiento."""

    def __init__(self, placa: str, marca: str, kilometraje_actual: int, tipo: str):
        # Validación de datos: aseguramos que el estado inicial del objeto sea coherente
        if int(kilometraje_actual) < 0:
            raise ValueError("El kilometraje actual no puede ser negativo.")
        
        # Normalizamos el tipo de vehículo para evitar inconsistencias en la base de datos
        tipo_formateado = tipo.strip().capitalize()
        if tipo_formateado not in ["Auto", "Moto"]:
            raise ValueError("El tipo de vehículo debe ser 'Auto' o 'Moto'.")
            
        self.placa = placa.upper()
        self.marca = marca
        self.kilometraje_actual = int(kilometraje_actual)
        self.tipo = tipo_formateado
        self.historial_servicios = []  

    def agregar_servicio(self, servicio: Servicio):
        """Añade un servicio al historial y actualiza el kilometraje actual si el servicio es más reciente."""
        self.historial_servicios.append(servicio)
        
        # Lógica de negocio: el kilometraje del vehículo siempre debe ser el máximo registrado
        if servicio.kilometraje_servicio > self.kilometraje_actual:
            self.kilometraje_actual = servicio.kilometraje_servicio

    def obtener_total_gastado(self) -> float:
        """Calcula el costo acumulado de todos los servicios asociados al vehículo."""
        return sum(servicio.costo for servicio in self.historial_servicios)

    def to_dict(self):
        """Serializa la instancia y su historial a un diccionario para almacenamiento JSON."""
        return {
            "placa": self.placa,
            "marca": self.marca,
            "kilometraje_actual": self.kilometraje_actual,
            "tipo": self.tipo,
            "historial_servicios": [
                {
                    "fecha": s.fecha,
                    "descripcion": s.descripcion,
                    "costo": s.costo,
                    "kilometraje_servicio": s.kilometraje_servicio
                } for s in self.historial_servicios
            ]
        }