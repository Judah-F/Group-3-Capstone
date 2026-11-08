from main import go_to, window, pages

def test_main_routing(qtbot):
    qtbot.addWidget(window) #this will add the main window to qtbot

    go_to("model") #this will simulate routing to the model page

    assert window.currentWidget() ==pages["model"] #asserting that the currently visible widget is the modelPage

    go_to("settings") #simulating routing to the settings page

    assert window.currentWidget() ==pages["settings"] #asserting that the visible widget actually changed to settings page

