from plan_instance import Gaps

from widgets.widget_add import Ui_Form
from PyQt5 import QtWidgets


class Ui_Add(Ui_Form):
    widget = None
    owner = None
    widgets = []
    slider_vals = []

    def __init__(self, owner):
        self.owner = owner
        for i in range(31):
            self.slider_vals.append(False)

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
        vals = self.slider_vals
        self.checkBox_gap_month.setChecked(vals[num-1])

    def checked_gap_month_event(self):
        status = self.checkBox_gap_month.isChecked()
        slider_position = self.horizontalSlider.sliderPosition()
        self.slider_vals[slider_position-1] = status

    def save_event(self):
        pass

    def delete_event(self):
        pass

    def today_event(self):
        pass

    def tomorrow_event(self):
        pass
