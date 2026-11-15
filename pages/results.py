"""
Results page of the Edge LLM Benchmark GUI

Displays benchmark results and lets the user return home or start a
new benchmark.
"""
from PySide6.QtWidgets import QWidget

from . import load_ui


class ResultsPage(QWidget):
    """Page that displays benchmark results."""
    def __init__(self, go_to):
        """Load the results UI and connect its navigation buttons.

        Args:
            go_to (callable): Function that switches to a page by name.
        """
        super().__init__()
        self.ui = load_ui("results.ui", self)

        self.ui.homeButton.clicked.connect(lambda: go_to("home"))
        self.ui.newBenchmarkButton.clicked.connect(lambda: go_to("model"))
