from pathlib import Path

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QVBoxLayout

UI_FOLDER = Path(__file__).parent.parent / "ui"


def load_ui(filename, page):
    """Load ui/<filename> (made in Qt Designer) and place it inside `page`."""
    ui = QUiLoader().load(str(UI_FOLDER / filename))
    layout = QVBoxLayout(page)
    layout.setContentsMargins(0, 0, 0, 0)
    layout.addWidget(ui)
    return ui
