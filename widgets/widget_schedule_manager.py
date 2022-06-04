from PyQt5.uic.properties import QtCore

from widgets import custom_calendar
from widgets.widget_schedule import Ui_Form
from PyQt5 import QtWidgets
from db_manager import Load_manager
from PyQt5.QtCore import QDate
from plan_manager import plan_event


# from custom_calendar import Calendar_manager
# from custom_calendar import Calendar_manager

class Ui_Schedule(Ui_Form):
    widget = None
    owner = None
    load_manager = Load_manager()
    events: [plan_event] = list()
    activity_buttons = list()
    # min_date = QDate(2022, 1, 1)
    # max_date = QDate(2022, 12, 31)
    selected_tags = set()
    start_date = None # период отображенных дат, старт - неделя
    end_date = None # период отображенных дат, конец + неделя

    def __init__(self, owner):
        self.owner = owner

    def setupUi(self, **kwargs):
        self.widget = QtWidgets.QWidget(self.owner)
        super().setupUi(self.widget)

        date_shown = QDate(self.calendarWidget.yearShown(), self.calendarWidget.monthShown(), 1)
        self.start_date = date_shown.addDays(-7)
        self.end_date = date_shown.addDays(date_shown.daysInMonth()-1).addDays(7)

        self.events = self.load_manager.load_events(self.start_date, self.end_date)

        self.refresh_comboBox()
        self.comboBoxAddFilters.setCurrentIndex(-1)
        self.comboBoxAddFilters.setEditable(False)
        self.comboBoxAddFilters.activated.connect(self.event_add_selected_tags)

        self.removeFiltersButton.clicked.connect(self.event_clear_selected_events)

        self.initialize_activity_buttons()
        self.pushButtonActivity_7.hide()
        for item in self.activity_buttons:
            item.hide()
        self.labelActivity_3.hide()

        # self.findEventEditText.installEventFilter(self)
        self.calendarWidget.clicked.connect(self.event_calendar_clicked)
        self.calendarWidget.currentPageChanged.connect(self.event_change_view)

        pass

    # def eventFilter(self, obj, event):
    #     if event.type() == QtCore.QEvent.KeyPress and obj is self.findEventEditText:
    #         if event.key() == QtCore.Qt.Key_Return and self.findEventEditText.hasFocus():
    #             print('Enter pressed')
    #     return super().eventFilter(obj, event)

    def show(self):
        current_date = self.calendarWidget.selectedDate()
        start_date = QDate(current_date.year(), current_date.month(), 1)
        end_date = QDate(current_date.year(), current_date.month(), start_date.daysInMonth())
        self.events = self.load_manager.load_events(start_date, end_date)
        self.comboBoxAddFilters.clear()
        self.refresh_comboBox()
        self.widget.show()

    def hide(self):
        self.widget.hide()

    def event_calendar_clicked(self, date: QDate):
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

    def event_change_view(self, year, month):
        start_date = QDate(year, month, 1)
        end_date = QDate(year, month, start_date.daysInMonth())
        self.events = self.load_manager.load_events(start_date, end_date)
        pass

    def initialize_activity_buttons(self):
        self.activity_buttons = [self.pushButtonActivity_1,
                                 self.pushButtonActivity_2,
                                 self.pushButtonActivity_3,
                                 self.pushButtonActivity_4,
                                 self.pushButtonActivity_5,
                                 self.pushButtonActivity_6]

    # # Соответствует полю "поиск"
    # def find_event_by_name(self):
    #     name = self.findEventEditText.text()
    #
    #     # Нахождение элемента с заданным именем
    #     event = plan_event()
    #     for element in self.events:
    #         if element.name == name:
    #             event = element
    #
    #
    #     pass

    # Обновить выбранные тэги в compoBox
    def refresh_comboBox(self):
        items = self.load_manager.get_unique_tags(self.start_date, self.end_date)
        self.comboBoxAddFilters.addItems(items)
        self.comboBoxAddFilters.setCurrentIndex(-1)
        self.comboBoxAddFilters.setEditable(False)
        pass

    # Добавить тэг к фильтру
    def event_add_selected_tags(self):
        self.selected_tags.add(self.comboBoxAddFilters.currentText())

        dates = set()
        # Получение дат событий за выбранный месяц
        for event in self.events:
            for tag in event.tags:
                if tag in self.selected_tags:
                    dates.add(event.date)

        custom_calendar.Calendar_manager.selected_dates = dates
        self.calendarWidget.updateCells()
        pass

    # Очистка фильтров
    def event_clear_selected_events(self):
        custom_calendar.Calendar_manager.selected_dates = None
        self.selected_tags = set()
        self.calendarWidget.updateCells()
        self.comboBoxAddFilters.setCurrentIndex(-1)
        self.comboBoxAddFilters.setEditable(False)
        pass

    # Отобразить выбранный ивент
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


# сравнение какая дата больше
def compare_dates(date1: QDate, date2: QDate) -> bool:
    cond1 = date1.year() == date2.year()
    cond2 = date1.month() == date2.month()
    cond3 = date1.day() == date2.day()
    return cond1 and cond2 and cond3
