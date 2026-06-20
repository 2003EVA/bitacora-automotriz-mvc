import pytest
from app.models.vehiculo import Vehiculo
from app.models.servicio import Servicio
from app.models.gestor import GestorBitacora

def test_vehiculo_calcula_total_gastado():
    mi_auto = Vehiculo("ABC123", "Toyota", 50000, "Auto")
    servicio = Servicio("2026-06-19", "Cambio de Aceite", 45.0, 50000)
    mi_auto.agregar_servicio(servicio)
    assert len(mi_auto.historial_servicios) == 1
    
def test_gestor_busca_vehiculo_correctamente():
    gestor = GestorBitacora()
    moto = Vehiculo("XYZ98M", "Yamaha", 10000, "Moto")
    gestor.registrar_vehiculo(moto)
    vehiculo_encontrado = gestor.buscar_vehiculo("XYZ98M")
    assert vehiculo_encontrado is not None
    assert vehiculo_encontrado.marca == "Yamaha"

def test_crear_servicio_costo_negativo_lanza_error():
    with pytest.raises(ValueError) as informacion_error:
        servicio_invalido = Servicio("2026-06-19", "Lavado", -50.0, 100)
    
    assert "El costo y kilometraje deben ser positivos." in str(informacion_error.value)
