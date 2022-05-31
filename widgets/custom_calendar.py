from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QDate

from plan_manager import plan_event
from db_manager import Load_manager

class my_calendar(QtWidgets.QCalendarWidget):

    def __init__(self, parent=None):
        QtWidgets.QCalendarWidget.__init__(self, parent)
        """
        load_manager = Load_manager()
        events = list()

        events = load_manager.load_events(QDate(2022, 5, 1), QDate(2022, 5, 31))
        
        if events is not None:
            for event in events:
                print(event.)
        """

    """
    def paintCell(self, painter, rect, date):
        current_month = QtWidgets.QCalendarWidget.monthShown(self)
        current_year = QtWidgets.QCalendarWidget.yearShown(self)
        highlighted_days = [1, 4, 20, 14, 5, 23, 31]
        needed_dates = []
        needed_dates = [QDate(current_year, current_month, 1),
                        QDate(current_year, current_month, 4),
                        QDate(current_year, current_month, 20),
                        QDate(current_year, current_month, 18),
                        QDate(current_year, current_month, 30)]
        for days in highlighted_days:
            needed_dates.append(QDate(current_year, current_month, days))
        load_manager = Load_manager()
        events = []
        events = load_manager.load_events(self, QDate(2022, 5, 1), QDate(2022, 5, 31))


        plan = plan_event()


        #QtWidgets.QCalendarWidget.paintCell(self, painter, rect, date)
        if date in :
            painter.setPen(QtGui.QPen(QtGui.QColor(0, 200, 200), 2, Qt.SolidLine, Qt.RoundCap))
            painter.drawLine(rect.topRight(), rect.topLeft())
            painter.drawLine(rect.topRight(), rect.bottomRight())
            painter.drawLine(rect.bottomLeft(), rect.bottomRight())
            painter.drawLine(rect.topLeft(), rect.bottomLeft())
    """