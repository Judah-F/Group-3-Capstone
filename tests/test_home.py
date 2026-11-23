"""
Tests for the home page

Checks that the home page buttons route to the correct pages.
"""
from unittest.mock import MagicMock
from pages.home import HomePage

# These are UI tests, so MagicMock stands in for the real go_to function


def test_home_page_navigation(qtbot):
    """Home buttons route to the model and results pages."""
    # create a fake go_to function to track which page is requested
    mock_go_to = MagicMock()

    # instantiate the page, passing in the fake function
    page = HomePage(go_to=mock_go_to)

    qtbot.addWidget(page)  # register the widget with qtbot

    # simulate a user clicking the choose model button
    page.ui.chooseModelButton.click()

    # the fake function should be called with "model"
    mock_go_to.assert_called_once_with("model")

    mock_go_to.reset_mock()  # reset the mock between checks

    page.ui.viewResultsButton.click()  # test the view results button

    # the fake function should be called with "results"
    mock_go_to.assert_called_once_with("results")
