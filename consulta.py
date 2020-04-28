import mysql.connector
from credenciales import *
from enlace import *

busquedadeusario=input("Ingresa en nombre del usuario a buscar ")
query= ("SELECT * FROM datos WHERE  nombre LIKE '%s%%'"%busquedadeusario)
cursor.execute(query)
print("\n")
print("El resultado de la solicitud es: ")

for(id,nombre,edad,fecha) in cursor:
	print("id:{} nombre:{} edad:{} fecha:{}".format(id,nombre,edad,fecha))
cursor.close()
conectando.close()
