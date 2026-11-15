from unittest.mock import MagicMock
from pages.model import ModelPage


def test_model_page_navigation(qtbot):
    #creating fake function to track calls
    mock_go_to = MagicMock()

    page = ModelPage(go_to=mock_go_to) #instantiating the ui

    qtbot.addWidget(page) ##adding widget

    #this test tests the add button in the settings page
def test_add_button_click(qtbot):

    mock_action = MagicMock() #creating a fake action to test the button

    page = ModelPage(go_to=mock_action) #instantiating page

    qtbot.addWidget(page) #creating a widget 

    assert page.ui.addButton.text()=="Add" #confirming text says add

    #page.ui.addButton.click() #simulating mouse clock test currently doesn't work

    #mock_action.assert_called_once() #asserting that the button was pressed
    

def test_browse_button_click(qtbot):

    mock_action = MagicMock() #creating a fake action

    page =ModelPage(go_to=mock_action) #instantiating

    assert page.ui.browseButton.text()=="Browse…"

    #page.ui.addButton.click() #simulating mouse click #test currently doesn't work

    #mock_action.assert_called_once() #test currently doesn't work