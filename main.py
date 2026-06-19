from app.controllers.bitacora_controller import BitacoraController

if __name__ == "__main__":
    # Punto de entrada principal: instancia el controlador (que a su vez carga modelo y vista)
    aplicacion = BitacoraController()
    
    # Inicia el ciclo de vida de la interfaz gráfica
    aplicacion.vista.iniciar()