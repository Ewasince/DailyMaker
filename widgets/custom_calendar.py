from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QDate

from plan_manager import plan_event
from db_manager import Load_manager

class my_calendar(QtWidgets.QCalendarWidget):
    specific_dates = None

    def __init__(self, parent=None):
        QtWidgets.QCalendarWidget.__init__(self, parent)

    def paintCell(self, painter, rect, date):
        if self.specific_dates is not None and date in self.specific_dates:
            painter.setPen(QtGui.QPen(QtGui.QColor(0, 200, 200), 2, Qt.SolidLine, Qt.RoundCap))
            painter.drawLine(rect.topRight(), rect.topLeft())
            painter.drawLine(rect.topRight(), rect.bottomRight())
            painter.drawLine(rect.bottomLeft(), rect.bottomRight())
            painter.drawLine(rect.topLeft(), rect.bottomLeft())