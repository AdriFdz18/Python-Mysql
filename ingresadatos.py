import mysql.connector
import time
from credenciales import *
from enlace import *



query = "INSERT INTO datos (nombre,edad,fecha) VALUES (%s, %s,%s)"
nombre = input("Inserte el nombre: ")
edad = int(input("Inserte la edad:"))
fecha = time.strftime("%y%m%d")


cursor.execute(query,(nombre,edad,fecha))
conectando.commit()
cursor.close()
conectando.close()
