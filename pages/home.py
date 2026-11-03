from PySide6.QtWidgets import QWidget

from . import load_ui


class HomePage(QWidget):
    def __init__(self, go_to):
        super().__init__()
        self.ui = load_ui("home.ui", self)

        self.ui.chooseModelButton.clicked.connect(lambda: go_to("model"))
        self.ui.viewResultsButton.clicked.connect(lambda: go_to("results"))
