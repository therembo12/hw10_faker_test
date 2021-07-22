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
# add_city = """
#     INSERT INTO city (id,city_name,city_id) VALUES (%s, %s)
# """
for _ in range(50):
    add_city = """
    INSERT INTO city (id,city_name,country_id) VALUES (%s,%s)
"""
    cursor.executemany(add_city, fake.city())

connection.commit()
print('Commit Success')
if connection:
    print('Connection closed')
    cursor.close()
    connection.close()
