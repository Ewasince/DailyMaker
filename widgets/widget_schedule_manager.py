import datetime

from PyQt5.QtCore import QDate

from widgets.widget_schedule import Ui_Form
from PyQt5 import QtWidgets
import db_manager
from db_manager import Load_manager, Save_manager
import datetime
from widgets.custom_calendar import my_calendar
from PyQt5.QtCore import QDate
from plan_manager import plan_event


class Ui_Schedule(Ui_Form):
    widget = None
    owner = None

    def __init__(self, owner):
        self.owner = owner

    def setupUi(self):
        self.widget = my_calendar(self.owner)
        super().setupUi(self.widget)


        #self.comboBoxAddFilters.addItems(list1)


        from PyQt5.QtCore import QDate
        from PyQt5.QtCore import QTime

        save_manager_ = Save_manager()

        manager = Load_manager()
        date_from = QDate(2022, 1, 1)
        date_to = QDate(2022, 12, 31)
        events = list()
        events.extend(manager.load_events(date_from, date_to))
        tags = list()

        for event in events:
            print(event.tags)
            tags.append(event.tags)
            #for list_of_tags in event.tags:


        unique_tags = list(set(tags))
        print("unique tags = ", unique_tags)
        print("tags = ", tags)

        pass

    def get_events(self):
        load_manager = Load_manager()
        load_manager.load_events(load_manager, QDate(2022, 5, 1), QDate(2022, 5, 31))

    # Соответствует полю "поиск"
    def find_event_by_name(self):

        pass


    # Инициализация comboBox с фильтрами
    def fill_combo_box(self):

        pass

    # Фильтр событий
    # В параметры функции также требуется передавать текущий выбранный на календаре месяц
    def filter_events_by_tag(self):
        # Получение объектов событий за выбранный месяц

        # Получение дат событий за выбранный месяц


        pass

    # Подсвечивание событий в календаре с одинаковым тегом
    def display_events_with_same_tag(self):


        pass

    # Очистка фильтров
    def remove_events(self):

        pass

    # Отображение в правой части экрана всех активностей за выбранный день
    def display_events_on_certain_day(self):

        pass
