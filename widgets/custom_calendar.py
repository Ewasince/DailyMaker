from PyQt5 import QtGui, QtWidgets


class my_calendar(QtWidgets.QCalendarWidget):
    specific_dates = None

    def __init__(self, parent=None):
        QtWidgets.QCalendarWidget.__init__(self, parent)

    def paintCell(self, painter, rect, date):
        QtWidgets.QCalendarWidget.paintCell(self, painter, rect, date)

        if self.specific_dates is not None and date in self.specific_dates:
            painter.setBrush(QtGui.QColor(0, 200, 200, 50))
            painter.setPen(QtGui.QColor(0, 0, 0, 0))
            painter.drawRect(rect)
