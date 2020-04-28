import mysql.connector
from credenciales import *
from enlace import *

busquedadeusuario=raw_input("Buscar el nombre a modificar: ")
query=("SELECT *FROM datos WHERE nombre LIKE '%s%%'"%busquedadeusuario)
cursor.execute(query)
print("\n")
print("Los datos que coincinden con la busqueda son:")

for(id,nombre,edad,fecha) in cursor:
	print ("id:{} nombre:{} edad:{} fecha:{}".format(id,nombre,edad,fecha))
print("\n")
print("---------------------------------------------")

Idaborrar=input("Ingresa el ID del nombre a modificar: ")
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
nuevonombre=raw_input("Ingresa el nuevo nombre para actualizar:")

print("------------------------------------------------")
verifica=raw_input("Estas seguro que este usario quieres modificar, si o no?")

if verifica=='si':
	modificando={'laide':Idaborrar,'nombrenuevo':nuevonombre}
	querymodifica="UPDATE datos SET nombre=(%(nombrenuevo)s) WHERE id=(%(laide)s)"
	cursor.execute(querymodifica,modificando)
	conectando.commit()
	print("La solicitud fue realizada con exito!!")
print("------------------------------------------------")

cursor.close()
conectando.close()
