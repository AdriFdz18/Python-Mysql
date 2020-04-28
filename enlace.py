import mysql.connector
from credenciales import *


conectando=mysql.connector.connect(user=usuario,host=direccion,port=puerta,password=clave,database=basedatos)
cursor=conectando.cursor()


