from main import go_to, window, pages

def test_main_routing(qtbot):
    qtbot.addWidget(window)

    go_to("model")