import sqlite3
from plan_manager import *
from PyQt5.QtCore import QTime, QDate

'''Названия таблиц:
events
time_from
time_to
date
tags
repeat_model
repeat_model_days
repeat_model_year
'''

name_db = 'events.db'


class Save_manager:
    def __init__(self, connection=None):
        try:
            with open(name_db, 'r') as f:
                pass
        except Exception as e:
            print('Файл базы данных не обнаружен, создание...')
            flag_connection = False
            try:
                if connection == None:
                    connection = sqlite3.connect(name_db)
                    flag_connection = True
                cursor = connection.cursor()

                query_table_events = '''CREATE TABLE events(
                id INTEGER PRIMARY KEY,
                name TEXT,
                description TEXT, 
                rm_id INTEGER);'''

                query_table_time_from = '''CREATE TABLE time_from(
                id INTEGER PRIMARY KEY,
                time INTEGER);'''

                query_table_time_to = '''CREATE TABLE time_to(
                id INTEGER PRIMARY KEY,
                time INTEGER);'''

                query_table_date = '''CREATE TABLE date(
                id INTEGER PRIMARY KEY,
                date INTEGER);'''

                query_table_tags = '''CREATE TABLE tags(
                id INTEGER,
                value TEXT,
                CONSTRAINT my_key PRIMARY KEY (id, value));'''

                query_table_repeat_model = '''CREATE TABLE repeat_model(
                id INTEGER PRIMARY KEY,
                type TEXT,
                interval INTEGER);'''

                query_table_repeat_model_days = '''CREATE TABLE repeat_model_days(
                id INTEGER,
                day INTEGER,
                CONSTRAINT my_key PRIMARY KEY (id, day));'''

                query_table_repeat_model_year = '''CREATE TABLE repeat_model_year(
                id INTEGER PRIMARY KEY,
                day INTEGER,
                month INTEGER);'''

                cursor.execute(query_table_events)
                cursor.execute(query_table_time_from)
                cursor.execute(query_table_time_to)
                cursor.execute(query_table_date)
                cursor.execute(query_table_tags)
                cursor.execute(query_table_repeat_model)
                cursor.execute(query_table_repeat_model_days)
                cursor.execute(query_table_repeat_model_year)
                connection.commit()
                cursor.close()
                print('Файл базы данных успешно создан.')
            except sqlite3.Error as error:
                print("Ошибка при создании базы данных", error)
            finally:
                if flag_connection and connection:
                    connection.close()
                    print("Соединение с SQLite закрыто")
        pass

    def save_event(self, event: plan_event, connection=None):
        flag_connection = False
        try:
            if connection is None:
                connection = sqlite3.connect(name_db)
                flag_connection = True

            cursor = connection.cursor()
            print("Успешно подключено к SQLite")

            rm_id = 0
            event_id = None
            if event.repeat_model is not None:
                repeat_inst = event.repeat_model
                query_repeat_model = f'''INSERT INTO repeat_model
                (type, interval)
                VALUES ('{repeat_inst.type}', {repeat_inst.gap})
                '''
                cursor.execute(query_repeat_model)
                rm_id = cursor.lastrowid
                time_interval = event.repeat_model.time_interval
                match event.repeat_model.type:
                    case Gaps.week.value:
                        day_tuple = list(map(lambda x: (rm_id, x), time_interval.days_week[0]))
                        query_days = '''INSERT INTO repeat_model_days
                                        (id, day)
                                        VALUES (?,?)'''
                        cursor.executemany(query_days, day_tuple)
                    case Gaps.month.value:
                        day_tuple = list(map(lambda x: (rm_id, x), time_interval.days_month[0]))
                        query_days = '''INSERT INTO repeat_model_days
                                        (id, day)
                                        VALUES (?,?)'''
                        cursor.executemany(query_days, day_tuple)
                    case Gaps.year.value:
                        date_ = time_interval.date
                        query_day_month = f'''INSERT INTO repeat_model_year
                                        (id, day, month)
                                        VALUES ({rm_id}, {date_.day()}, {date_.month()})'''
                        cursor.execute(query_day_month)

            create_event(cursor, event, rm_id)

            connection.commit()
        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if flag_connection:
                connection.close()
                print("Соединение с SQLite закрыто")


