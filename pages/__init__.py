"""
Shared helpers for the GUI pages

Provides load_ui(), which loads a Qt Designer .ui file from the ui/
folder at runtime and embeds it inside a page widget.
"""
from pathlib import Path

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QVBoxLayout

UI_FOLDER = Path(__file__).parent.parent / "ui"


def load_ui(filename, page):
    """Load a Qt Designer .ui file and embed it inside a page.

    Args:
        filename (str): Name of the .ui file in the ui/ folder.
        page (QWidget): Page widget the loaded UI is placed inside.

    Returns:
        QWidget: The loaded UI, used to access its child widgets.
    """
    ui = QUiLoader().load(str(UI_FOLDER / filename))
    layout = QVBoxLayout(page)
    layout.setContentsMargins(0, 0, 0, 0)
    layout.addWidget(ui)
    return ui
