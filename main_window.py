# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1200, 631)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 631))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 631))
        MainWindow.setBaseSize(QtCore.QSize(1200, 610))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("")
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(1200, 631))
        self.centralwidget.setMaximumSize(QtCore.QSize(1200, 631))
        self.centralwidget.setBaseSize(QtCore.QSize(1200, 631))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.centralwidget.setFont(font)
        self.centralwidget.setMouseTracking(False)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("background-color: rgb(90, 108, 131);")
        self.centralwidget.setObjectName("centralwidget")
        self.leftLayout = QtWidgets.QWidget(self.centralwidget)
        self.leftLayout.setGeometry(QtCore.QRect(0, 0, 81, 631))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftLayout.sizePolicy().hasHeightForWidth())
        self.leftLayout.setSizePolicy(sizePolicy)
        self.leftLayout.setStyleSheet("background-color: rgb(75, 90, 108);")
        self.leftLayout.setObjectName("leftLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.leftLayout)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.pushButton_schedule = QtWidgets.QPushButton(self.leftLayout)
        self.pushButton_schedule.setEnabled(True)
        self.pushButton_schedule.setMinimumSize(QtCore.QSize(63, 63))
        self.pushButton_schedule.setStyleSheet("#pushButton_schedule{\n"
                                               "border-image: url(:/1_schedule/1_schedule_up.jpg)\n"
                                               "}\n"
                                               "#pushButton_schedule:pressed{\n"
                                               "border-image: url(:/1_schedule/1_schedule_down.jpg)\n"
                                               "}")
        self.pushButton_schedule.setText("")
        self.pushButton_schedule.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_schedule.setObjectName("pushButton_schedule")
        self.verticalLayout_2.addWidget(self.pushButton_schedule)
        spacerItem1 = QtWidgets.QSpacerItem(20, 400, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.pushButton_add = QtWidgets.QPushButton(self.leftLayout)
        self.pushButton_add.setMinimumSize(QtCore.QSize(63, 63))
        self.pushButton_add.setStyleSheet("#pushButton_add{\n"
                                          "border-image: url(:/2_add/2_add_up.jpg)\n"
                                          "}\n"
                                          "#pushButton_add:pressed{\n"
                                          "border-image: url(:/2_add/2_add_down.jpg)\n"
                                          "}")
        self.pushButton_add.setText("")
        self.pushButton_add.setObjectName("pushButton_add")
        self.verticalLayout_2.addWidget(self.pushButton_add)
        spacerItem2 = QtWidgets.QSpacerItem(20, 340, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.pushButton_analytics = QtWidgets.QPushButton(self.leftLayout)
        self.pushButton_analytics.setMinimumSize(QtCore.QSize(63, 63))
        self.pushButton_analytics.setStyleSheet("#pushButton_analytics{\n"
                                                "border-image: url(:/3_analytics/3_analytics_up.jpg)\n"
                                                "}\n"
                                                "#pushButton_analytics:pressed{\n"
                                                "border-image: url(:/3_analytics/3_analytics_down.jpg)\n"
                                                "}")
        self.pushButton_analytics.setText("")
        self.pushButton_analytics.setObjectName("pushButton_analytics")
        self.verticalLayout_2.addWidget(self.pushButton_analytics)
        self.widget_parent = QtWidgets.QWidget(self.centralwidget)
        self.widget_parent.setGeometry(QtCore.QRect(80, 0, 1131, 631))
        self.widget_parent.setObjectName("widget_parent")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


import icons_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
