from view.View import View
# from model.Model import Model

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
        elif action == 'action2':
            self.handleAction2()
        elif action == 'openFile':
            self.handleOpenFile()
        else:
            print("Unknown action!")

    def run(self):
        """
        Initialize the view
        """
        self.view.run()