from unittest.mock import MagicMock
from pages.results import ResultsPage


def test_title(qtbot):

     mock_action = MagicMock() #creating a fake action to test 

     page = ResultsPage(go_to=mock_action) #instantiating page

     qtbot.addWidget(page) #creating a widget 

     assert page.ui.titleLabel.text()=="Results" #confirming text says results