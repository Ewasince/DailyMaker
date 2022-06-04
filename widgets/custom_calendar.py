from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QCalendarWidget

class Calendar_manager:
    calendar_widget = None
    selected_dates = None

def paintCell(painter, rect, date):
    QtWidgets.QCalendarWidget.paintCell(Calendar_manager.calendar_widget, painter, rect, date)
    selected_dates = None
    if Calendar_manager.selected_dates is not None and date in Calendar_manager.selected_dates:
        painter.setBrush(QtGui.QColor(0, 200, 200, 50))
        painter.setPen(QtGui.QColor(0, 0, 0, 0))
        painter.drawRect(rect)
    pass
