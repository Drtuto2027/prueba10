import tkinter as tk
from tkinter import ttk
import random
import time

# Función para actualizar los valores de voltaje y temperatura
def actualizar_datos():
    # Simular valores aleatorios de voltaje y temperatura
    voltaje = round(random.uniform(110, 230), 2)  # Voltaje entre 110V y 230V
    temperatura = round(random.uniform(15, 90), 2)  # Temperatura entre 15°C y 90°C
    
    # Actualizar las etiquetas en la interfaz
    etiqueta_voltaje.config(text=f"Voltaje: {voltaje} V")
    etiqueta_temperatura.config(text=f"Temperatura: {temperatura} °C")
    
    # Programar la próxima actualización en 1000 ms (1 segundo)
    ventana.after(1000, actualizar_datos)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Simulación de Generador")
ventana.geometry("300x150")

# Etiqueta para el voltaje
etiqueta_voltaje = ttk.Label(ventana, text="Voltaje: --- V", font=("Helvetica", 14))
etiqueta_voltaje.pack(pady=10)

# Etiqueta para la temperatura
etiqueta_temperatura = ttk.Label(ventana, text="Temperatura: --- °C", font=("Helvetica", 14))
etiqueta_temperatura.pack(pady=10)

# Iniciar la actualización de datos
actualizar_datos()

# Iniciar el loop de la interfaz
ventana.mainloop()
