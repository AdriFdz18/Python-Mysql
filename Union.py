import mysql.connector
import time 
import os

persona= input("Ingrese su nombre:")
entrada= input("Desea Ingresar al sistema:")



if entrada == 'si':

        print("Bienvenido {persona}" )

        #Registro para designar a que base de datos se va a conectar
        usuario = str(input("Ingrese el Usuario de su base de datos:"))
        direccion = str(input("Ingrese la direccion de su base de datos:"))
        puerta = str(input("Ingrese el puerto de su base de datos:"))
        clave = str(input("Ingrese la clave de su base de datos:"))
        basedatos = str(input("Ingrese el nombre de su base de datos:"))


        #Conectar a la base de datos
        conectando=mysql.connector.connect(user=usuario,host=direccion,port=puerta,password=clave,database=basedatos)
        cursor=conectando.cursor()


        continuar= str (input("\nFinalizo el ingreso de las credenciales?\n"))

    

        if continuar == 'si':

            def menu():
                """
                Función que limpia la pantalla y muestra nuevamente el menu
                """
                os.system('cls')  # NOTA para windows tienes que cambiar clear por cls
                print("1 - Insertar datos")
                print("2 - Modificar datos ")
                print("3 - Borrar datos")
                print("4 - Consulta datos")
                print("5 - Lista datos")
                print("6 - salir")


            while True:
                # Mostramos el menu
                menu()
                opcionmenu = input("Seleccione una opcion:")
    

               #Opcion 1
                if opcionmenu == "1":
                    print("")
                    query = "INSERT INTO datos (nombre,edad,fecha) VALUES (%s, %s,%s)"
                    nombre = input("Inserte el nombre: ")
                    edad = int(input("Inserte la edad:"))
                    fecha = time.strftime("%y%m%d")
                    cursor.execute(query,(nombre,edad,fecha))
                    conectando.commit()
                    print(cursor.rowcount, "record inserted.")
                    input("Has pulsado la opción 1...\npulsa una tecla para continuar")
                


                #Opcion 2 
                elif opcionmenu == "2":

                    print("")
                    busquedadeusuario=input("Buscar el nombre a modificar: ")
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
                    nuevonombre=input("Ingresa el nuevo nombre para actualizar:")

                    print("------------------------------------------------")
                    verifica=input("Estas seguro que este usario quieres modificar, si o no?")

                    if verifica=='si':
	                    modificando={'laide':Idaborrar,'nombrenuevo':nuevonombre}
	                    querymodifica="UPDATE datos SET nombre=(%(nombrenuevo)s) WHERE id=(%(laide)s)"
	                    cursor.execute(querymodifica,modificando)
	                    conectando.commit()
	                    print("La solicitud fue realizada con exito!!")
                    print("------------------------------------------------")
                    print(cursor.rowcount, "record inserted.")
                    input("Has pulsado la opción 2...\npulsa una tecla para continuar")



                    #Opcion3
                elif opcionmenu == "3":
                    busquedadeusuario = input("Buscar el nombre a borrar: ")
                    query = ("SELECT *FROM datos WHERE nombre LIKE '%s%%'" % busquedadeusuario)
                    cursor.execute(query)
                    print("\n")
                    print("Los datos que coincinden con la busqueda son:")

                    for (id, nombre, edad, fecha) in cursor:
                        print("id:{} nombre:{} edad:{} fecha:{}".format(id, nombre, edad, fecha))
                    print("\n")
                    print("---------------------------------------------")

                    Idaborrar = input("Ingresa el ID del nombre a borrar: ")
                    borra = {'nombre': Idaborrar}
                    queryparaID = "SELECT * FROM datos WHERE id=(%(nombre)s)"
                    cursor.execute(queryparaID, borra)
                    print("------------------------------------------------")
                    print("El ID solicitado corresponde a: ")
                    print("\n")
                    for (id, nombre, edad, fecha) in cursor:
                        print("id:{} nombre:{} edad:{} fecha:{}".format(id, nombre, edad, fecha))
                    print("\n")
                    print("------------------------------------------------")
                    verifica = input("Estas seguro que este usario quieres borrar, si o no?")

                    if verifica == 'si':
                        queryEliminaID = "DELETE FROM datos WHERE id=(%(nombre)s)"
                        cursor.execute(queryEliminaID, borra)
                        conectando.commit()
                        print("La solicitud fue realizada con exito!!")
                    print("------------------------------------------------")
                    print(cursor.rowcount, "record inserted.")
                    input("Has pulsado la opción 3...\npulsa una tecla para continuar")



                    # Opcion 4
                elif opcionmenu == "4" :
                    busquedadeusario = input("Ingresa en nombre del usuario a buscar: ")
                    query = ("SELECT * FROM datos WHERE  nombre LIKE '%s%%'" % busquedadeusario)
                    cursor.execute(query)
                    print("\n")
                    print("El resultado de la solicitud es: ")

                    for (id, nombre, edad, fecha) in cursor:
                        print("id:{} nombre:{} edad:{} fecha:{}".format(id, nombre, edad, fecha))
                    print(cursor.rowcount, "record inserted.")
                    input("Has pulsado la opción 4...\npulsa una tecla para continuar")


                elif opcionmenu == "5":
                    query = ("SELECT * FROM datos")
                    cursor.execute(query)

                    for (id, nombre, edad, fecha) in cursor:
                        print("id:{} nombre:{} edad:{} fecha:{}".format(id, nombre, edad, fecha))
                    print(cursor.rowcount, "record inserted.")
                    input("Has pulsado la opción 5...\npulsa una tecla para continuar")

                    #Opcion 6
                elif opcionmenu == "6":
                    cursor.close()
                    conectando.close()

                    print(cursor.rowcount, "record inserted.")
                    input("Has pulsado la opción 6...\npulsa una tecla para continuar")
                    break


                else:
                    print("")
                    input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

else :
    print("Gracias, Fin del sistema")
    