import datetime
import enum


class onetime_instance:
    name: str = None
    time_from: datetime.time = None
    time_to: datetime.time = None
    date: datetime.date = None
    tags: str = []
    description: str = None

    def __init__(self):
        pass


class reusable_instance(onetime_instance):
    type = None  # type: Gaps
    repeat_model = None
    gap = None

    def __init__(self):
        super().__init__()


class rm_week:
    days_week = {}

    def __init__(self, *numbers):  # TODO: проверить как это говно работает или придумать что нибуль по-лучше
        for i in range(7):
            self.days_week[i] = False
            if len(numbers) != 0:
                for j in numbers:
                    if j == i:
                        self.days_week[i] = True
                        break


class rm_month:
    days_month = {}
    isEndure = False

    def __init__(self, *numbers):
        for i in range(31):
            self.days_month[i] = False
            if len(numbers) != 0:
                for j in numbers:
                    if j == i:
                        self.days_month[i] = True
                        break


class rm_year:
    date = None

    def __init__(self, date):
        self.date = date


if __name__ == "__main__":
    pass


# class type_plan(enum.Enum):
#     onetime = 0
#     reusable = 1

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
