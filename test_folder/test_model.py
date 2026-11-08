from unittest.mock import MagicMock
from pages.model import ModelPage


def test_model_page_navigation(qtbot):
    #creating fake function to track calls
    mock_go_to = MagicMock()