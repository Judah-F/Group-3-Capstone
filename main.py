"""
Edge LLM Benchmark application entry point

Creates the main window and registers each page (home, model, settings,
results) in a QStackedWidget. Pages switch views by calling go_to()
with the name of the page to show.

Run with: python main.py
"""
import sys

from PySide6.QtWidgets import QApplication, QStackedWidget

from pages.home import HomePage
from pages.model import ModelPage
from pages.results import ResultsPage
from pages.settings import SettingsPage

app = QApplication(sys.argv)

window = QStackedWidget()  # shows one page at a time
window.setWindowTitle("Edge LLM Benchmark")
window.resize(800, 600)
pages = {}


def go_to(name):
    """Switch the window to the page with the given name.

    Args:
        name (str): Key of the page in the pages dict, e.g. "home".
    """
    if name in pages:
        window.setCurrentWidget(pages[name])


pages["home"] = HomePage(go_to)
pages["model"] = ModelPage(go_to)
pages["settings"] = SettingsPage(go_to)
pages["results"] = ResultsPage(go_to)

for page in pages.values():
    window.addWidget(page)

# Only show the window when run directly, so importing main in tests
# doesn't launch the UI and block the test run.
if __name__ == "__main__":
    go_to("home")
    window.show()
    sys.exit(app.exec())
