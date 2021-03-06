import datetime
import enum

from PyQt5.QtCore import QDate, QTime


# класс ивента
class plan_event:
    id: int = 0
    name: str = None
    time_from: QTime = None
    time_to: QTime = None
    date: QDate = None
    tags: list[str] = None
    description: str = None
    repeat_model = None  # type: repeat_instance

    def __init__(self):
        pass


# класс repeat_model содержит информацию о том, по какой модели повторяется событие
class repeat_instance:
    type = None  # type: Gaps
    time_interval = None
    gap = None  # type: rm_week, rm_month, rm_year

    def __init__(self):
        super().__init__()


# вспомогательный класс, содержит информацию о дня повторения в неделе
class rm_week:
    days_week = {}

    def __init__(self, *numbers):
        # self.days_week = [False] * 7
        # if len(numbers) == 0:
        #     return
        # list = numbers[0]
        # for i in list:
        #     self.days_week[i] = True
        self.days_week = numbers


# вспомогательный класс, содержит информацию о дня повторения в месяце
class rm_month:
    days_month = {}
    isEndure = False

    def __init__(self, isEndure, *numbers):
        # for i in range(31):
        #     self.days_month[i] = False
        #     if len(numbers) != 0:
        #         for j in numbers:
        #             if j == i:
        #                 self.days_month[i] = True
        #                 break
        self.days_month = numbers
        self.isEndure = isEndure


# вспомогательный класс, содержит информацию о дня повторения в году
class rm_year:
    date = None

    def __init__(self, date):
        self.date = date


# enum с названиями моделей повторения событий
class Gaps(enum.Enum):
    day = "дня"
    week = "недели"
    month = "месяца"
    year = "года"

    @staticmethod
    def get_names():
        items = []
        for item in Gaps:
            items.append(item.value)
        return items
