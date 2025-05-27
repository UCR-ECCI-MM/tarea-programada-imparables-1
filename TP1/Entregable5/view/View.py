from PyQt5.QtWidgets import (QMainWindow, QApplication, QFileDialog, 
                            QPushButton, QFileDialog, QTableWidgetItem, 
                            QWidget, QTableWidget, QHeaderView, QDialog, 
                            QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, 
                            QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.uic import loadUi
from PyQt5 import uic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class View(QMainWindow):

    #
    # Constructor method with it self and controller class
    #
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.initUI()  # Initialize the User Interface

    #
    # UI initializer method
    #
    def initUI(self):
        """
        Initialize the view of the app, the welcom screen
        """
        self.welcomePage = QWidget() #Initiate the landingPage first, so the landingPage now gonna be a main window

        try: #Try to load the IU
            loadUi( 'view/welcomePage.ui' , self ) # Load from the UI file #Linux
        except:
            loadUi( 'Entregable5/view/welcomePage.ui' , self ) # Load from the UI file #Mac

        self.centerWindow() # Center the main window on the screen
        self.stackedWidget.addWidget(self.welcomePage) # Add welcomePage to the stackedWidget
        self.stackedWidget.setCurrentWidget(self.welcomePage) # set the welcomePage to the main window on the stackedWidget
        self.connectButtons() # Connect buttons or other widgets to controller methods

    def switchToMainWindow(self):
        """
        Switch to the main window and show the menu bar.
        """
        self.mainPage = QWidget() #Initiate the landingPage first, so the landingPage now gonna be a main window

        try: #Try to load the IU
            loadUi( 'view/mainWindow.ui' , self ) # Load from the UI file #Linux
        except:
            loadUi( 'Entregable5/view/mainWindow.ui' , self ) # Load from the UI file #Mac

        self.centerWindow() # Center the main window on the screen
        self.stackedWidget.addWidget(self.mainPage) # Add welcomePage to the stackedWidget
        self.stackedWidget.setCurrentWidget(self.mainPage) # set the welcomePage to the main window on the stackedWidget
        self.connectButtons() # Connect buttons or other widgets to controller methods

    def filterTable(self, text):
        """
        Filter the rows of the QTableWidget based on the search text.
        """
        for row in range(self.tableWidget.rowCount()):
            match = False
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item and text.lower() in item.text().lower():
                    match = True
                    break
            self.tableWidget.setRowHidden(row, not match)

    def switchToDashboard(self):
        """
        Switch to the dashboard window.
        """
        self.dashboardPage = QWidget()

        try: #Try to load the IU
            loadUi( 'view/dashboardWindow.ui' , self ) # Load from the UI file #Linux
        except:
            loadUi( 'Entregable5/view/dashboardWindow.ui' , self ) # Load from the UI file #Mac
        
        self.centerWindow() # Center the main window on the screen
        # Conectar la barra de búsqueda al método filterTable
        self.searchBar.textChanged.connect(self.filterTable)

        self.connectMenuActions()

    def populateTable(self, data):
        """
        Populate the QTableWidget with styled data.
        """
        if not data or len(data) == 0:
            return
        
        # Configuración básica de la tabla
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))
        
        # Encabezados personalizados
        headers = ["Nivel de Log", "Fecha", "Hora", "Nivel", "Número", "Mensaje"]
        self.tableWidget.setHorizontalHeaderLabels(headers)
        
        # Aplicar estilos a la tabla
        self.tableWidget.setStyleSheet("""
            QTableWidget {
                background-color: #f8f9fa;
                alternate-background-color: #e9ecef;
                gridline-color: #dee2e6;
                border: 1px solid #ced4da;
                border-radius: 8px;
                font-family: 'Segoe UI', sans-serif;
            }
            QTableWidget::item {
                padding: 8px;
                border-bottom: 1px solid #dee2e6;
            }
            QTableWidget::item:selected {
                background-color: #007bff;
                color: white;
            }
            QHeaderView::section {
                background-color: #343a40;
                color: white;
                padding: 8px;
                border: none;
                font-weight: bold;
            }
            QTableCornerButton::section {
                background-color: #343a40;
                border: none;
            }
        """)
        
        # Configuraciones adicionales
        self.tableWidget.verticalHeader().setVisible(False)  # Ocultar números de fila
        self.tableWidget.setAlternatingRowColors(True)  # Filas alternas de diferente color
        self.tableWidget.setShowGrid(False)  # Ocultar líneas de la cuadrícula
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)  # Seleccionar filas completas
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)  # Deshabilitar edición
        
        # Ajustar el tamaño de las columnas
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Interactive)
        header.setStretchLastSection(True)
        
        # Agregar los datos con estilo condicional
        for row_idx, row_data in enumerate(data):
            for col_idx, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                
                # Estilo condicional basado en el nivel de log
                if col_idx == 0:  # Columna de nivel de log
                    log_level = str(col_data).lower()
                    if 'error' in log_level:
                        item.setBackground(QColor('#ffdddd'))
                        item.setForeground(QColor('#721c24'))
                    elif 'warning' in log_level:
                        item.setBackground(QColor('#fff3cd'))
                        item.setForeground(QColor('#856404'))
                    elif 'success' in log_level or 'ok' in log_level:
                        item.setBackground(QColor('#d4edda'))
                        item.setForeground(QColor('#155724'))
                
                # Alineación del texto
                if col_idx in [3, 4]:  # Columnas numéricas
                    item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                else:
                    item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                
                self.tableWidget.setItem(row_idx, col_idx, item)
        
        # Ajustar automáticamente el tamaño de las columnas al contenido
        self.tableWidget.resizeColumnsToContents()
        
        # Añadir tooltips a las celdas
        self.tableWidget.itemClicked.connect(self.handleCellClick)

    def handleCellClick(self, item):
        """
        Handle clicks on the QTableWidget.
        """
        row = item.row()
        cell_data = item.text()
        print(f"Celda clicada: Fila {row}, Datos: {cell_data}")

        # Obtener los datos de la fila seleccionada
        log_data = self.getLogData(row)

        # Mostrar la ventana de detalles
        self.showLogDetails(log_data)

    def getLogData(self, row):
        """
        Get the log data for the selected row.
        """
        log_data = {}
        headers = ["Nivel de Log", "Fecha", "Hora", "Nivel", "Número", "Mensaje"]

        for col in range(self.tableWidget.columnCount()):
            header = headers[col]
            value = self.tableWidget.item(row, col).text()
            log_data[header] = value

        return log_data

    def showLogDetails(self, log_data):
        """
        Show a dialog with the details of the selected log.
        """
        # Crear un QDialog directamente
        dialog = QDialog(self)
        dialog.setWindowTitle("Detalles del Log")
        dialog.setMinimumSize(400, 300)

        # Crear un diseño vertical para el contenido
        layout = QVBoxLayout()

        # Agregar etiquetas con la información del log
        for key, value in log_data.items():
            label = QLabel(f"<b>{key}:</b> {value}")
            layout.addWidget(label)

        # Configurar el diseño en el QDialog
        dialog.setLayout(layout)

        # Mostrar el diálogo de forma modal
        dialog.exec_()

    def connectButtons(self):
        """
        Connect buttons to the controller's handleButtonClick method.
        """
        self.connectButton('startButton', 'startApp', 'clicked') # (butttonName, actionName, actionExecuted)
        self.connectButton('agregarButton', 'agregar', 'clicked') # (butttonName, actionName, actionExecuted)

    def connectMenuActions(self):
        """
        Connect menu actions to the controller's handleButtonClick method.
        """
        self.connectButton('actionGraficos', 'GRAFICO', 'triggered') #(butttonName, actionName, actionExecuted)
        self.connectButton('actionfuncionabilidadPrueba', 'FUNCIONABILIDAD', 'triggered')

    def connectButton(self, widgetName, action, signal):
        """
        Connect a widget (button or menu action) to the controller's handleButtonClick method, passing the action as a parameter.
        :param widgetName: Name of the widget (button or menu action).
        :param action: Action to pass to the controller.
        :param signal: Signal to connect (e.g., 'clicked' for buttons, 'triggered' for menu actions).
        """
        if hasattr(self, widgetName):
            widget = getattr(self, widgetName)
            if signal == 'clicked':
                widget.clicked.connect(lambda: self.controller.handleButtonClick(action))
            elif signal == 'triggered':
                widget.triggered.connect(lambda: self.controller.handleButtonClick(action))
            else:
                print(f"Unsupported signal: {signal}")
    
    def showLogLevelPieChart(self, table_data):
        """
        Muestra un gráfico de pastel con la distribución de niveles de log.
        """
        if not table_data:
            return

        # Contar la frecuencia de cada nivel de log
        log_levels = {}
        for row in table_data:
            level = row[0]  # El nivel de log está en la primera columna
            if level:
                log_levels[level] = log_levels.get(level, 0) + 1
        
        if not log_levels:
            QMessageBox.information(self, "Información", "No se encontraron datos de niveles de log.")
            return
        
        # Crear el diálogo para el gráfico
        pie_dialog = QDialog(self)
        pie_dialog.setWindowTitle("Distribución de Niveles de Log")
        pie_dialog.setGeometry(100, 100, 600, 500)
        
        layout = QVBoxLayout()
        
        # Crear figura de matplotlib
        fig = Figure(figsize=(6, 5), dpi=100)
        canvas = FigureCanvas(fig)
        
        # Crear el gráfico de pastel
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
        wedges, texts, autotexts = ax.pie(
            sizes, 
            labels=labels, 
            autopct='%1.1f%%',
            startangle=90,
            colors=color_list,
            textprops={'fontsize': 10}
        )
        
        # Mejorar la legibilidad
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        
        ax.set_title('Distribución de Niveles de Log', pad=20)
        ax.axis('equal')  # Para que el pastel sea circular
        
        # Añadir leyenda
        ax.legend(
            wedges,
            labels,
            title="Niveles de Log",
            loc="center left",
            bbox_to_anchor=(1, 0, 0.5, 1)
        )
        
        # Añadir el canvas al layout
        layout.addWidget(canvas)
        pie_dialog.setLayout(layout)
        
        # Mostrar el diálogo
        pie_dialog.exec_()

    def centerWindow(self):
        screen = QApplication.primaryScreen().availableGeometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen.center())
        self.move(window_geometry.topLeft())

    def run(self):
        self.show()