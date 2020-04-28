import mysql.connector
from credenciales import *
from enlace import *


query=("SELECT * FROM datos")
cursor.execute(query)

for(id,nombre,edad,fecha) in cursor:
	print("id:{} nombre:{} edad:{} fecha:{}".format(id,nombre,edad,fecha))
cursor.close()
conectando.close()

