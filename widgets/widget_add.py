# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\widget_add.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1130, 631)
        Form.setMinimumSize(QtCore.QSize(750, 580))
        self.lineEdit_name = QtWidgets.QLineEdit(Form)
        self.lineEdit_name.setGeometry(QtCore.QRect(40, 80, 621, 20))
        self.lineEdit_name.setToolTip("")
        self.lineEdit_name.setStyleSheet("background-color: rgb(63, 75, 90);\n"
                                         "font: 10pt \"Microsoft YaHei UI\";;\n"
                                         "color: rgb(255, 255, 255);")
        self.lineEdit_name.setText("")
        self.lineEdit_name.setFrame(False)
        self.lineEdit_name.setDragEnabled(False)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.pushButton_save = QtWidgets.QPushButton(Form)
        self.pushButton_save.setGeometry(QtCore.QRect(690, 80, 191, 23))
        self.pushButton_save.setStyleSheet("background-color: rgb(63, 75, 90);\n"
                                           "font: 10pt \"Microsoft YaHei UI\";;\n"
                                           "color: rgb(255, 255, 255);")
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_delete = QtWidgets.QPushButton(Form)
        self.pushButton_delete.setGeometry(QtCore.QRect(910, 80, 181, 23))
        self.pushButton_delete.setStyleSheet("background-color: rgb(63, 75, 90);\n"
                                             "font: 10pt \"Microsoft YaHei UI\";;\n"
                                             "color: rgb(255, 255, 255);")
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.timeEdit_start = QtWidgets.QTimeEdit(Form)
        self.timeEdit_start.setGeometry(QtCore.QRect(40, 120, 291, 22))
        self.timeEdit_start.setStyleSheet("background-color: rgb(63, 75, 90);\n"
                                          "font: 10pt \"Microsoft YaHei UI\";;\n"
                                          "color: rgb(255, 255, 255);")
        self.timeEdit_start.setFrame(False)
        self.timeEdit_start.setTime(QtCore.QTime(10, 0, 0))
        self.timeEdit_start.setObjectName("timeEdit_start")
        self.timeEdit_end = QtWidgets.QTimeEdit(Form)
        self.timeEdit_end.setGeometry(QtCore.QRect(360, 120, 301, 22))
        self.timeEdit_end.setStyleSheet("background-color: rgb(63, 75, 90);\n"
                                        "font: 10pt \"Microsoft YaHei UI\";;\n"
                                        "color: rgb(255, 255, 255);")
        self.timeEdit_end.setFrame(False)
        self.timeEdit_end.setTime(QtCore.QTime(11, 0, 0))
        self.timeEdit_end.setObjectName("timeEdit_end")
        self.pushButton_today = QtWidgets.QPushButton(Form)
        self.pushButton_today.setGeometry(QtCore.QRect(690, 120, 191, 23))
        self.pushButton_today.setStyleSheet("background-color: rgb(63, 75, 90);\n"
                                            "font: 10pt \"Microsoft YaHei UI\";;\n"
                                            "color: rgb(255, 255, 255);")
        self.pushButton_today.setObjectName("pushButton_today")
        self.pushButton_tomorrow = QtWidgets.QPushButton(Form)
        self.pushButton_tomorrow.setGeometry(QtCore.QRect(910, 120, 181, 23))
        self.pushButton_tomorrow.setStyleSheet("background-color: rgb(63, 75, 90);\n"
                                               "font: 10pt \"Microsoft YaHei UI\";;\n"
                                               "color: rgb(255, 255, 255);")
        self.pushButton_tomorrow.setObjectName("pushButton_tomorrow")
        self.dateEdit_date = QtWidgets.QDateEdit(Form)
        self.dateEdit_date.setGeometry(QtCore.QRect(690, 160, 401, 22))
        self.dateEdit_date.setStyleSheet("background-color: rgb(63, 75, 90);\n"
                                         "font: 10pt \"Microsoft YaHei UI\";;\n"
                                         "color: rgb(255, 255, 255);")
        self.dateEdit_date.setFrame(False)
        self.dateEdit_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_date.setObjectName("dateEdit_date")
        self.lineEdit_tags = QtWidgets.QLineEdit(Form)
        self.lineEdit_tags.setGeometry(QtCore.QRect(40, 160, 621, 20))
        self.lineEdit_tags.setStyleSheet("background-color: rgb(63, 75, 90);\n"
                                         "font: 10pt \"Microsoft YaHei UI\";;\n"
                                         "color: rgb(255, 255, 255);")
        self.lineEdit_tags.setFrame(False)
        self.lineEdit_tags.setObjectName("lineEdit_tags")
        self.textEdit_main = QtWidgets.QTextEdit(Form)
        self.textEdit_main.setGeometry(QtCore.QRect(40, 200, 621, 401))
        self.textEdit_main.setStyleSheet("background-color: rgb(63, 75, 90);\n"
                                         "font: 10pt \"Microsoft YaHei UI\";;\n"
                                         "color: rgb(255, 255, 255);")
        self.textEdit_main.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_main.setObjectName("textEdit_main")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(690, 200, 121, 16))
        self.label.setObjectName("label")
        self.spinBox_count_repeats = QtWidgets.QSpinBox(Form)
        self.spinBox_count_repeats.setGeometry(QtCore.QRect(810, 200, 71, 22))
        self.spinBox_count_repeats.setStyleSheet("background-color: rgb(63, 75, 90);\n"
                                                 "font: 10pt \"Microsoft YaHei UI\";;\n"
                                                 "color: rgb(255, 255, 255);")
        self.spinBox_count_repeats.setFrame(False)
        self.spinBox_count_repeats.setMinimum(0)
        self.spinBox_count_repeats.setMaximum(100)
        self.spinBox_count_repeats.setObjectName("spinBox_count_repeats")
        self.comboBox_gap = QtWidgets.QComboBox(Form)
        self.comboBox_gap.setGeometry(QtCore.QRect(900, 200, 191, 22))
        self.comboBox_gap.setStyleSheet("background-color: rgb(63, 75, 90);\n"
                                        "font: 10pt \"Microsoft YaHei UI\";;\n"
                                        "color: rgb(255, 255, 255);")
        self.comboBox_gap.setFrame(False)
        self.comboBox_gap.setObjectName("comboBox_gap")
        self.comboBox_gap.addItem("")
        self.comboBox_gap.addItem("")
        self.comboBox_gap.addItem("")
        self.comboBox_gap.addItem("")
        self.widget_week = QtWidgets.QWidget(Form)
        self.widget_week.setEnabled(True)
        self.widget_week.setGeometry(QtCore.QRect(690, 230, 400, 61))
        self.widget_week.setObjectName("widget_week")
        self.checkBox_mo = QtWidgets.QCheckBox(self.widget_week)
        self.checkBox_mo.setGeometry(QtCore.QRect(0, 10, 41, 17))
        self.checkBox_mo.setStyleSheet("")
        self.checkBox_mo.setObjectName("checkBox_mo")
        self.checkBox_tu = QtWidgets.QCheckBox(self.widget_week)
        self.checkBox_tu.setGeometry(QtCore.QRect(60, 10, 41, 17))
        self.checkBox_tu.setObjectName("checkBox_tu")
        self.checkBox_we = QtWidgets.QCheckBox(self.widget_week)
        self.checkBox_we.setGeometry(QtCore.QRect(120, 10, 41, 17))
        self.checkBox_we.setObjectName("checkBox_we")
        self.checkBox_th = QtWidgets.QCheckBox(self.widget_week)
        self.checkBox_th.setGeometry(QtCore.QRect(180, 10, 41, 17))
        self.checkBox_th.setObjectName("checkBox_th")
        self.checkBox_fr = QtWidgets.QCheckBox(self.widget_week)
        self.checkBox_fr.setGeometry(QtCore.QRect(240, 10, 31, 17))
        self.checkBox_fr.setObjectName("checkBox_fr")
        self.checkBox_sa = QtWidgets.QCheckBox(self.widget_week)
        self.checkBox_sa.setGeometry(QtCore.QRect(300, 10, 41, 17))
        self.checkBox_sa.setObjectName("checkBox_sa")
        self.checkBox_su = QtWidgets.QCheckBox(self.widget_week)
        self.checkBox_su.setGeometry(QtCore.QRect(360, 10, 31, 17))
        self.checkBox_su.setObjectName("checkBox_su")
        self.widget_month = QtWidgets.QWidget(Form)
        self.widget_month.setEnabled(True)
        self.widget_month.setGeometry(QtCore.QRect(690, 230, 400, 61))
        self.widget_month.setObjectName("widget_month")
        self.checkBox_gap_month = QtWidgets.QCheckBox(self.widget_month)
        self.checkBox_gap_month.setGeometry(QtCore.QRect(10, 40, 70, 17))
        self.checkBox_gap_month.setObjectName("checkBox_gap_month")
        self.horizontalSlider = QtWidgets.QSlider(self.widget_month)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 10, 301, 22))
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(31)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.checkBox_endure = QtWidgets.QCheckBox(self.widget_month)
        self.checkBox_endure.setGeometry(QtCore.QRect(270, 40, 111, 17))
        self.checkBox_endure.setObjectName("checkBox_endure")
        self.label_slider = QtWidgets.QLabel(self.widget_month)
        self.label_slider.setGeometry(QtCore.QRect(340, 10, 47, 13))
        self.label_slider.setObjectName("label_slider")
        self.widget_year = QtWidgets.QWidget(Form)
        self.widget_year.setEnabled(True)
        self.widget_year.setGeometry(QtCore.QRect(690, 230, 400, 61))
        self.widget_year.setObjectName("widget_year")
        self.dateEdit_year = QtWidgets.QDateEdit(self.widget_year)
        self.dateEdit_year.setGeometry(QtCore.QRect(10, 10, 381, 22))
        self.dateEdit_year.setStyleSheet("background-color: rgb(63, 75, 90);\n"
                                         "font: 10pt \"Microsoft YaHei UI\";;\n"
                                         "color: rgb(255, 255, 255);")
        self.dateEdit_year.setFrame(False)
        self.dateEdit_year.setObjectName("dateEdit_year")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(35, 25, 378, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 30))
        self.label_2.setMaximumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 20pt \"Microsoft YaHei UI\";")
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(False)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        self.lineEdit_name.raise_()
        self.pushButton_save.raise_()
        self.pushButton_delete.raise_()
        self.timeEdit_start.raise_()
        self.timeEdit_end.raise_()
        self.pushButton_today.raise_()
        self.pushButton_tomorrow.raise_()
        self.dateEdit_date.raise_()
        self.lineEdit_tags.raise_()
        self.textEdit_main.raise_()
        self.label.raise_()
        self.spinBox_count_repeats.raise_()
        self.comboBox_gap.raise_()
        self.widget_week.raise_()
        self.widget_year.raise_()
        self.widget_month.raise_()
        self.label_2.raise_()

        self.retranslateUi(Form)
        self.comboBox_gap.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit_name.setPlaceholderText(_translate("Form", "???????????????? ??????????????"))
        self.pushButton_save.setText(_translate("Form", "??????????????????"))
        self.pushButton_delete.setText(_translate("Form", "??????????????"))
        self.pushButton_today.setText(_translate("Form", "???? ??????????????"))
        self.pushButton_tomorrow.setText(_translate("Form", "???? ????????????"))
        self.lineEdit_tags.setPlaceholderText(_translate("Form", "????????, ?????????? ??????????????"))
        self.label.setText(_translate("Form", "???????????? ???????????? "))
        self.comboBox_gap.setCurrentText(_translate("Form", "??????"))
        self.comboBox_gap.setItemText(0, _translate("Form", "??????"))
        self.comboBox_gap.setItemText(1, _translate("Form", "????????????"))
        self.comboBox_gap.setItemText(2, _translate("Form", "??????????"))
        self.comboBox_gap.setItemText(3, _translate("Form", "??????"))
        self.checkBox_mo.setText(_translate("Form", "????"))
        self.checkBox_tu.setText(_translate("Form", "????"))
        self.checkBox_we.setText(_translate("Form", "????"))
        self.checkBox_th.setText(_translate("Form", "????"))
        self.checkBox_fr.setText(_translate("Form", "????"))
        self.checkBox_sa.setText(_translate("Form", "????"))
        self.checkBox_su.setText(_translate("Form", "????"))
        self.checkBox_gap_month.setText(_translate("Form", "??????????????"))
        self.checkBox_endure.setToolTip(_translate("Form",
                                                   "<html><head/><body><p>???????????????????? ?????? ?????????????? ?????? ???????????? ???? ?????????? ?????????????????????? ??????????</p></body></html>"))
        self.checkBox_endure.setText(_translate("Form", "???????????????????? ????????"))
        self.label_slider.setText(_translate("Form", "1"))
        self.dateEdit_year.setDisplayFormat(_translate("Form", "dd.MM"))
        self.label_2.setText(_translate("Form", "???????????????????? ????????????????????"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
