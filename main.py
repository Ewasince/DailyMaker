from main_window import Ui_MainWindow

from widgets.widget_schedule_manager import Ui_Schedule
from widgets.widget_add_manager import Ui_Add
from widgets.widget_analytics_manager import Ui_Analytics

from widgets import custom_calendar

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication


class Ui_MainWindow_cover(Ui_MainWindow):
    widgets_array = []
    calendar_widget = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)

        parent_widget = self.widget_parent

        self.widget_schedule = Ui_Schedule(parent_widget)
        self.widgets_array.append(self.widget_schedule)
        self.setup_widget(self.widget_schedule, "widget_schedule")
        self.widget_schedule.widget.show()
        self.widget_schedule.calendarWidget.paintCell = lambda *n: print(n)
        custom_calendar.Calendar_manager.calendar_widget = self.widget_schedule.calendarWidget
        self.widget_schedule.calendarWidget.paintCell = custom_calendar.paintCell

        self.widget_add = Ui_Add(parent_widget)
        self.widgets_array.append(self.widget_add)
        self.setup_widget(self.widget_add, "widget_add")

        self.widget_analytics = Ui_Analytics(parent_widget)
        self.widgets_array.append(self.widget_analytics)
        self.setup_widget(self.widget_analytics, "widget_analytics")

        self.pushButton_analytics.hide()
        self.add_functions()

    def setup_widget(self, custom_widget, name):
        custom_widget.setupUi()
        widget = custom_widget.widget
        widget.setGeometry(QtCore.QRect(0, 0, 1131, 631))
        widget.setObjectName(name)
        widget.hide()

    def add_functions(self):
        self.pushButton_schedule.clicked.connect(lambda: self.visible_widget(self.widget_schedule))
        self.pushButton_add.clicked.connect(lambda: self.visible_widget(self.widget_add))
        self.pushButton_analytics.clicked.connect(lambda: self.visible_widget(self.widget_analytics))

    def visible_widget(self, target_widget):
        for item in self.widgets_array:
            if item == target_widget:
                item.show()
            else:
                item.hide()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow_cover()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
