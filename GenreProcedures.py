import pyodbc
from ConnectionGenerator import *
from Options import *

class Genre():
    def __init__(self):
        self.__options = Options()

    def add_values_in_genre(self, name):
        cnc = get_connection()
        cursor = cnc.cursor()
        query = self.__options.add_jenre + f"{name}"
        cursor.execute(query)
        cnc.commit()
        cnc.close()

    def delete_genre(self, id):
        cnc = get_connection()
        cursor = cnc.cursor()
        cursor.execute(f"DeleteGenre {id}")
        cnc.commit()
        cnc.close()

    def update_genre(self, id, name):
        cnc = get_connection()
        cursor = cnc.cursor()
        cursor.execute(f"UpdateGenre {id}, {name}")
        cnc.commit()
        cnc.close()

    def get_genre_by_user(self):
        cursor = get_connection().cursor()
        query = self.__options.get_genre_by_user
        cursor.execute(query)
        return cursor.fetchall()

    def get_users_and_genre(self):
        cursor = get_connection().cursor()
        query = self.__options.get_users_and_genre
        cursor.execute(query)
        return cursor.fetchall()