def create_event(cursor, event, rm_id):
    query_event = f'''INSERT INTO events
                (name, description, rm_id)
                VALUES ('{event.name}', '{event.description}', {rm_id});'''
    cursor.execute(query_event)
    event_id = cursor.lastrowid

    time = event.time_from
    hour, minute = make_xx(time.hour(), time.minute())
    query_time_from = f'''INSERT INTO time_from
                (id, time)
                VALUES ({event_id}, time('{hour}:{minute}'))'''
    cursor.execute(query_time_from)

    time = event.time_to
    hour, minute = make_xx(time.hour(), time.minute())
    query_time_to = f'''INSERT INTO time_to
                (id, time)
                VALUES ({event_id}, time('{hour}:{minute}'))'''
    cursor.execute(query_time_to)

    date = event.date
    year, month, day = make_xx(date.year(), date.month(), date.day())
    query_date = f'''INSERT INTO date
                (id, date)
                VALUES ({event_id}, julianday('{year}-{month}-{day}'))'''
    cursor.execute(query_date)

    tag_set = set(event.tags)
    tag_tuple = list(map(lambda x: (event_id, x), tag_set))
    query_tags = '''INSERT INTO tags
                (id, value)
                VALUES (?,?)'''
    cursor.executemany(query_tags, tag_tuple)


def make_xx(*numbers) -> list:
    output = list()
    for i in numbers:
        if i < 10:
            output.append('0' + str(i))
        else:
            output.append((str(i)))
    return output


def convert_to_QTime(cursor, time_str):
    time = list(map(lambda x: int(x), time_str.split(':')))
    return QTime(time[0], time[1])


def convert_to_QDate(cursor, jdate):
    query_date = f"SELECT strftime('%Y-%m-%d', '{jdate}')"
    cursor.execute(query_date)
    date_list_raw = cursor.fetchall()
    date_list = (date_list_raw[0][0]).split('-')
    date = list(map(lambda x: int(x), date_list))
    return QDate(date[0], date[1], date[2])


def sql_reguest(cursor: sqlite3.Cursor, request: str):
    test = request
    cursor.execute(request)
    result = cursor.fetchall()
    return result


