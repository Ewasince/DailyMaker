from widgets.widget_schedule import Ui_Form
from PyQt5 import QtWidgets
import db_manager
from db_manager import load_manager, save_manager

class Ui_Schedule(Ui_Form):
    widget = None
    owner = None

    def __init__(self, owner):
        self.owner = owner

    def setupUi(self):
        self.widget = QtWidgets.QWidget(self.owner)
        super().setupUi(self.widget)

        from PyQt5.QtCore import QDate
        from PyQt5.QtCore import QTime

        # save_manager_ = save_manager()

        manager = load_manager()
        date_from = QDate(2022, 5, 28)
        date_to = QDate(2022, 5, 31)
        time_from = QTime(0, 0)
        time_to = QTime(23, 59)
        manager.load_events(date_from, date_to, time_from, time_to)

