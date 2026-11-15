"""
Tests for the results page

Checks that the results page loads with the correct title.
"""
from unittest.mock import MagicMock
from pages.results import ResultsPage


def test_title(qtbot):
    """Results page title reads "Results"."""
    mock_action = MagicMock()  # create a fake action to test with

    page = ResultsPage(go_to=mock_action)  # instantiate the page

    qtbot.addWidget(page)  # register the widget with qtbot

    assert page.ui.titleLabel.text() == "Results"  # title says Results
