from view.View import View
# from model.Model import Model

class Controller:

    #
    # Constructor of Controller
    #
    def __init__(self):
        """
        Initialize the view
        """
        self.view = View(self)  # Build the view and pass the controller as a parameter
        print("Controller build!")

    #
    # Controller logic
    #
    def run(self):
        """
        # Inicia la vista.
        """
        self.view.run()
        