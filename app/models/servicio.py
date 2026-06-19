class Servicio:
    """Representa un mantenimiento o reparación realizada a un vehículo."""

    def __init__(self, fecha: str, descripcion: str, costo: float, kilometraje_servicio: int):
        # Validaciones de integridad: prevenimos datos inconsistentes (precios o km negativos)
        if costo < 0:
            raise ValueError("El costo del servicio no puede ser negativo.")
        if kilometraje_servicio < 0:
            raise ValueError("El kilometraje no puede ser negativo.")

        self.fecha = fecha
        self.descripcion = descripcion
        self.costo = costo
        self.kilometraje_servicio = kilometraje_servicio

    def __str__(self):
        """Retorna una representación legible del servicio para reportes o consola."""
        return f"{self.fecha} - {self.descripcion} | Costo: ${self.costo} | Km: {self.kilometraje_servicio}"