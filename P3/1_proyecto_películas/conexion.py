
import mysql.connector
from mysql.connector import Error


def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",      
        database="bd_peliculas"
    )
