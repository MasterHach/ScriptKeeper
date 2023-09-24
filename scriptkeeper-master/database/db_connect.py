import config
import pyodbc


def connect_to_bd():
    conn_str = f'DRIVER={config.driver};' \
               f'SERVER={config.server};' \
               f'DATABASE={config.database};' \
               f'Trusted_Connection=yes;'
    conn = pyodbc.connect(conn_str)
    return conn.cursor()


cursor = connect_to_bd()
