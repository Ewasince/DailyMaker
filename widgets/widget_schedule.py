# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_schedule.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.custom_calendar import My_Calendar


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1121, 631)
        self.rightLayout = QtWidgets.QWidget(Form)
        self.rightLayout.setGeometry(QtCore.QRect(870, 0, 251, 631))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightLayout.sizePolicy().hasHeightForWidth())
        self.rightLayout.setSizePolicy(sizePolicy)
        self.rightLayout.setStyleSheet("background-color: rgb(75, 90, 108);")
        self.rightLayout.setObjectName("rightLayout")
        self.pushButtonActivity_6 = QtWidgets.QPushButton(self.rightLayout)
        self.pushButtonActivity_6.setGeometry(QtCore.QRect(15, 522, 220, 83))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonActivity_6.sizePolicy().hasHeightForWidth())
        self.pushButtonActivity_6.setSizePolicy(sizePolicy)
        self.pushButtonActivity_6.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButtonActivity_6.setMaximumSize(QtCore.QSize(300, 100))
        self.pushButtonActivity_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButtonActivity_6.setStyleSheet("background-color: rgb(63, 75, 90);\n"
                                                "color: rgb(255, 255, 255);\n"
                                                "font: 13pt \"Microsoft YaHei UI\";\n"
                                                "border-radius: 20px;")
        self.pushButtonActivity_6.setAutoRepeat(False)
        self.pushButtonActivity_6.setAutoDefault(False)
        self.pushButtonActivity_6.setFlat(False)
        self.pushButtonActivity_6.setObjectName("pushButtonActivity_6")
        self.pushButtonActivity_5 = QtWidgets.QPushButton(self.rightLayout)
        self.pushButtonActivity_5.setGeometry(QtCore.QRect(15, 432, 220, 83))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonActivity_5.sizePolicy().hasHeightForWidth())
        self.pushButtonActivity_5.setSizePolicy(sizePolicy)
        self.pushButtonActivity_5.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButtonActivity_5.setMaximumSize(QtCore.QSize(300, 100))
        self.pushButtonActivity_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButtonActivity_5.setStyleSheet("background-color: rgb(63, 75, 90);\n"
                                                "color: rgb(255, 255, 255);\n"
                                                "font: 13pt \"Microsoft YaHei UI\";\n"
                                                "border-radius: 20px;")
        self.pushButtonActivity_5.setAutoRepeat(False)
        self.pushButtonActivity_5.setAutoDefault(False)
        self.pushButtonActivity_5.setFlat(False)
        self.pushButtonActivity_5.setObjectName("pushButtonActivity_5")
        self.pushButtonActivity_4 = QtWidgets.QPushButton(self.rightLayout)
        self.pushButtonActivity_4.setGeometry(QtCore.QRect(15, 342, 220, 83))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonActivity_4.sizePolicy().hasHeightForWidth())
        self.pushButtonActivity_4.setSizePolicy(sizePolicy)
        self.pushButtonActivity_4.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButtonActivity_4.setMaximumSize(QtCore.QSize(300, 100))
        self.pushButtonActivity_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButtonActivity_4.setStyleSheet("background-color: rgb(63, 75, 90);\n"
                                                "color: rgb(255, 255, 255);\n"
                                                "font: 13pt \"Microsoft YaHei UI\";\n"
                                                "border-radius: 20px;")
        self.pushButtonActivity_4.setAutoRepeat(False)
        self.pushButtonActivity_4.setAutoDefault(False)
        self.pushButtonActivity_4.setFlat(False)
        self.pushButtonActivity_4.setObjectName("pushButtonActivity_4")
        self.pushButtonActivity_3 = QtWidgets.QPushButton(self.rightLayout)
        self.pushButtonActivity_3.setGeometry(QtCore.QRect(15, 252, 220, 83))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonActivity_3.sizePolicy().hasHeightForWidth())
        self.pushButtonActivity_3.setSizePolicy(sizePolicy)
        self.pushButtonActivity_3.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButtonActivity_3.setMaximumSize(QtCore.QSize(300, 100))
        self.pushButtonActivity_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButtonActivity_3.setStyleSheet("background-color: rgb(63, 75, 90);\n"
                                                "color: rgb(255, 255, 255);\n"
                                                "font: 13pt \"Microsoft YaHei UI\";\n"
                                                "border-radius: 20px;")
        self.pushButtonActivity_3.setAutoRepeat(False)
        self.pushButtonActivity_3.setAutoDefault(False)
        self.pushButtonActivity_3.setFlat(False)
        self.pushButtonActivity_3.setObjectName("pushButtonActivity_3")
        self.pushButtonActivity_2 = QtWidgets.QPushButton(self.rightLayout)
        self.pushButtonActivity_2.setGeometry(QtCore.QRect(15, 162, 220, 83))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonActivity_2.sizePolicy().hasHeightForWidth())
        self.pushButtonActivity_2.setSizePolicy(sizePolicy)
        self.pushButtonActivity_2.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButtonActivity_2.setMaximumSize(QtCore.QSize(300, 100))
        self.pushButtonActivity_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButtonActivity_2.setStyleSheet("background-color: rgb(63, 75, 90);\n"
                                                "color: rgb(255, 255, 255);\n"
                                                "font: 13pt \"Microsoft YaHei UI\";\n"
                                                "border-radius: 20px;")
        self.pushButtonActivity_2.setAutoRepeat(False)
        self.pushButtonActivity_2.setAutoDefault(False)
        self.pushButtonActivity_2.setFlat(False)
        self.pushButtonActivity_2.setObjectName("pushButtonActivity_2")
        self.pushButtonActivity_1 = QtWidgets.QPushButton(self.rightLayout)
        self.pushButtonActivity_1.setGeometry(QtCore.QRect(15, 72, 220, 83))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonActivity_1.sizePolicy().hasHeightForWidth())
        self.pushButtonActivity_1.setSizePolicy(sizePolicy)
        self.pushButtonActivity_1.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButtonActivity_1.setMaximumSize(QtCore.QSize(300, 100))
        self.pushButtonActivity_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButtonActivity_1.setStyleSheet("background-color: rgb(63, 75, 90);\n"
                                                "color: rgb(255, 255, 255);\n"
                                                "font: 13pt \"Microsoft YaHei UI\";\n"
                                                "border-radius: 20px;")
        self.pushButtonActivity_1.setAutoRepeat(False)
        self.pushButtonActivity_1.setAutoDefault(False)
        self.pushButtonActivity_1.setDefault(False)
        self.pushButtonActivity_1.setFlat(False)
        self.pushButtonActivity_1.setObjectName("pushButtonActivity_1")
        self.labelActivity = QtWidgets.QLabel(self.rightLayout)
        self.labelActivity.setGeometry(QtCore.QRect(0, 22, 250, 27))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelActivity.sizePolicy().hasHeightForWidth())
        self.labelActivity.setSizePolicy(sizePolicy)
        self.labelActivity.setMaximumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelActivity.setFont(font)
        self.labelActivity.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "font: 15pt \"Microsoft YaHei UI\";")
        self.labelActivity.setTextFormat(QtCore.Qt.AutoText)
        self.labelActivity.setAlignment(QtCore.Qt.AlignCenter)
        self.labelActivity.setObjectName("labelActivity")
        self.labelActivity_2 = QtWidgets.QLabel(self.rightLayout)
        self.labelActivity_2.setGeometry(QtCore.QRect(0, 265, 250, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelActivity_2.sizePolicy().hasHeightForWidth())
        self.labelActivity_2.setSizePolicy(sizePolicy)
        self.labelActivity_2.setMaximumSize(QtCore.QSize(1000, 500))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelActivity_2.setFont(font)
        self.labelActivity_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                           "font: 15pt \"Microsoft YaHei UI\";")
        self.labelActivity_2.setTextFormat(QtCore.Qt.AutoText)
        self.labelActivity_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelActivity_2.setObjectName("labelActivity_2")
        self.labelActivity_3 = QtWidgets.QLabel(self.rightLayout)
        self.labelActivity_3.setGeometry(QtCore.QRect(0, 265, 250, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelActivity_3.sizePolicy().hasHeightForWidth())
        self.labelActivity_3.setSizePolicy(sizePolicy)
        self.labelActivity_3.setMaximumSize(QtCore.QSize(1000, 500))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelActivity_3.setFont(font)
        self.labelActivity_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                           "font: 15pt \"Microsoft YaHei UI\";")
        self.labelActivity_3.setTextFormat(QtCore.Qt.AutoText)
        self.labelActivity_3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelActivity_3.setObjectName("labelActivity_3")
        self.pushButtonActivity_7 = QtWidgets.QPushButton(self.rightLayout)
        self.pushButtonActivity_7.setGeometry(QtCore.QRect(15, 72, 220, 200))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonActivity_7.sizePolicy().hasHeightForWidth())
        self.pushButtonActivity_7.setSizePolicy(sizePolicy)
        self.pushButtonActivity_7.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButtonActivity_7.setMaximumSize(QtCore.QSize(1000, 1000))
        self.pushButtonActivity_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButtonActivity_7.setStyleSheet("background-color: rgb(63, 75, 90);\n"
                                                "color: rgb(255, 255, 255);\n"
                                                "font: 13pt \"Microsoft YaHei UI\";\n"
                                                "border-radius: 20px;")
        self.pushButtonActivity_7.setAutoRepeat(False)
        self.pushButtonActivity_7.setAutoDefault(False)
        self.pushButtonActivity_7.setDefault(False)
        self.pushButtonActivity_7.setFlat(False)
        self.pushButtonActivity_7.setObjectName("pushButtonActivity_7")
        self.centralLayout = QtWidgets.QWidget(Form)
        self.centralLayout.setGeometry(QtCore.QRect(0, 0, 871, 631))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralLayout.sizePolicy().hasHeightForWidth())
        self.centralLayout.setSizePolicy(sizePolicy)
        self.centralLayout.setObjectName("centralLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralLayout)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.centerUpperLayout = QtWidgets.QWidget(self.centralLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centerUpperLayout.sizePolicy().hasHeightForWidth())
        self.centerUpperLayout.setSizePolicy(sizePolicy)
        self.centerUpperLayout.setMinimumSize(QtCore.QSize(0, 30))
        self.centerUpperLayout.setObjectName("centerUpperLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centerUpperLayout)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centerUpperLayout)
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setMaximumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font: 20pt \"Microsoft YaHei UI\";")
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignVCenter)
        spacerItem = QtWidgets.QSpacerItem(645, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addWidget(self.centerUpperLayout, 0, QtCore.Qt.AlignHCenter)
        self.centerCenterLayout = QtWidgets.QWidget(self.centralLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centerCenterLayout.sizePolicy().hasHeightForWidth())
        self.centerCenterLayout.setSizePolicy(sizePolicy)
        self.centerCenterLayout.setMinimumSize(QtCore.QSize(801, 30))
        self.centerCenterLayout.setMaximumSize(QtCore.QSize(801, 30))
        self.centerCenterLayout.setObjectName("centerCenterLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centerCenterLayout)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addFiltersLabel = QtWidgets.QLabel(self.centerCenterLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addFiltersLabel.sizePolicy().hasHeightForWidth())
        self.addFiltersLabel.setSizePolicy(sizePolicy)
        self.addFiltersLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
                                           "font: 10pt \"Microsoft YaHei UI\";")
        self.addFiltersLabel.setObjectName("addFiltersLabel")
        self.horizontalLayout_2.addWidget(self.addFiltersLabel, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.comboBoxAddFilters = QtWidgets.QComboBox(self.centerCenterLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxAddFilters.sizePolicy().hasHeightForWidth())
        self.comboBoxAddFilters.setSizePolicy(sizePolicy)
        self.comboBoxAddFilters.setMinimumSize(QtCore.QSize(140, 30))
        self.comboBoxAddFilters.setMaximumSize(QtCore.QSize(140, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 96, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 96, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 96, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 96, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 96, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 96, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 96, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 96, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 96, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.comboBoxAddFilters.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.comboBoxAddFilters.setFont(font)
        self.comboBoxAddFilters.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.comboBoxAddFilters.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBoxAddFilters.setAutoFillBackground(False)
        self.comboBoxAddFilters.setStyleSheet("background-color: rgb(80, 96, 115);\n"
                                              "color: rgb(255, 255, 255);\n"
                                              "font: 10pt \"Microsoft JhengHei UI\";")
        self.comboBoxAddFilters.setEditable(False)
        self.comboBoxAddFilters.setCurrentText("")
        self.comboBoxAddFilters.setMaxVisibleItems(16)
        self.comboBoxAddFilters.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.comboBoxAddFilters.setFrame(True)
        self.comboBoxAddFilters.setObjectName("comboBoxAddFilters")
        self.horizontalLayout_2.addWidget(self.comboBoxAddFilters)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.removeFiltersButton = QtWidgets.QPushButton(self.centerCenterLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeFiltersButton.sizePolicy().hasHeightForWidth())
        self.removeFiltersButton.setSizePolicy(sizePolicy)
        self.removeFiltersButton.setMinimumSize(QtCore.QSize(140, 30))
        self.removeFiltersButton.setMaximumSize(QtCore.QSize(140, 30))
        self.removeFiltersButton.setStyleSheet("background-color: rgb(63, 75, 90);\n"
                                               "color: rgb(255, 255, 255);\n"
                                               "font: 10pt \"Microsoft YaHei UI\";\n"
                                               "border-radius: 10px;")
        self.removeFiltersButton.setObjectName("removeFiltersButton")
        self.horizontalLayout_2.addWidget(self.removeFiltersButton, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.verticalLayout_3.addWidget(self.centerCenterLayout, 0, QtCore.Qt.AlignHCenter)
        self.calendarWidget = My_Calendar(self.centralLayout)
        self.calendarWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        self.calendarWidget.setMinimumSize(QtCore.QSize(801, 470))
        self.calendarWidget.setMaximumSize(QtCore.QSize(801, 470))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.calendarWidget.setMouseTracking(False)
        self.calendarWidget.setTabletTracking(False)
        self.calendarWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.calendarWidget.setAcceptDrops(False)
        self.calendarWidget.setStatusTip("")
        self.calendarWidget.setWhatsThis("")
        self.calendarWidget.setAccessibleName("")
        self.calendarWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.calendarWidget.setAutoFillBackground(False)
        self.calendarWidget.setStyleSheet("background-color: rgb(75, 90, 108);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "alternate-background-color: rgb(63, 75, 90);\n"
                                          "\n"
                                          "")
        self.calendarWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout_3.addWidget(self.calendarWidget, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButtonActivity_6.setText(_translate("Form", "Активность 6"))
        self.pushButtonActivity_5.setText(_translate("Form", "Активность 5"))
        self.pushButtonActivity_4.setText(_translate("Form", "Активность 4"))
        self.pushButtonActivity_3.setText(_translate("Form", "Активность 3"))
        self.pushButtonActivity_2.setText(_translate("Form", "Активность 2"))
        self.pushButtonActivity_1.setText(_translate("Form", "Активность 1"))
        self.labelActivity.setText(_translate("Form", "Список активностей"))
        self.labelActivity_2.setText(_translate("Form", "Здесь будут\n"
                                                        "отображены\n"
                                                        " ваши события"))
        self.labelActivity_3.setText(_translate("Form", "На этот день\n"
                                                        " ничего не\n"
                                                        "запланировано"))
        self.pushButtonActivity_7.setText(_translate("Form", "Активность 1"))
        self.label.setText(_translate("Form", "Расписание"))
        self.addFiltersLabel.setText(_translate("Form", "Добавить фильтры"))
        self.removeFiltersButton.setText(_translate("Form", "Убрать фильтры"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
