from main import go_to, window, pages

def test_main_routing(qtbot):
    qtbot.addWidget(window) #this will add the main window to qtbot

    go_to("model") #this will simulate routing to the model page

    assert window.currentWidget() ==pages["model"] #asserting that the currently visible widget is the modelPage

    go_to("settings") #simulating routing to the settings page

    assert window.currentWidget() ==pages["settings"] #asserting that the visible widget actually changed to settings page


def test_add_button_click(qtbot):

    mock_action = MagicMock() #creating a fake action to test the button

    page = SettingsPage(go_to=mock_action) #instantiating page

    qtbot.addWidget(page) #creating a widget 

    assert page.ui.addButton.text()=="Add" #confirming text says add

    page.ui.addButton.click() #simulating mouse clock

    mock_action.assert_called_once() #asserting that the button was pressed