"""
Benchmark settings page of the Edge LLM Benchmark GUI

Lets the user choose benchmark settings before starting a run. The
custom settings group is only enabled when "Custom" mode is selected.
"""
from PySide6.QtWidgets import QWidget

from . import load_ui


class SettingsPage(QWidget):
    def __init__(self, go_to):
        super().__init__()
        self.ui = load_ui("settings.ui", self)

        self.ui.backButton.clicked.connect(lambda: go_to("model"))
        self.ui.startButton.clicked.connect(lambda: go_to("results"))

        # Custom settings can only be edited when "Custom" mode is picked
        self.ui.customRadio.toggled.connect(self.ui.customGroup.setEnabled)
