from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QPushButton, QFileDialog, QTableWidgetItem, QWidget
from PyQt5.uic import loadUi
from PyQt5 import uic

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
            loadUi( 'Entregable4/view/welcomePage.ui' , self ) # Load from the UI file #Mac

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
            loadUi( 'Entregable4/view/mainWindow.ui' , self ) # Load from the UI file #Mac

        self.centerWindow() # Center the main window on the screen
        self.stackedWidget.addWidget(self.mainPage) # Add welcomePage to the stackedWidget
        self.stackedWidget.setCurrentWidget(self.mainPage) # set the welcomePage to the main window on the stackedWidget
        self.connectMenuActions() # Connect menu actions to controller methods
        self.connectButtons() # Connect buttons or other widgets to controller methods

    def switchToDashboard(self):
        """
        Switch to the dashboard window.
        """
        self.dashboardPage = QWidget()

        try: #Try to load the IU
            loadUi( 'view/dashboardWindow.ui' , self ) # Load from the UI file #Linux
        except:
            loadUi( 'Entregable4/view/dashboardWindow.ui' , self ) # Load from the UI file #Mac

        
        
        self.centerWindow() # Center the main window on the screen
        self.stackedWidget.addWidget(self.dashboardPage) # Add dashboardPage to the stackedWidget
        self.stackedWidget.setCurrentWidget(self.dashboardPage) # set the dashboardPage to the main window on the stackedWidget
        self.menuBar.setVisible(True)  # Show the menu bar

    def connectButtons(self):
        """
        Connect buttons to the controller's handleButtonClick method.
        """
        self.connectButton('startButton', 'startApp', 'clicked') # (butttonName, actionName, actionExecuted)
        self.connectButton('analizarButton', 'analizar', 'clicked') # (butttonName, actionName, actionExecuted)
        self.connectButton('agregarButton', 'agregar', 'clicked') # (butttonName, actionName, actionExecuted)

    def displayParsedData(self, parserData):
        """
        Display the parsed data in the dashboard view.
        :param parserData: List of parsed data entries
        """
        # Clear any existing items in the table
        if hasattr(self, 'dataTable'):
            self.dataTable.setRowCount(0)
            
            # Set up table columns
            self.dataTable.setColumnCount(3)
            self.dataTable.setHorizontalHeaderLabels(['Tipo', 'Datos', 'Bloques'])
            
            # Add data to the table
            for entry in parserData:
                entry_type = entry[0]
                entry_data = entry[1]
                entry_blocks = entry[2]
                
                # Create a row for each entry
                row = self.dataTable.rowCount()
                self.dataTable.insertRow(row)
                
                # Add type
                self.dataTable.setItem(row, 0, QTableWidgetItem(str(entry_type)))
                
                # Add data as formatted string
                data_str = '\n'.join([f"{k}: {v}" for k, v in entry_data.items()])
                self.dataTable.setItem(row, 1, QTableWidgetItem(data_str))
                
                # Add blocks as formatted string
                blocks_str = '\n'.join([f"{block[0]}: {block[1]}" for block in entry_blocks])
                self.dataTable.setItem(row, 2, QTableWidgetItem(blocks_str))
                
                # Adjust row height to fit content
                self.dataTable.resizeRowToContents(row)
            
            # Adjust column widths
            self.dataTable.resizeColumnsToContents()
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

    #
    # Center the main window on the screen
    #
    def centerWindow(self):
        screen = QApplication.primaryScreen().availableGeometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen.center())
        self.move(window_geometry.topLeft())

    def displayParsedData(self, parserData):
        """
        Display the parsed data in the dashboard view.
        :param parserData: List of parsed data entries
        """
        # Clear any existing items in the table
        if hasattr(self, 'dataTable'):
            self.dataTable.setRowCount(0)
            
            # Set up table columns
            self.dataTable.setColumnCount(3)
            self.dataTable.setHorizontalHeaderLabels(['Tipo', 'Datos', 'Bloques'])
            
            # Add data to the table
            for entry in parserData:
                entry_type = entry[0]
                entry_data = entry[1]
                entry_blocks = entry[2]
                
                # Create a row for each entry
                row = self.dataTable.rowCount()
                self.dataTable.insertRow(row)
                
                # Add type
                self.dataTable.setItem(row, 0, QTableWidgetItem(str(entry_type)))
                
                # Add data as formatted string
                data_str = '\n'.join([f"{k}: {v}" for k, v in entry_data.items()])
                self.dataTable.setItem(row, 1, QTableWidgetItem(data_str))
                
                # Add blocks as formatted string
                blocks_str = '\n'.join([f"{block[0]}: {block[1]}" for block in entry_blocks])
                self.dataTable.setItem(row, 2, QTableWidgetItem(blocks_str))
                
                # Adjust row height to fit content
                self.dataTable.resizeRowToContents(row)
            
            # Adjust column widths
            self.dataTable.resizeColumnsToContents()

    def run(self):
        self.show()