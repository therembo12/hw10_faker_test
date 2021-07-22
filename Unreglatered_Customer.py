from _typeshed import Self


import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from config import *
from psycopg2 import Error
connection = psycopg2.connect(
    user=USER, password=PASSWORD, host=HOST, port=PORT, database='shop_db')
cursor = connection.cursor()
cursor.execute('SELECT VERSION()')

print('Commit Success')
if connection:
    print('Connection closed')
    cursor.close()
    connection.close()


class unregister_user:
    def __init__(self):
        pass

    @classmethod
    def get_product_info(self):
        pass
