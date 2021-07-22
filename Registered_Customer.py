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


class Registered_user:
    def __init__(self, firstname, lastname, city, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.city = city
        self.email = email
        self.password = password

    @classmethod
    def edit_self_info(self):
        pass

    def create_order(self):
        pass

    def delete_order(self):
        pass

    def get_product_info(self):
        pass
