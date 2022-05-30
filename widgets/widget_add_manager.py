import plan_manager
from plan_manager import Gaps, plan_event, repeat_instance
import db_manager

from widgets.widget_add import Ui_Form
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import datetime


class Ui_Add(Ui_Form):
    widget = None  # виджет, с которым мы работаем
    owner = None  # родительский элемент интерфейса
    widgets = []  # контейнеры с доп инфой, который показываются при указании повтора события
    checked_days_of_month = []  # массив для работы слайдера
    list_checkboxes_week = ()  # массив для удобного перебора чекбоксов дней недели

    def __init__(self, owner):
        self.owner = owner  # установка родительского жлемента
        self.initialize_slider()

    def setupUi(self):
        self.widget = QtWidgets.QWidget(self.owner)
        super().setupUi(self.widget)
        self.widget_week.hide()
        self.widgets.append(self.widget_week)
        self.widgets.append(self.widget_month)
        self.widgets.append(self.widget_year)
        for item in self.widgets:
            item.hide()
        self.comboBox_gap.clear()
        self.comboBox_gap.addItems(Gaps.get_names())
        self.comboBox_gap.activated.connect(self.comboBox_event)
        self.horizontalSlider.valueChanged.connect(self.slider_event)
        self.checkBox_gap_month.stateChanged.connect(self.checked_gap_month_event)

        self.pushButton_save.clicked.connect(self.save_event)
        self.pushButton_delete.clicked.connect(self.delete_event)
        self.pushButton_today.clicked.connect(self.today_event)
        self.pushButton_tomorrow.clicked.connect(self.tomorrow_event)

        self.list_checkboxes_week = (
            self.checkBox_mo, self.checkBox_tu, self.checkBox_we, self.checkBox_th, self.checkBox_fr, self.checkBox_sa,
            self.checkBox_su)

        self.set_default()

    def clear_fields(self):
        self.lineEdit_name.setText('')
        self.lineEdit_tags.setText('')
        self.textEdit_main.setText('')
        self.spinBox_count_repeats.setValue(0)
        self.comboBox_gap.setCurrentIndex(0)
        self.comboBox_event()
        self.checkBox_endure.setChecked(False)
        self.checkBox_gap_month.setChecked(False)
        self.initialize_slider()
        for item in self.list_checkboxes_week:
            item.setChecked(False)
        self.set_default()

    def initialize_slider(self):  # инициализация массива, нужного для работы слайдера
        self.checked_days_of_month = []
        for i in range(31):
            self.checked_days_of_month.append(False)

    def set_default(self):
        self.today_event()
        now = datetime.datetime.now()
        self.timeEdit_start.setTime(datetime.time((now.hour + 1) % 24))
        self.timeEdit_end.setTime(datetime.time((now.hour + 2) % 24))
        self.dateEdit_year.setDate(datetime.date.today())

    def comboBox_event(self):
        value = self.comboBox_gap.currentText()
        match value:
            case Gaps.day.value:
                self.show_gap_widget(None)
            case Gaps.week.value:
                self.show_gap_widget(self.widget_week)
            case Gaps.month.value:
                self.show_gap_widget(self.widget_month)
            case Gaps.year.value:
                self.show_gap_widget(self.widget_year)

    def show_gap_widget(self, widget):
        for item in self.widgets:
            if item == widget:
                item.show()
            else:
                item.hide()

    def slider_event(self):
        num = self.horizontalSlider.sliderPosition()
        self.label_slider.setText(str(num))
        vals = self.checked_days_of_month
        self.checkBox_gap_month.setChecked(vals[num - 1])

    def checked_gap_month_event(self):
        status = self.checkBox_gap_month.isChecked()
        slider_position = self.horizontalSlider.sliderPosition()
        self.checked_days_of_month[slider_position - 1] = status

    flag_plan_instance: bool = True

    def save_event(self):
        self.flag_plan_instance = True
        plan_instance = plan_event()
        self.fill_plan_instance(plan_instance)
        if self.spinBox_count_repeats.value() != 0:  # проверка является ли план дела повторяемым
            self.set_plan_repeat_model(plan_instance)
        if self.flag_plan_instance:
            self.save_plan_instance(plan_instance)
            self.process_plan_instance(plan_instance)

    def save_plan_instance(self, instance):
        save_manager = db_manager.Save_manager()
        save_manager.save_event(instance)
        pass

    def process_plan_instance(self, instance):
        pass

    def fill_plan_instance(self, instance: plan_event):
        instance.name = self.lineEdit_name.text()

        date = self.dateEdit_date.date()
        time_start = self.timeEdit_start.time()
        time_end = self.timeEdit_end.time()
        date_time = datetime.datetime(date.year(), date.month(), date.day(), time_start.hour(), time_start.minute())
        instance.date = date
        instance.time_from = time_start
        instance.time_to = time_end
        if date_time < datetime.datetime.now():
            self.warning_message('Дата и время окончания события меньше, чем дата и время сейчас. Вы '
                                 'уверены, что хотите создать событие в прошлом?')
        if time_start >= time_end:
            self.warning_message('Время окончания события меньше, чем время начала. Окончание события будет '
                                 'перенесено на следующий день')
        instance.tags = list(map(lambda x: x.strip(), self.lineEdit_tags.text().split(',')))
        instance.description = self.textEdit_main.toPlainText()

    def set_plan_repeat_model(self, instance: plan_event):
        repeat_instance_ = repeat_instance()

        type = self.comboBox_gap.currentText()
        repeat_instance_.type = type
        repeat_instance_.gap = self.spinBox_count_repeats.value()
        match type:
            case Gaps.week.value:
                days_of_week = []
                # value: QtWidgets.QCheckBox = None # TODO: разобраться можно ли указывать тип в цикле
                for count, value in enumerate(self.list_checkboxes_week):
                    if (value.isChecked()):
                        days_of_week.append(count)
                week_model = plan_manager.rm_week(days_of_week)
                repeat_instance_.time_interval = week_model
            case Gaps.month.value:
                # n = 0
                month_days = [n for n, i in enumerate(self.checked_days_of_month) if i is True]
                month_model = plan_manager.rm_month(self.checkBox_endure.isChecked(),
                                                    month_days)
                repeat_instance_.time_interval = month_model
            case Gaps.year.value:
                year_model = plan_manager.rm_year(self.dateEdit_year.date())
                repeat_instance_.time_interval = year_model
        instance.repeat_model = repeat_instance_

    def warning_message(self, text, title='Подтвердите действие'):
        error = QtWidgets.QMessageBox()
        error.setText(text)
        error.setWindowTitle(title)
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        error.setDefaultButton(QMessageBox.No)
        error.buttonClicked.connect(self.warning_message_event)

        error.exec_()  # TODO: доделать логику всплывающего сообщения

    def warning_message_event(self, btn):  # TODO: эта пар*ша не работает
        if btn.text() == 'Yes':
            self.flag_plan_instance = True
        elif btn.text() == 'No':
            self.flag_plan_instance = False

    def delete_event(self):
        self.clear_fields()

    def today_event(self):
        date = datetime.date.today()
        # date_str = date.strftime('%d.%m.%Y')
        self.dateEdit_date.setDate(date)

    def tomorrow_event(self):
        today = datetime.date.today()
        date = datetime.date(today.year, today.month, today.day + 1)
        self.dateEdit_date.setDate(date)
        pass
