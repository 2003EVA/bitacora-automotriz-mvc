import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry

class GraficaView:
    """Clase encargada de la interfaz gráfica de usuario utilizando Tkinter."""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bitácora Automotriz MVC")
        self.root.geometry("400x400")
        
        tk.Label(self.root, text="Bitácora Automotriz", font=("Arial", 16, "bold")).pack(pady=15)
        
        # Botones principales: su acción será configurada por el controlador
        self.btn_registrar = tk.Button(self.root, text="Registrar Vehículo", width=25)
        self.btn_registrar.pack(pady=5)
        self.btn_servicio = tk.Button(self.root, text="Registrar Mantenimiento", width=25)
        self.btn_servicio.pack(pady=5)
        self.btn_consultar = tk.Button(self.root, text="Consultar Historial", width=25)
        self.btn_consultar.pack(pady=5)
        self.btn_eliminar = tk.Button(self.root, text="Eliminar Vehículo", width=25)
        self.btn_eliminar.pack(pady=5)
        
        # Botón para cerrar la aplicación de manera controlada
        self.btn_salir = tk.Button(self.root, text="Salir", width=25, command=self.root.destroy)
        self.btn_salir.pack(pady=20)
        
    def iniciar(self):
        """Inicia el ciclo principal de eventos de la ventana."""
        self.root.mainloop()

    def configurar_callback_eliminar(self, callback_abrir_lista):
        """Asigna la lógica para abrir el selector de eliminación desde el controlador."""
        self.btn_eliminar.config(command=callback_abrir_lista)

    def solicitar_eliminacion_con_lista(self, placas_disponibles, callback_eliminar):
        """Abre un modal con un menú desplegable para seleccionar la placa a eliminar."""
        top = tk.Toplevel(self.root)
        top.title("Eliminar Vehículo")
        top.geometry("300x250")
        
        tk.Label(top, text="Selecciona la placa a eliminar:").pack(pady=10)
        placa_var = tk.StringVar(value=placas_disponibles[0])
        tk.OptionMenu(top, placa_var, *placas_disponibles).pack(pady=5)
        
        def confirmar():
            callback_eliminar({"placa": placa_var.get()})
            top.destroy()
            
        tk.Button(top, text="Eliminar", command=confirmar).pack(pady=20)

    # --- Métodos de apoyo: creación de formularios dinámicos ---
    def abrir_formulario_registro(self, callback):
        self._crear_ventana_input("Nuevo Vehículo", ["Tipo", "Placa", "Marca", "Kilometraje"], callback)

    def abrir_formulario_servicio(self, callback):
        self._crear_ventana_input("Nuevo Servicio", ["Placa", "Fecha", "Descripción", "Costo", "Kilometraje"], callback)

    def abrir_formulario_consulta(self, callback):
        self._crear_ventana_input("Consultar Historial", ["Placa"], callback)

    def _crear_ventana_input(self, titulo, campos, callback):
        """Crea una ventana emergente genérica basada en una lista de campos requeridos."""
        top = tk.Toplevel(self.root)
        top.title(titulo)
        top.geometry("300x400")
        entries = {}
        for campo in campos:
            tk.Label(top, text=campo, pady=5).pack()
            # Diferenciamos tipos de entrada: Fecha, Selección o Texto libre
            if campo == "Fecha": e = DateEntry(top, width=20, date_pattern='dd/mm/yyyy')
            elif campo == "Tipo":
                e = tk.StringVar(value="Auto")
                tk.OptionMenu(top, e, "Auto", "Moto").pack()
            else: e = tk.Entry(top, width=30)
            
            if not isinstance(e, tk.StringVar): e.pack()
            entries[campo.lower()] = e
        
        def enviar():
            # Recolectamos datos de todos los widgets antes de llamar al callback
            datos = {k: v.get() if isinstance(v, (tk.Entry, tk.StringVar)) else v.get() for k, v in entries.items()}
            callback(datos)
            top.destroy()
            
        tk.Button(top, text="Confirmar", command=enviar, width=20).pack(pady=20)

    def mostrar_mensaje(self, mensaje: str, exito: bool = True):
        """Despliega un mensaje de información o error mediante un cuadro de diálogo."""
        messagebox.showinfo("Info" if exito else "Error", mensaje)