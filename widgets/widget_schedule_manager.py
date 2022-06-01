import datetime

from PyQt5.QtCore import QDate
from PyQt5.uic.properties import QtCore

from widgets.widget_schedule import Ui_Form
from PyQt5 import QtWidgets
import db_manager
from db_manager import Load_manager, Save_manager
import datetime
from widgets.custom_calendar import my_calendar
from PyQt5.QtCore import QDate, QTime
from plan_manager import plan_event


class Ui_Schedule(Ui_Form):
    widget = None
    calendar_widget = None
    owner = None
    manager = Load_manager()
    events: [plan_event] = list()
    activity_buttons = list()

    def __init__(self, owner):
        self.owner = owner

    def setupUi(self):
        self.widget = QtWidgets.QWidget(self.owner)
        # self.widget = my_calendar(self.owner):
        super().setupUi(self.widget)
        self.calendar_widget = self.calendarWidget

        # TODO возможно нужно изменить минимальную дату
        self.calendar_widget.setMinimumDate(QDate(2022, 1, 1))
        self.calendar_widget.setMaximumDate(QDate(2022, 12, 31))

        self.events = self.manager.load_events(self.calendar_widget.minimumDate(), self.calendar_widget.maximumDate())
        # self.events[0].

        # save_manager_ = Save_manager()
        self.comboBoxAddFilters.clear()
        self.comboBoxAddFilters.setEditable(False)
        self.fill_combo_box()
        self.comboBoxAddFilters.activated.connect(self.filter_events_by_tag)

        self.initialize_activity_buttons()

        self.calendar_widget.clicked.connect(self.event_calendar_clicked)


        pass

    def event_calendar_clicked(self, day):
        self.display_events_on_certain_day(day)
        pass


    def initialize_activity_buttons(self):
        self.activity_buttons.append(self.pushButtonActivity_1)
        self.activity_buttons.append(self.pushButtonActivity_2)
        self.activity_buttons.append(self.pushButtonActivity_3)
        self.activity_buttons.append(self.pushButtonActivity_4)
        self.activity_buttons.append(self.pushButtonActivity_5)
        self.activity_buttons.append(self.pushButtonActivity_6)
        self.activity_buttons.append(self.pushButtonActivity_7)
        self.activity_buttons.append(self.pushButtonActivity_8)

    # Соответствует полю "поиск"
    def find_event_by_name(self):

        pass

    # Инициализация comboBox с фильтрами
    def fill_combo_box(self):
        self.comboBoxAddFilters.addItems(
            self.manager.get_unique_tags(self.calendar_widget.minimumDate(), self.calendar_widget.maximumDate()))
        pass

    # Фильтр событий
    # В параметры функции также требуется передавать текущий выбранный на календаре месяц
    def filter_events_by_tag(self):
        tag = self.comboBoxAddFilters.currentText()

        dates = list()
        # Получение дат событий за выбранный месяц
        for event in self.events:
            if tag in event.tags:
                dates.append(event.date)

        unique_dates = list(set(dates))

        self.calendar_widget.specific_dates = unique_dates
        pass

    # Очистка фильтров
    def remove_events(self):

        self.calendar_widget.specific_dates = None
        pass

    # Отображение в правой части экрана всех активностей за выбранный день
    def display_events_on_certain_day(self, date: QDate):
        certain_events = list()
        event: plan_event
        for event in self.events:
            if compare_dates(event.date, date):
                certain_events.append(event)
        self.display_events(certain_events)

        pass

    def display_events(self, target_events):
        n = 0
        from PyQt5.QtWidgets import QPushButton
        but: QPushButton
        for but in self.activity_buttons:
            but.hide()

        event: plan_event
        for event in target_events:
            but = self.activity_buttons[n]
            but.setText(event.name + '\n' + f"{event.time_from.toString()}={event.time_to.toString()}")
            but.show()
            n += 1


def compare_dates(date1: QDate, date2: QDate):
    cond1 = date1.year() == date2.year()
    cond2 = date1.month() == date2.month()
    cond3 = date1.day() == date2.day()
    return cond1 and cond2 and cond3
