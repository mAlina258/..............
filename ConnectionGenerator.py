import pyodbc
from DataLogicLair.Options import *

def get_connection():
    options = Options()
    connection = pyodbc.connect(options.connection_string)
    return connection