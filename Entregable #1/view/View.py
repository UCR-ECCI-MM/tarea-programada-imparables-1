from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QPushButton, QFileDialog, QTableWidgetItem
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
        loadUi( 'Entregable #1/view/mainWindow.ui' , self )  # Load mainWindow.ui, designed in Qt Designer
        self.centerWindow() # Center the main window on the screen
        self.welcomePage = QMainWindow() #Initiate the landingPage first, so the landingPage now gonna be a main window
        loadUi( 'Entregable #1/view/welcomePage.ui' , self ) # Load from the UI file
        self.menuBar.setVisible(False) # Hide the menu bar initially (since we start on the welcome page)
        self.connectButtons() # Connect buttons or other widgets to controller methods

    def connectButtons(self):
        """
        Connect buttons to the controller's handleButtonClick method, passing the button name as a parameter.
        """
        self.connectButton('startButton', 'startApp') # (butttonName, actionName)

    def connectButton(self, buttonName, action):
        """
        Connect a button to the controller's handleButtonClick method, passing the action as a parameter.
        """
        if hasattr(self, buttonName):
            button = getattr(self, buttonName)
            button.clicked.connect(lambda: self.controller.handleButtonClick(action))

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