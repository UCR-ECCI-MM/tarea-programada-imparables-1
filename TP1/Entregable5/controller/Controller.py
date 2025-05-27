try: # Intento directo de importación
    from view.View import View #Linux
except ImportError:
    from Entregable5.view.View import View #Mac

try: 
    from model.Model import Model  # Import the model
except ImportError:
    from Entregable5.model.Model import Model #Mac

# from model.Model import Model
from PyQt5.QtWidgets import QVBoxLayout, QDialog, QMessageBox, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import os


class Controller:

    def __init__(self):
        """
        Initialize the view
        """
        self.view = View(self)  # Build the view and pass the controller as a parameter
        self.model = Model()  # Build the model
        print("Controller build!")
        self.TABLEDATA = None

    def handleButtonClick(self, action):
        """
        Handle the button click event based on the action.
        """
        print(f"Button clicked! Action: {action}")

        if action == 'startApp':
            self.view.switchToMainWindow()
        elif action == "GRAFICO":
            # ------------------------------------PROVISIONAL------------------------------------
            self.view.showLogLevelPieChart(self.TABLEDATA)
            # ------------------------------------PROVISIONAL------------------------------------
        elif action == "FUNCIONABILIDAD":
            # ------------------------------------PROVISIONAL------------------------------------
            log_levels = self.getLogLevels(self.TABLEDATA)
            self.exportToPDF(self.TABLEDATA, log_levels)
            # ------------------------------------PROVISIONAL------------------------------------
        # elif action == "analizar":
        #     self.dataAnalisis()
        elif action == "agregar":
            file_path = self.selectFile()
            self.view.switchToDashboard()
            self.TABLEDATA = self.parserDataToTable(self.dataAnalisis(file_path))
            self.view.populateTable(self.TABLEDATA)
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

        return parserData

        # for entry in parserData:
        #     entry_type = entry[0]
        #     entry_data = entry[1]
        #     entry_blocks = entry[2]

        #     print(f"\n\nTipo de entrada: {entry_type}")
        #     print("Datos principales:")
        #     for key, value in entry_data.items():
        #         print(f"  {key}: {value}")

        #     print("Bloques asociados:")
        #     for block in entry_blocks:
        #         block_type = block[0]
        #         block_data = block[1]

        #         print(f"  Tipo de bloque: {block_type}")
        #         if isinstance(block_data, list):  # Si el bloque contiene una lista
        #             for item in block_data:
        #                 print(f"    {item}")
        #         elif isinstance(block_data, dict):  # Si el bloque contiene un diccionario
        #             for key, value in block_data.items():
        #                 print(f"    {key}: {value}")
        #         else:
        #             print(f"    {block_data}")


        # ------------------------TEST THE LEXER------------------------
        # self.model.lexerAnalyze(file_path)
        # # Retrieve and print the lexical data
        # lexicalData = self.model.getLexicalData()
        # print("Lexical Data:")
        # for token in lexicalData:
        #     print(token)
    def getLogLevels(self, table_data):
        """
        Get the frequency of log levels from the table data.
        """
        log_levels = {}
        for row in table_data:
            level = row[0]  # El nivel de log está en la primera columna
            if level:
                log_levels[level] = log_levels.get(level, 0) + 1
        return log_levels

    def exportToPDF(self, table_data, log_levels):
        """
        Export the table and the pie chart to a PDF file with proper pagination.
        """
        if not table_data or not log_levels:
            QMessageBox.warning(self.view, "Advertencia", "No hay datos para exportar")
            return

        # Seleccionar el archivo de salida
        file_path, _ = QFileDialog.getSaveFileName(
            self.view,
            "Guardar PDF",
            "",
            "PDF Files (*.pdf)"
        )

        if not file_path:
            return

        if not file_path.endswith(".pdf"):
            file_path += ".pdf"

        # Configurar ruta absoluta para la imagen temporal
        temp_dir = os.path.join(os.getcwd(), "temp")
        os.makedirs(temp_dir, exist_ok=True)
        pie_chart_path = os.path.join(temp_dir, "pie_chart_temp.png")
        
        try:
            # Generar el gráfico
            self.savePieChart(log_levels, pie_chart_path)
            
            if not os.path.exists(pie_chart_path):
                raise FileNotFoundError(f"No se pudo crear el archivo {pie_chart_path}")

            # Configuración del documento
            doc = SimpleDocTemplate(
                file_path,
                pagesize=letter,
                leftMargin=50,
                rightMargin=50,
                topMargin=50,
                bottomMargin=50
            )
            
            # Estilos
            styles = getSampleStyleSheet()
            elements = []
            
            # Título del documento
            title = Paragraph("<b>Reporte de Logs</b>", styles['Title'])
            elements.append(title)
            elements.append(Spacer(1, 20))
            
            # Sección de la tabla
            elements.append(Paragraph("<b>Tabla de Logs:</b>", styles['Heading2']))
            elements.append(Spacer(1, 10))
            
            # Preparar datos de la tabla
            headers = ["Nivel", "Fecha", "Hora", "Nivel", "Número", "Mensaje"]
            data = [headers] + table_data
            
            # Crear tabla con anchos de columna ajustados
            col_widths = [60, 80, 60, 60, 60, 200]
            table = Table(data, colWidths=col_widths, repeatRows=1)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ]))
            
            elements.append(table)
            elements.append(Spacer(1, 20))
            
            # Sección del gráfico
            elements.append(Paragraph("<b>Distribución de Niveles de Log:</b>", styles['Heading2']))
            elements.append(Spacer(1, 10))
            
            # Añadir imagen del gráfico
            img = Image(pie_chart_path, width=400, height=300)
            elements.append(img)
            
            # Construir el documento
            doc.build(elements)
            QMessageBox.information(self.view, "Éxito", f"El reporte se ha guardado en {file_path}")
            
        except Exception as e:
            QMessageBox.critical(self.view, "Error", f"Ocurrió un error al generar el PDF: {str(e)}")
        finally:
            # Intentar eliminar el archivo temporal si existe
            try:
                if os.path.exists(pie_chart_path):
                    os.remove(pie_chart_path)
            except Exception as e:
                print(f"Error al eliminar archivo temporal: {e}")

    def savePieChart(self, log_levels, file_path):
        """
        Save the pie chart as an image file.
        """
        fig = Figure(figsize=(6, 5), dpi=100)
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)

        # Preparar datos para el gráfico
        labels = list(log_levels.keys())
        sizes = list(log_levels.values())

        # Colores para cada nivel (puedes personalizarlos)
        colors = {
            'ERROR': '#ff6b6b',
            'WARNING': '#ffd166',
            'INFO': '#06d6a0',
            'DEBUG': '#118ab2',
            'CRITICAL': '#ef476f'
        }

        # Asignar colores o usar colores por defecto
        color_list = [colors.get(level.upper(), '#888888') for level in labels]

        # Crear el gráfico de pastel
        ax.pie(
            sizes,
            labels=labels,
            autopct='%1.1f%%',
            startangle=90,
            colors=color_list,
            textprops={'fontsize': 10}
        )

        ax.set_title('Distribución de Niveles de Log', pad=20)
        ax.axis('equal')  # Para que el pastel sea circular

        # Guardar el gráfico como imagen
        fig.savefig(file_path)
        print(f"Gráfico guardado en: {file_path}")  # Depuración

    def parserDataToTable(self, parsed_data):
        """
        Convert the parsed data into a tabular format for QTableWidget.
        """
        table_data = []

        for entry in parsed_data:
            entry_type = entry[0]
            entry_data = entry[1]

            # Extraer datos principales de la entrada
            row = [
                entry_data.get('loglevel', ''),
                entry_data.get('date', ''),
                entry_data.get('time', ''),
                entry_data.get('loglevel', ''),
                entry_data.get('entry_number', ''),
                entry_data.get('entry_message', '')
            ]
            table_data.append(row)

        return table_data
    
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