try: # Intento directo de importación
    from view.View import View #Linux
except ImportError:
    from Entregable4.view.View import View #Mac

try: 
    from model.Model import Model  # Import the model
except ImportError:
    from Entregable4.model.Model import Model #Mac

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
        self.model = Model()  # Build the model
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
        elif action == "analizar":
            self.dataAnalisis()

        else:
            print("Unknown action!")

    def dataAnalisis(self):
        """
        Perform lexical analysis and print the results.
        """
        file_path = 'Docs/large_complex_log.txt'

        # Call the model to perform lexical analysis
        has_errors = self.model.lexerAnalyze(file_path)

        if has_errors:
            # Retrieve and print the lexical errors
            lexicalErrors = self.model.getLexicalErrors()
            print("Lexical Errors Found:")
            for error in lexicalErrors:
                print(error)
        else:
            print("Análisis léxico completado sin errores.")

        self.model.parserAnalyzeData(file_path)


        # ------------------------TEST THE LEXER------------------------
        # self.model.lexerAnalyze(file_path)
        # # Retrieve and print the lexical data
        # lexicalData = self.model.getLexicalData()
        # print("Lexical Data:")
        # for token in lexicalData:
        #     print(token)

    def run(self):
        """
        Initialize the view
        """
        self.view.run()