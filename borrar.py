import mysql.connector
from credenciales import *
from enlace import *

busquedadeusuario=raw_input("Buscar el nombre a borrar: ")
query=("SELECT *FROM datos WHERE nombre LIKE '%s%%'"%busquedadeusuario)
cursor.execute(query)
print("\n")
print("Los datos que coincinden con la busqueda son:")

for(id,nombre,edad,fecha) in cursor:
	print ("id:{} nombre:{} edad:{} fecha:{}".format(id,nombre,edad,fecha))
print("\n")
print("---------------------------------------------")

Idaborrar=input("Ingresa el ID del nombre a borrar: ")
borra={'nombre':Idaborrar}
queryparaID="SELECT * FROM datos WHERE id=(%(nombre)s)"
cursor.execute(queryparaID,borra)
print("------------------------------------------------")
print("El ID solicitado corresponde a: ")
print("\n")
for(id,nombre,edad,fecha) in cursor:
	print ("id:{} nombre:{} edad:{} fecha:{}".format(id,nombre,edad,fecha))
print("\n")
print("------------------------------------------------")
verifica=raw_input("Estas seguro que este usario quieres borrar, si o no?")

if verifica=='si':
	queryEliminaID="DELETE FROM datos WHERE id=(%(nombre)s)"
	cursor.execute(queryEliminaID,borra)
	conectando.commit()
	print("La solicitud fue realizada con exito!!")
print("------------------------------------------------")

cursor.close()
conectando.close()
