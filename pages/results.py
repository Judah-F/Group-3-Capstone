from PySide6.QtWidgets import QWidget

from . import load_ui


class ResultsPage(QWidget):
    def __init__(self, go_to):
        super().__init__()
        self.ui = load_ui("results.ui", self)

        self.ui.homeButton.clicked.connect(lambda: go_to("home"))
        self.ui.newBenchmarkButton.clicked.connect(lambda: go_to("model"))
