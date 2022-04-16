import enum


class onetime_instance:
    name = None
    time_from = None
    time_to = None
    date = None
    tags = []
    description = None

    def __init__(self):
        pass

class reusable_instance(onetime_instance):
    type = None # type: Gaps
    repeat_model = None

    def __init__(self):
        super().__init__()

class rm_week:
    days_week = []

    def __init__(self, *numbers): #TODO: проверить как это говно работает или придумать что нибуль по-лучше
        for i in range(7):         #TODO: сделать это на мапе
            if len(numbers) != 0:
                for j in numbers:
                    if j == i:
                        self.days_week.append(True)
                        break
            self.days_week.append(False)

# class rm_month: #TODO: доделать классы повторений
#     days




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