class Load_manager:
    from PyQt5.QtCore import QDate, QTime

    db_flag = True

    def __init__(self):
        try:
            with open(name_db, 'r'):
                pass
        except Exception as e:
            print('Файл базы данных не обнаружен')
            self.db_flag = False

    def find_events(self, date_from: QDate, date_to: QDate, connection=None) -> list:
        flag_connection = False
        try:
            if connection is None:
                connection = sqlite3.connect(name_db)
                flag_connection = True
            cursor = connection.cursor()
            print("Успешно подключено к SQLite")
            date = date_from
            year, month, day = make_xx(date.year(), date.month(), date.day())
            date_from_str = f'''{year}-{month}-{day}'''
            date = date_to
            year, month, day = make_xx(date.year(), date.month(), date.day())
            date_to_str = f'''{year}-{month}-{day}'''

            query_find_date = f'''SELECT id FROM date WHERE
             date BETWEEN julianday('{date_from_str}') AND julianday('{date_to_str}')'''
            cursor.execute(query_find_date)

            dates_ids_tuples = cursor.fetchall()
            dates_ids_list = list(map(lambda x: str(x[0]), dates_ids_tuples))

            return dates_ids_list
        except Exception as e:
            print('Не удалость отобрать events id по причине ', e)
        finally:
            if flag_connection and connection:
                connection.close()

    def load_events(self, date_from: QDate, date_to: QDate, connection=None) -> list:
        flag_connection = False
        try:
            if connection is None:
                connection = sqlite3.connect(name_db)
                flag_connection = True
            cursor = connection.cursor()

            query_repeat_models = f'''SELECT * FROM repeat_model'''
            cursor.execute(query_repeat_models)
            repeat_models_raw = cursor.fetchall()
            for i in repeat_models_raw:  # в этом цикле перебираются все rm_model и создаются для них
                # event'ы, оторые попадают в просматривамый промежуток
                rm_id = i[0]  # rm расшифровывается как repeat_model
                rm_type = i[1]
                query_events_rm = f'''SELECT id FROM events WHERE rm_id = {rm_id}'''
                cursor.execute(query_events_rm)
                events_rm_raw = cursor.fetchall()
                if len(events_rm_raw) == 0:  # если у перебираемого repeat_model нету event'ов, то он удаляется
                    query_rm_delete = f'''DELETE FROM repeat_model WHERE id = {rm_id}'''
                    cursor.execute(query_rm_delete)
                    if rm_type == Gaps.week.value or rm_type == Gaps.month.value:
                        query_rm_delete = f'''DELETE FROM repeat_model_days WHERE id = {rm_id}'''
                        cursor.execute(query_rm_delete)
                    else:
                        query_rm_delete = f'''DELETE FROM repeat_model_year WHERE id = {rm_id}'''
                        cursor.execute(query_rm_delete)
                    continue
                query_events_rm_int = list(map(lambda x: str(x[0]), events_rm_raw))
                query_events_rm_str = '(' + ', '.join(query_events_rm_int) + ')'

                query_last_entry_date = f'''SELECT * from date WHERE id IN {query_events_rm_str} AND
                date = (SELECT MAX(date) FROM date WHERE id IN {query_events_rm_str})'''

                cursor.execute(query_last_entry_date)
                last_entry_date = cursor.fetchall()[0]

                query_last_entry_event = f'''SELECT * FROM events WHERE id = {last_entry_date[0]}'''
                cursor.execute(query_last_entry_event)
                last_entry_event = cursor.fetchall()[0]

                query_last_entry_tfrom = f'''SELECT * FROM time_from WHERE id = {last_entry_date[0]}'''
                cursor.execute(query_last_entry_tfrom)
                last_entry_time_from = cursor.fetchall()[0]

                query_last_entry_tto = f'''SELECT * FROM time_to WHERE id = {last_entry_date[0]}'''
                cursor.execute(query_last_entry_tto)
                last_entry_time_to = cursor.fetchall()[0]

                query_last_entry_tags = f'''SELECT * FROM tags WHERE id = {last_entry_date[0]}'''
                cursor.execute(query_last_entry_tags)
                last_entry_tags = list(map(lambda x: x[1], cursor.fetchall()))

                e_event = plan_event()
                e_event.name = last_entry_event[1]
                e_event.description = last_entry_event[2]
                e_event.time_from = convert_to_QTime(cursor, last_entry_time_from[1])
                e_event.time_to = convert_to_QTime(cursor, last_entry_time_to[1])

                e_event.date = convert_to_QDate(cursor, last_entry_date[1])
                e_event.tags = last_entry_tags

                pass
                rm_interval = i[2]
                match rm_type:
                    case Gaps.day.value:
                        next_date = QDate(e_event.date.year(),
                                          e_event.date.month(),
                                          e_event.date.day())
                        next_date = next_date.addDays(rm_interval)
                        while date_to > next_date:
                            e_event.date = next_date
                            create_event(cursor, e_event, rm_id)
                            next_date = next_date.addDays(rm_interval)
                    case Gaps.week.value:
                        next_date = QDate(e_event.date.year(),
                                          e_event.date.month(),
                                          e_event.date.day())
                        next_date = next_date.addDays(rm_interval * 7)
                        while date_to > next_date:
                            query_days = f'''SELECT day FROM repeat_model_days WHERE id = {rm_id}'''
                            cursor.execute(query_days)
                            days = list(map(lambda x: x[0], cursor.fetchall()))

                            next_date_ = QDate(next_date.year(), next_date.month(), next_date.day())
                            for j in range(7):
                                next_date_ = next_date_.addDays(1)
                                try:
                                    days.index(next_date_.dayOfWeek())
                                    e_event.date = next_date_
                                    create_event(cursor, e_event, rm_id)
                                except Exception as e:
                                    pass
                            next_date = next_date.addDays(rm_interval * 7)
                    case Gaps.month.value:
                        next_date = QDate(e_event.date.year(),
                                          e_event.date.month(),
                                          e_event.date.day())
                        # next_date = next_date.addMonths(rm_interval)
                        while date_to > next_date:
                            query_days = f'''SELECT day FROM repeat_model_days WHERE id = {rm_id}'''
                            cursor.execute(query_days)
                            days = list(map(lambda x: x[0], cursor.fetchall()))

                            next_date_ = QDate(next_date.year(), next_date.month(), next_date.day())
                            for j in range(31):
                                next_date_ = next_date_.addDays(1)
                                try:
                                    days.index(next_date_.day() - 1)
                                    year, month, day = make_xx(next_date_.year(), next_date_.month(),
                                                               next_date_.day())
                                    month = '07'
                                    query = f'''SELECT id FROM date WHERE date = 
                                                                julianday('{year}-{month}-{day}')'''
                                    exiting_event_id = sql_reguest(cursor, query)
                                    if len(exiting_event_id) != 0:
                                        exiting_rm_id = sql_reguest(cursor,
                                                                    f'''SELECT rm_id FROM events WHERE id = {exiting_event_id[0][0]}''')
                                        if len(exiting_rm_id) != 0:
                                            if exiting_rm_id[0][0] == rm_id:
                                                continue
                                    e_event.date = next_date_
                                    create_event(cursor, e_event, rm_id)
                                    connection.commit()
                                except Exception as e:
                                    test = e
                                    pass
                            next_date = next_date.addMonths(rm_interval)
                    case Gaps.year.value:
                        next_date = QDate(e_event.date.year(),
                                          e_event.date.month(),
                                          e_event.date.day())
                        next_date = next_date.addYears(rm_interval)
                        while date_to > next_date:
                            query_year = f'''SELECT day, month FROM repeat_model_year WHERE id = {rm_id}'''
                            cursor.execute(query_year)
                            year_days = cursor.fetchall()[0]
                            next_date_ = QDate(next_date.year(), year_days[1], year_days[0])

                            e_event.date = next_date_
                            create_event(cursor, e_event, rm_id)
                            next_date = next_date.addYears(rm_interval)
                connection.commit()

            events_id_int = self.find_events(date_from, date_to, connection)
            events_id_str = '(' + ', '.join(map(lambda x: str(x), events_id_int)) + ')'

            query_events = f'''SELECT * FROM events WHERE id IN {events_id_str} ORDER BY id'''
            cursor.execute(query_events)
            events_raw = cursor.fetchall()

            query_time_from = f'''SELECT * FROM time_from WHERE id IN {events_id_str} ORDER BY id'''
            cursor.execute(query_time_from)
            time_from_raw = cursor.fetchall()

            query_time_to = f'''SELECT * FROM time_to WHERE id IN {events_id_str} ORDER BY id'''
            cursor.execute(query_time_to)
            time_to_raw = cursor.fetchall()

            query_date = f'''SELECT * FROM date WHERE id IN {events_id_str} ORDER BY id'''
            cursor.execute(query_date)
            date_raw = cursor.fetchall()

            events = list()
            for n, i in enumerate(events_raw):
                event = plan_event()
                event.id = i[0]
                event.name = i[1]
                event.description = i[2]
                event.time_from = convert_to_QTime(cursor, time_from_raw[n][1])
                event.time_to = convert_to_QTime(cursor, time_to_raw[n][1])
                event.date = convert_to_QDate(cursor, date_raw[n][1])

                events.append(event)
            return events
        except Exception as e:
            print('Загрузка не удалась по причине ', e)
            return []
        finally:
            if flag_connection and connection:
                connection.close()
