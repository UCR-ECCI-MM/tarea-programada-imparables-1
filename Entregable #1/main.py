import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import sys
from PyQt5.QtWidgets import QApplication
from controller.Controller import Controller

# def main():
#     # Inicializa QApplication antes de cualquier QWidget
#     app = QApplication(sys.argv)

#     # Crear la controladora y correr el programa
#     controller = Controller()
#     controller.run()

#     # Ejecuta el evento de la aplicación
#     sys.exit(app.exec_())

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     controller = Controller()
#     controller.run()
#     sys.exit(app.exec_())

# Ventana principal
root = tk.Tk()
root.title("Aplicación Prototipo")
root.geometry("300x200")

# Función para mostrar gráfico
def mostrar_grafico():
    datos = {'A': 20, 'B': 34, 'C': 30, 'D': 35}
    
    ventana_grafico = tk.Toplevel(root)
    ventana_grafico.title("Gráfico de barras")

    fig, ax = plt.subplots()
    ax.bar(datos.keys(), datos.values())
    ax.set_title("Datos Inventados")

    canvas = FigureCanvasTkAgg(fig, master=ventana_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Opciones del menú principal
def opcion_1():
    messagebox.showinfo("Opción 1", "Has seleccionado la opción 1")

def opcion_2():
    mostrar_grafico()

def opcion_3():
    messagebox.showinfo("Opción 3", "Has seleccionado la opción 3")

# Botones del menú
btn1 = tk.Button(root, text="Opción 1", command=opcion_1)
btn1.pack(pady=10)

btn2 = tk.Button(root, text="Mostrar Gráfico", command=opcion_2)
btn2.pack(pady=10)

btn3 = tk.Button(root, text="Opción 3", command=opcion_3)
btn3.pack(pady=10)

root.mainloop()