
# сравнение какая дата больше
from PyQt5.QtCore import QDate


def compare_equals_dates(date1: QDate, date2: QDate) -> bool:
    cond1 = date1.year() == date2.year()
    cond2 = date1.month() == date2.month()
    cond3 = date1.day() == date2.day()
    return cond1 and cond2 and cond3
#
# def compare_dates(date1: QDate, date2: QDate) -> bool:
#     cond = PyQt5.QtCore.
#     return False