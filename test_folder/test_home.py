from unittest.mock import MagicMock
from pages.home import HomePage
#For these tests being UI we're using MagicMock to immitate a ui 
#
def test_home_page_navigation(qtbot):
    #creating a fake function for the purpose of testing the ui
        mock_go_to =MagicMock()


#instantiating the ui while passing in this fake function
        page = HomePage(go_to=mock_go_to) #

        qtbot.addWidget(page) #adding a widget to qbot

        page.ui.chooseModelButton.click() #simulating a user clicking the choose model button


        mock_go_to.assert_called_once_with("model") # asserting that this fake function gets called with model

        mock_go_to.reset_mock() #resetting mock function

        page.ui.viewResultsButton.click() #testking view results button

        mock_go_to.assert_called_once_with("results") #asserting that fake function was called with results
       


