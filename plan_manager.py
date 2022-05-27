import datetime
import enum
import sqlite3


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


class save_events():
    name_db = 'events.db'

    def __init__(self):
        try:
            with open(self.name_db, 'r') as f:
                pass
        except Exception as e:
            print('Файл базы данных не обнаружен, создание...')
            try:
                connection = sqlite3.connect(self.name_db)
                cursor = connection.cursor()
                query = '''CREATE TABLE events(
                id INTEGER AUTOINCREMENT PRIMARY KEY,
                name TEXT,
                description TEXT, 
                is_repetable INTEGER);'''
                cursor.execute(query)
                connection.commit()
                cursor.close()

            except sqlite3.Error as error:
                print("Ошибка при создании базы данных", error)
            finally:
                if (connection):
                    connection.close()
                    print("Соединение с SQLite закрыто")
        pass

    def add_event(self, event: plan_event):
        try:
            connection = sqlite3.connect(self.name_db)
            cursor = connection.cursor()
            print("Успешно подключено к SQLite")

            sqlite_select_query = "select sqlite_version();"
            cursor.execute(sqlite_select_query)
            record = cursor.fetchall()
            print("Версия базы данных SQLite: ", record)
            cursor.close()

        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if (connection):
                connection.close()
                print("Соединение с SQLite закрыто")
