from widgets.widget_analytics import Ui_Form
from PyQt5 import QtWidgets
from db_manager import Load_manager


class Ui_Analytics(Ui_Form):
    widget = None
    owner = None

    def __init__(self, owner):
        self.owner = owner

    def show(self):
        self.widget.show()

    def hide(self):
        self.widget.hide()

    def setupUi(self):
        self.widget = QtWidgets.QWidget(self.owner)
        super().setupUi(self.widget)
