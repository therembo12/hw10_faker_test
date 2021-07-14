# Update data base shop_db

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from config import *
from psycopg2 import Error
from faker import Faker
fake = Faker()
connection = psycopg2.connect(
    user=USER, password=PASSWORD, host=HOST, port=PORT, database='shop_db')
cursor = connection.cursor()
cursor.execute('SELECT VERSION()')
add_city = """
    INSERT INTO city (id,city_name,city_id) VALUES (%s, %s)
"""
city_list = []
city_tuple = ()
for _ in range(50):
    city_tuple[_] = f"{fake.city()}"
    city_list.append(city_tuple[_])
cursor.execute(add_city, city_tuple)
print(city_tuple)
connection.commit()
print('Commit Success')
if connection:
    print('Connection closed')
    cursor.close()
    connection.close()
