from PySide6.QtWidgets import QWidget

from . import load_ui


class ModelPage(QWidget):
    def __init__(self, go_to):
        super().__init__()
        self.ui = load_ui("model.ui", self)

        self.ui.backButton.clicked.connect(lambda: go_to("home"))
        self.ui.nextButton.clicked.connect(lambda: go_to("settings"))
