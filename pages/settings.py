from PySide6.QtWidgets import QWidget

from . import load_ui


class SettingsPage(QWidget):
    def __init__(self, go_to):
        super().__init__()
        self.ui = load_ui("settings.ui", self)

        self.ui.backButton.clicked.connect(lambda: go_to("model"))
        self.ui.startButton.clicked.connect(lambda: go_to("results"))
