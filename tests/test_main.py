"""
Tests for the main application window

Checks that go_to() switches the visible page in the stacked widget.
"""
from main import go_to, window, pages


def test_main_routing(qtbot):
    """go_to() changes the visible page in the main window."""
    qtbot.addWidget(window)  # add the main window to qtbot

    go_to("model")  # simulate routing to the model page

    # the visible widget should now be the model page
    assert window.currentWidget() == pages["model"]

    go_to("settings")  # simulate routing to the settings page

    # the visible widget should have changed to the settings page
    assert window.currentWidget() == pages["settings"]
