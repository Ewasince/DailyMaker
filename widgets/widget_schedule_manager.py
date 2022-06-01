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
    owner = None
    manager = Load_manager()

    def __init__(self, owner):
        self.owner = owner

    def setupUi(self):
        self.widget = my_calendar(self.owner)
        super().setupUi(self.widget)

        # TODO возможно нужно изменить минимальную дату
        self.widget.setMinimumDate(QDate(2022, 1, 1))
        self.widget.setMaximumDate(QDate(2022, 12, 31))

        # save_manager_ = Save_manager()
        self.comboBoxAddFilters.clear()
        self.fill_combo_box()
        self.comboBoxAddFilters.activated.connect(self.filter_events_by_tag)

        pass

    # Соответствует полю "поиск"
    def find_event_by_name(self):


        pass

    # Инициализация comboBox с фильтрами
    def fill_combo_box(self):
        self.comboBoxAddFilters.addItems(
            self.manager.get_unique_tags(self.widget.minimumDate(), self.widget.maximumDate()))
        pass

    # Фильтр событий
    # В параметры функции также требуется передавать текущий выбранный на календаре месяц
    def filter_events_by_tag(self):
        tag = self.comboBoxAddFilters.currentText()

        # Получение объектов событий за выбранный месяц
        events = self.manager.load_events(self.widget.minimumDate(), self.widget.maximumDate())

        dates = list()
        # Получение дат событий за выбранный месяц
        for event in events:
            if tag in event.tags:
                dates.append(QtCore.QDate.fromString(event.date, f"yyyy-MM-dd")) # TODO КОНВЕРТАЦИЯ DATE ИЗ СТРОКИ В QDATE

        #unique_dates = list(set(dates))

        #for date in unique_dates:
         #   print(date)

        #self.widget.specific_dates = QDate(unique_dates)
        pass

    # Очистка фильтров
    def remove_events(self):

        self.widget.specific_dates = None
        pass

    # Отображение в правой части экрана всех активностей за выбранный день
    def display_events_on_certain_day(self, day):

        pass
