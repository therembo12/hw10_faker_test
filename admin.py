# ADMIN INTERFACE
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


class Admin_interface:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def add_product(self):
        pass

    def add_product_category(self):
        pass

    def add_employee(self):
        pass

    def delete_product(self):
        pass

    def delete_product_category(self):
        pass

    def delete_employee(self):
        pass

    def delete_customer(self):
        pass

    def edit_product(self):
        pass

    def edit_product_category(self):
        pass

    def edit_employee(self):
        pass

    def get_order_info(self):
        pass
