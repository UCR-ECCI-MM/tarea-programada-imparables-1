import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import sys
from PyQt5.QtWidgets import QApplication

try: # Try to load the Class Controller
    from controller.Controller import Controller #Linux
except ImportError:
    from Entregable4.controller.Controller import Controller #Mac

def main():
    # Inicializa QApplication antes de cualquier QWidget
    app = QApplication(sys.argv)

    # Crear la controladora y correr el programa
    controller = Controller()
    controller.run()

    # Ejecuta el evento de la aplicación
    sys.exit(app.exec_())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = Controller()
    controller.run()
    sys.exit(app.exec_())