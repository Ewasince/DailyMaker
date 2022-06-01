import datetime

from PyQt5.QtCore import QDate
from PyQt5.uic.properties import QtCore

from widgets.widget_schedule import Ui_Form
from PyQt5 import QtWidgets
from db_manager import Load_manager
from PyQt5.QtCore import QDate
from plan_manager import plan_event


class Ui_Schedule(Ui_Form):
    widget = None
    owner = None
    manager = Load_manager()
    events: [plan_event] = list()
    activity_buttons = list()
    min_date = QDate(2022, 1, 1)
    max_date = QDate(2022, 12, 31)

    def __init__(self, owner):
        self.owner = owner

    def setupUi(self):
        self.widget = QtWidgets.QWidget(self.owner)
        super().setupUi(self.widget)

        self.removeFiltersButton.setStyleSheet("border-radius: 10px;\n"
                                               "background-color: rgb(63, 75, 90);\n"
                                               "color: rgb(255, 255, 255);\n"
                                               "font: 10pt \"Microsoft YaHei UI\";")
        self.findEventEditText.setStyleSheet("border-radius: 10px;\n"
                                             "background-color: rgb(63, 75, 90);\n"
                                             "font: 10pt \"Microsoft YaHei UI\";;\n"
                                             "color: rgb(255, 255, 255);")

        self.events = self.manager.load_events(self.min_date, self.max_date)

        self.fill_combo_box()
        self.comboBoxAddFilters.setCurrentIndex(-1)
        self.comboBoxAddFilters.setEditable(False)
        self.comboBoxAddFilters.activated.connect(self.filter_events_by_tag)

        self.removeFiltersButton.clicked.connect(self.remove_events)

        self.initialize_activity_buttons()
        for item in self.activity_buttons:
            item.hide()
        self.labelActivity_3.hide()

        #self.findEventEditText.activated.connect(self.find_event_by_name)
        self.calendarWidget.clicked.connect(self.event_calendar_clicked)
        self.calendarWidget.currentPageChanged.connect(self.event_change_view)

        pass

    def show(self):
        current_date = self.calendarWidget.selectedDate()
        start_date = QDate(current_date.year(), current_date.month(), 1)
        end_date = QDate(current_date.year(), current_date.month(), start_date.daysInMonth())
        self.events = self.manager.load_events(start_date, end_date)
        self.widget.show()

    def hide(self):
        self.widget.hide()

    def event_calendar_clicked(self, day):
        self.display_events_on_certain_day(day)
        pass

    def event_change_view(self, year, month):
        start_date = QDate(year, month, 1)
        end_date = QDate(year, month, start_date.daysInMonth())
        self.events = self.manager.load_events(start_date, end_date)
        pass

    def initialize_activity_buttons(self):
        settings = '''border-radius: 15px;
                    background-color: rgb(63, 75, 90);
                    color: rgb(255, 255, 255);
                    font: 9pt \"Microsoft YaHei UI\";
                    '''
        self.pushButtonActivity_1.setStyleSheet(settings)
        self.pushButtonActivity_2.setStyleSheet(settings)
        self.pushButtonActivity_3.setStyleSheet(settings)
        self.pushButtonActivity_4.setStyleSheet(settings)
        self.pushButtonActivity_5.setStyleSheet(settings)
        self.pushButtonActivity_6.setStyleSheet(settings)
        self.pushButtonActivity_7.setStyleSheet(settings)
        self.pushButtonActivity_8.setStyleSheet(settings)

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
        name = self.findEventEditText.text()

        # Нахождение элемента с заданным именем
        event = plan_event()
        for element in self.events:
            if element.name == name:
                event = element


        pass

    # Инициализация comboBox с фильтрами
    def fill_combo_box(self):
        self.comboBoxAddFilters.addItems(self.manager.get_unique_tags(self.min_date, self.max_date))
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

        self.calendarWidget.specific_dates = unique_dates
        self.calendarWidget.updateCells()
        pass

    # Очистка фильтров
    def remove_events(self):
        self.calendarWidget.specific_dates = None
        self.calendarWidget.updateCells()
        pass

    # Отображение в правой части экрана всех активностей за выбранный день
    def display_events_on_certain_day(self, date: QDate):
        self.labelActivity_2.hide()
        certain_events = list()
        event: plan_event
        for event in self.events:
            if compare_dates(event.date, date):
                certain_events.append(event)

        self.display_events(certain_events)
        if len(certain_events) != 0:
            self.labelActivity_3.hide()
        else:
            self.labelActivity_3.show()

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

            index = 0
            for letter in range(len(event.name)):
                if event.name[letter] == " " and letter <= 20:
                    index = letter

            event_name_str = event.name
            if len(event.name) > 20:
                str_before_index = event.name[:index]
                str_after_index = event.name[index:]
                event_name_str = str_before_index + "\n" + str_after_index

            but.setText(event_name_str + "\n" + f"{event.time_from.toString()[0:-3]}-{event.time_to.toString()[0:-3]}")
            but.show()
            n += 1

def compare_dates(date1: QDate, date2: QDate):
    cond1 = date1.year() == date2.year()
    cond2 = date1.month() == date2.month()
    cond3 = date1.day() == date2.day()
    return cond1 and cond2 and cond3
