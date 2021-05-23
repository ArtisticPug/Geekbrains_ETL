import os

import pandas as pd
import psycopg2

# Параметры соединения
conn_string_a = "host='localhost' port=54320 dbname='database_a' user='postgres' password='postgres'"  # источник
conn_string_b = "host='localhost' port=54321 dbname='database_b' user='postgres' password='postgres'"  # приемник
tables_list = []  # Список таблиц для переноса
# Создаем соединение (оно поддерживает контекстный менеджер)
# Создаем курсор - это специальный объект который делает запросы и получает их результаты
with psycopg2.connect(conn_string_a) as conn, conn.cursor() as cursor:
    # запрос к БД
    query = """
    SELECT * 
    FROM pg_catalog.pg_tables pt  
    WHERE schemaname = 'public'
    """
    cursor.execute(query)  # выполнение запроса
    # получение результата fetchall для всех записей fetchone для одной
    result = cursor.fetchall()
    for row in result:
        tables_list.append(row[1])

for table in tables_list:  # итерирую полученный ранее список таблиц
    # Данные из источника
    with psycopg2.connect(conn_string_a) as conn, conn.cursor() as cursor:
        # Извлекаем данные из postgres_a в файл
        # Команда чувствительна к режиму открытия файла нужен "w"
        with open('resultsfile.csv', 'w') as f:
            q = f"COPY {table} TO STDOUT WITH DELIMITER ',' CSV HEADER;"
            cursor.copy_expert(q, f)

    # Данные в приемник
    with psycopg2.connect(conn_string_b) as conn, conn.cursor() as cursor:
        # Записываем данные в postgres_b из файла
        # Команда чувствительна к режиму открытия файла нужен "r"
        with open('resultsfile.csv', 'r') as f:
            q = f"COPY {table} FROM STDIN WITH DELIMITER ',' CSV HEADER;"
            cursor.copy_expert(q, f)
