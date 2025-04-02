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
        loadUi( 'Entregable1/view/welcomePage.ui' , self ) # Load from the UI file
        self.centerWindow() # Center the main window on the screen
        self.stackedWidget.addWidget(self.welcomePage) # Add welcomePage to the stackedWidget
        self.stackedWidget.setCurrentWidget(self.welcomePage) # set the welcomePage to the main window on the stackedWidget
        self.connectButtons() # Connect buttons or other widgets to controller methods

    def switchToMainWindow(self):
        """
        Switch to the main window and show the menu bar.
        """
        self.mainPage = QWidget() #Initiate the landingPage first, so the landingPage now gonna be a main window
        loadUi( 'Entregable1/view/mainWindow.ui' , self ) # Load from the UI file
        self.centerWindow() # Center the main window on the screen
        self.stackedWidget.addWidget(self.mainPage) # Add welcomePage to the stackedWidget
        self.stackedWidget.setCurrentWidget(self.mainPage) # set the welcomePage to the main window on the stackedWidget
        self.menuBar.setVisible(True)  # Show the menu bar
        self.connectMenuActions() # Connect menu actions to controller methods

    def connectButtons(self):
        """
        Connect buttons to the controller's handleButtonClick method.
        """
        self.connectButton('startButton', 'startApp', 'clicked') # (butttonName, actionName, actionExecuted)

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

    def run(self):
        self.show()