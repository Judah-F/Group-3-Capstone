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
    """Switch to another page by name."""
    if name in pages:
        window.setCurrentWidget(pages[name])


pages["home"] = HomePage(go_to)
pages["model"] = ModelPage(go_to)
pages["settings"] = SettingsPage(go_to)
pages["results"] = ResultsPage(go_to)

for page in pages.values():
    window.addWidget(page)

go_to("home")
window.show()
sys.exit(app.exec())
