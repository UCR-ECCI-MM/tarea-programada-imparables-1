from view.View import View
# from model.Model import Model
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class Controller:

    def __init__(self):
        """
        Initialize the view
        """
        self.view = View(self)  # Build the view and pass the controller as a parameter
        print("Controller build!")

    def handleButtonClick(self, action):
        """
        Handle the button click event based on the action.
        """
        print(f"Button clicked! Action: {action}")

        if action == 'startApp':
            self.view.switchToMainWindow()
        elif action == "GRAFICO":
            # ------------------------------------PROVISIONAL------------------------------------
            graphDialog = QDialog(self.view)
            graphDialog.setWindowTitle("Gráfico de Barras")
            graphDialog.setGeometry(100, 100, 400, 300)

            # Create a layout for the dialog
            layout = QVBoxLayout()

            # Create a matplotlib figure and axis
            fig = Figure()
            ax = fig.add_subplot(111)

            # Data for the bar chart
            datos = {'A': 20, 'B': 34, 'C': 30, 'D': 35}
            ax.bar(datos.keys(), datos.values())
            ax.set_title("Datos Inventados")

            # Embed the figure in a PyQt5 canvas
            canvas = FigureCanvas(fig)
            layout.addWidget(canvas)

            # Set the layout to the dialog
            graphDialog.setLayout(layout)

            # Show the dialog
            graphDialog.exec_()
            # ------------------------------------PROVISIONAL------------------------------------
        elif action == "FUNCIONABILIDAD":
            # ------------------------------------PROVISIONAL------------------------------------
            messagebox.showinfo("Opción 1", "Has seleccionado la opción 1")
            # ------------------------------------PROVISIONAL------------------------------------
        else:
            print("Unknown action!")

    def run(self):
        """
        Initialize the view
        """
        self.view.run()