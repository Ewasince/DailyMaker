import sqlite3
import numpy as np
from plan_manager import *

import datetime

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

class save_manager():
    def __init__(self):
        try:
            with open(self.name_db, 'r') as f:
                pass
        except Exception as e:
            print('Файл базы данных не обнаружен, создание...')
            try:
                connection = sqlite3.connect(name_db)
                cursor = connection.cursor()

                query_table_events = '''CREATE TABLE events(
                id INTEGER PRIMARY KEY,
                name TEXT,
                description TEXT, 
                is_repetable INTEGER);'''

                query_table_time_from = '''CREATE TABLE time_from(
                id INTEGER PRIMARY KEY,
                hour INTEGER,
                minute INTEGER);'''

                query_table_time_to = '''CREATE TABLE time_to(
                id INTEGER PRIMARY KEY,
                hour INTEGER,
                minute INTEGER);'''

                query_table_date = '''CREATE TABLE date(
                id INTEGER PRIMARY KEY,
                year INTEGER,
                month INTEGER,
                day INTEGER);'''

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
                if (connection):
                    connection.close()
                    print("Соединение с SQLite закрыто")
        pass

    def save_event(self, event: plan_event):
        try:
            connection = sqlite3.connect(name_db)
            with connection:
                # test_date = datetime.
                cursor = connection.cursor()
                print("Успешно подключено к SQLite")

                is_repetable = None
                if event.repeat_model != None:
                    is_repetable = 1
                else:
                    is_repetable = 0
                query_event = f'''INSERT INTO events
                (name, description, is_repetable)
                VALUES ('{event.name}', '{event.description}', {is_repetable});'''
                cursor.execute(query_event)
                id = cursor.lastrowid

                time = event.time_from
                query_time_from = f'''INSERT INTO time_from
                (id, hour, minute)
                VALUES ({id}, {time.hour()}, {time.minute()})
                '''
                cursor.execute(query_time_from)

                time = event.time_to
                query_time_to = f'''INSERT INTO time_to
                (id, hour, minute)
                VALUES ({id}, {time.hour()}, {time.minute()})
                '''
                cursor.execute(query_time_to)

                date = event.date
                query_date = f'''INSERT INTO date
                (id, year, month, day)
                VALUES ({id}, {date.year()}, {date.month()},{date.day()})
                '''
                cursor.execute(query_date)

                tag_set = set(event.tags)
                tag_tuple = list(map(lambda x: (id, x), tag_set))
                query_tags = '''INSERT INTO tags
                (id, value)
                VALUES (?,?)'''
                cursor.executemany(query_tags, tag_tuple)

                if event.repeat_model != None:
                    repeat_inst = event.repeat_model
                    query_repeat_model = f'''INSERT INTO repeat_model
                    (id, type, interval)
                    VALUES ({id}, '{repeat_inst.type}', {repeat_inst.gap})
                    '''
                    cursor.execute(query_repeat_model)
                    time_interval = event.repeat_model.time_interval
                    match event.repeat_model.type:
                        case Gaps.week.value:
                            day_tuple = list(map(lambda x: (id, x), time_interval.days_week[0]))
                            query_days = '''INSERT INTO repeat_model_days
                                            (id, day)
                                            VALUES (?,?)'''
                            cursor.executemany(query_days, day_tuple)
                        case Gaps.month.value:
                            day_tuple = list(map(lambda x: (id, x), time_interval.days_month[0]))
                            query_days = '''INSERT INTO repeat_model_days
                                            (id, day)
                                            VALUES (?,?)'''
                            cursor.executemany(query_days, day_tuple)
                        case Gaps.year.value:
                            date_ = time_interval.date
                            query_day_month = f'''INSERT INTO repeat_model_year
                                            (id, day, month)
                                            VALUES ({id},{date_.day()}, {date_.month()})'''
                            cursor.execute(query_day_month)
                connection.commit()
        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if (connection):
                connection.close()
                print("Соединение с SQLite закрыто")

class load_manager():
    from PyQt5.QtCore import QDate
    from PyQt5.QtCore import QTime

    db_flag = True
    def __init__(self):
        try:
            with open(self.name_db, 'r'):
                pass
        except Exception as e:
            print('Файл базы данных не обнаружен')
            self.db_flag = False

    def find_events(self, connection, date_from: QDate, date_to: QDate,
                    time_from: QTime, time_to: QTime):
        cursor = connection.cursor()
        print("Успешно подключено к SQLite")

        query_find_date = f'''SELECT DISTINCT id FROM date WHERE
         year BETWEEN {date_from.year()} AND {date_to.year()} AND
         month BETWEEN {date_from.month()} AND {date_to.month()} AND
         day BETWEEN {date_from.day()} AND {date_to.day()}
         '''
        cursor.execute(query_find_date)

        dates_ids_tuples = cursor.fetchall()
        dates_ids_set = list(map(lambda x: str(x[0]), dates_ids_tuples))
        string_ids = '(' + ', '.join(dates_ids_set) + ')'
        query_find_time = f'''SELECT DISTINCT id from time_from WHERE
        id IN {string_ids} AND
        hour BETWEEN {time_from.hour()} AND {time_to.hour()} AND
        minute BETWEEN {time_from.minute()} AND {time_to.minute()};
        '''
        cursor.execute(query_find_time)

        time_ids_tuples = cursor.fetchall()
        time_ids_set = list(map(lambda x: x[0], time_ids_tuples))

        return time_ids_set

    def load_events(self, date_from: QDate, date_to: QDate,
                    time_from: QTime, time_to: QTime):

        connection = sqlite3.connect(name_db)
        with connection:
            cursor = connection.cursor()
            events_id_int = self.find_events(connection, date_from, date_to, time_from, time_to)
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

            query_repeat_models = f'''SELECT * FROM repeat_models'''
            cursor.execute(query_repeat_models)
            repeat_models_raw = cursor.fetchall()

            pass
