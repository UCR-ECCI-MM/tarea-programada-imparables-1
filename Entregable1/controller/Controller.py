from Entregable1.view.View import View
# from model.Model import Model
from PyQt5.QtWidgets import QVBoxLayout, QDialog, QMessageBox
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
                # Crear el QMessageBox
                msg_box = QMessageBox(self.view)
                msg_box.setWindowTitle("Opción 1")
                msg_box.setText("Has seleccionado la opción 1")

                # Aplicar estilos CSS al QMessageBox
                msg_box.setStyleSheet("""
                    QMessageBox {
                        background-color: #f0f0f0;
                        font-family: Arial;
                        font-size: 14px;
                    }
                    QMessageBox QLabel {
                        color: #ffffff;
                        background-color: #000000;
                        border-radius: 5px;
                        padding: 6px;
                    }
                    QMessageBox QPushButton {
                        background-color: #0078d7;
                        color: white;
                        padding: 5px 10px;
                        border-radius: 5px;
                    }
                    QMessageBox QPushButton:hover {
                        background-color: #005bb5;
                    }
                """)

                # Mostrar el QMessageBox
                msg_box.exec_()
            # ------------------------------------PROVISIONAL------------------------------------
        else:
            print("Unknown action!")

    def run(self):
        """
        Initialize the view
        """
        self.view.run()