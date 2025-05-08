try: # Intento directo de importación
    from view.View import View #Linux
except ImportError:
    from Entregable4.view.View import View #Mac

try: 
    from model.Model import Model  # Import the model
except ImportError:
    from Entregable4.model.Model import Model #Mac

# from model.Model import Model
from PyQt5.QtWidgets import QVBoxLayout, QDialog, QMessageBox, QFileDialog
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
        elif action == "agregar":
            file_path = self.selectFile()
            self.view.switchToDashboard()
            # AQUI DEME LAS ESTRUCTURAS DE LOS DATOS


        else:
            print("Unknown action!")

    def dataAnalisis(self, file_path):
        """
        Perform lexical analysis and print the results.
        """

        if not file_path:
            return

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

        parserData = self.model.getParserData()

        self.view.switchToDashboard()
        self.view.displayParsedData(parserData)

        for entry in parserData:
            entry_type = entry[0]
            entry_data = entry[1]
            entry_blocks = entry[2]

            print(f"\n\nTipo de entrada: {entry_type}")
            print("Datos principales:")
            for key, value in entry_data.items():
                print(f"  {key}: {value}")

            print("Bloques asociados:")
            for block in entry_blocks:
                block_type = block[0]
                block_data = block[1]

                print(f"  Tipo de bloque: {block_type}")
                if isinstance(block_data, list):  # Si el bloque contiene una lista
                    for item in block_data:
                        print(f"    {item}")
                elif isinstance(block_data, dict):  # Si el bloque contiene un diccionario
                    for key, value in block_data.items():
                        print(f"    {key}: {value}")
                else:
                    print(f"    {block_data}")


        # ------------------------TEST THE LEXER------------------------
        # self.model.lexerAnalyze(file_path)
        # # Retrieve and print the lexical data
        # lexicalData = self.model.getLexicalData()
        # print("Lexical Data:")
        # for token in lexicalData:
        #     print(token)
    
    def selectFile(self):
        """
        Open a file dialog to select a file and store the selected file path.
        """
        # Abrir el cuadro de diálogo para seleccionar un archivo
        file_path, _ = QFileDialog.getOpenFileName(
            None,  # Ventana padre (None para usar la ventana principal)
            "Seleccionar archivo",  # Título del cuadro de diálogo
            "",  # Directorio inicial (vacío para usar el directorio actual)
            "Archivos de texto (*.txt);;Todos los archivos (*)"  # Filtros de archivo
        )

        # Verificar si se seleccionó un archivo
        if file_path:
            # Validar que el archivo tenga la extensión .txt
            if not file_path.endswith('.txt'):
                print("El archivo seleccionado no tiene la extensión .txt.")
                QMessageBox.warning(None, "Error de archivo", "Por favor, selecciona un archivo con extensión .txt.")
                return None

            print(f"Archivo seleccionado: {file_path}")
            return file_path
        else:
            print("No se seleccionó ningún archivo.")
            return None

    def run(self):
        """
        Initialize the view
        """
        self.view.run()