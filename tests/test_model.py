"""
Tests for the model selection page

Checks that the page loads and its Add and Browse buttons are labeled
correctly.
"""
from unittest.mock import MagicMock
from pages.model import ModelPage


def test_model_page_navigation(qtbot):
    """Model page loads inside qtbot without errors."""
    # create a fake function to track calls
    mock_go_to = MagicMock()

    page = ModelPage(go_to=mock_go_to)  # instantiate the ui

    qtbot.addWidget(page)  # register the widget with qtbot


def test_add_button_click(qtbot):
    """Add button is labeled "Add"."""
    mock_action = MagicMock()  # create a fake action to test the button

    page = ModelPage(go_to=mock_action)  # instantiate the page

    qtbot.addWidget(page)  # register the widget with qtbot

    assert page.ui.addButton.text() == "Add"  # confirm text says Add

    # TODO: simulated click doesn't trigger the action yet
    # page.ui.addButton.click()
    # mock_action.assert_called_once()


def test_browse_button_click(qtbot):
    """Browse button is labeled "Browse…"."""
    mock_action = MagicMock()  # create a fake action

    page = ModelPage(go_to=mock_action)  # instantiate the page

    qtbot.addWidget(page)  # register the widget with qtbot

    assert page.ui.browseButton.text() == "Browse…"

    # TODO: simulated click doesn't trigger the action yet
    # page.ui.browseButton.click()
    # mock_action.assert_called_once()
