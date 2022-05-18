import datetime
import enum


class plan_event:
    name: str = None
    time_from: datetime.time = None
    time_to: datetime.time = None
    date: datetime.date = None
    tags: str = []
    description: str = None
    repeat_model = None  # type: repeat_instance

    def __init__(self):
        pass


class repeat_instance:
    type = None  # type: Gaps
    time_interval = None
    gap = None

    def __init__(self):
        super().__init__()


class rm_week:
    days_week = {}

    def __init__(self, *numbers):
        self.days_week = [False] * 7
        if len(numbers) == 0:
            return
        list = numbers[0]
        for i in list:
            self.days_week[i] = True
        # for i in range(7):
        #     self.days_week[i] = False
        #     if len(numbers) != 0:
        #         for j in numbers:
        #             if j == i:
        #                 self.days_week[i] = True
        #                 break


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
