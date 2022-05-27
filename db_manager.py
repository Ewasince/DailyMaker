import sqlite3
import numpy as np
from plan_manager import *

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

    def add_event(self, event: plan_event):
        try:
            connection = sqlite3.connect(self.name_db)
            with connection:
                cursor = connection.cursor()
                print("Успешно подключено к SQLite")

                is_repetable = None
                if event.repeat_model != None:
                    is_repetable = 1
                else:
                    is_repetable = 0
                query_event = f'''INSERT INTO events
                (name, description, is_repetable INTEGER)
                VALUES ({event.name}, {event.description}, {is_repetable});'''
                cursor.execute(query_event)
                id = cursor.lastrowid

                time = event.time_from
                query_time_from = f'''INSERT INTO time_from
                (id, hour, minute)
                VALUES ({id}, {time.hour}, {time.minute})
                '''
                cursor.execute(query_time_from)

                time = event.time_to
                query_time_to = f'''INSERT INTO time_to
                (id, hour, minute)
                VALUES ({id}, {time.hour}, {time.minute})
                '''
                cursor.execute(query_time_to)

                date = event.date
                query_date = f'''INSERT INTO date
                (id, year, month, day)
                VALUES ({id}, {date.year}, {date.day})
                '''
                cursor.execute(query_date)

                # tag_tuple =
                tag_tuple = list(map(lambda x: (id, x), event.tags))
                # cursor.executemany('''INSERT INTO tags
                # (id, value)
                # VALUES (?,?)''', data_person_name)
                pass

                record = cursor.fetchall()
                print("Версия базы данных SQLite: ", record)
        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if (connection):
                connection.close()
                print("Соединение с SQLite закрыто")