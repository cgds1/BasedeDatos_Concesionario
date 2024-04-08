import psycopg2
from psycopg2 import DatabaseError
import os
from tabulate import tabulate

# Modificar o eliminar registro de cada entidad en la base de datos Solo administradores. #

def menu():
    print("-- Centro de modificaciones --")
    print("1. Vehiculo                   ")
    print("2. Proveedor                  ")
    print("3. Taller                     ")
    print("4. Evento                     ")
    print("5. Carrera                    ")
    print("6. Repuesto                   ")
    print("7. Factura                    ")
    print("8. Empleado                   ")
    print("9. Ente                       ")
    print("10. Salir                     ")

def menu2():
    print("-- Qué desea hacer? --")
    print("1. Modificar")
    print("2. Eliminar")

def cls():
    if os.name == "nt":
        os.system("cls")
    else: 
        os.system("clear")

def presiona(x):
    x = input("Presiona para continuar...")

def main():
    cls()
    try:
        connection_string = "postgresql://concesionaria_owner:WtN7HmGxF9pg@ep-weathered-glitter-a4gsgrak.us-east-1.aws.neon.tech/CONCESIONARIA?sslmode=require"
        connection = psycopg2.connect(connection_string)
        cursor = connection.cursor()

        us = input("Ingresa tu usuario: ")
        password = input("Ingresa tu clave: ")
        
        cursor.execute("SELECT * FROM admin")
        datos = cursor.fetchall()
        
        bandera = False
        
        for elements in datos:
            if us == elements[1] and password == elements[2]:
                bandera = True
                
        if bandera == False:
            print(f"El usuario {us} no se ha encontrado en la base de datos")
            x1 = None
            presiona(x1)
        else: 
            while(True):
                cls()
                print(f"Bienvenido {us}. \n")
                menu()
                opc = input("\nPor favor, ingrese una opción: ")

                if opc == "1":
                    cls()
                    cursor.execute("SELECT * FROM vehiculo")
                    datos = cursor.fetchall()

                    menu2()
                    opc2 = input("\nPor favor, ingrese una opción: ")

                    if opc2 == "1":
                        try:
                            opctabla = input("Quieres ver la tabla de datos?(1 = Si)(2 = No) \n->")
                            if opctabla == "1":
                                column_names = [description[0] for description in cursor.description]
                                tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                print(tabla)

                            vin = input("Ingrese el VIM del vehiculo:  ")
                            cls()

                        except:
                            print("Error en la coleccion de datos.")

                        while (True):
                            cls()
                            cursor.execute(f"SELECT * FROM vehiculo WHERE vin_vehiculo = '{vin}'")
                            datos = cursor.fetchall()
                            
                            if not datos:
                                print("VIM no existente. ")
                                x1 = None
                                presiona(x1)
                                break
                            else:
                                column_names = [description[0] for description in cursor.description]
                                tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                print(tabla)

                                print("-- Qué desea actualizar? --")
                                print("1. VIN ")
                                print("2. Precio ")
                                print("3. Color ")
                                print("4. Kilometraje ")
                                print("5. Matricula ")
                                print("6. Salir ")
                                carro = input("Porfavor, Ingrese una opción: ")
                                if carro == "1":
                                    try:

                                        cls()

                                        column_names = [description[0] for description in cursor.description]
                                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                        print(tabla)

                                        nuevo_vin = input("Ingrese su nuevo VIM: ")
                                        cursor.execute(f"UPDATE vehiculo SET vin_vehiculo = '{nuevo_vin}' WHERE vin_vehiculo = '{vin}'")
                                        connection.commit()
                                        break

                                    except:
                                        print("Error en la actualizacion de datos. ")
                                
                                elif carro == "2":
                                    try:
                                        cls()

                                        column_names = [description[0] for description in cursor.description]
                                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                        print(tabla)

                                        nuevo_precio = input("Ingrese su nuevo precio: ")
                                        cursor.execute(f"UPDATE vehiculo SET precio = {nuevo_precio} WHERE vin_vehiculo = '{vin}'")
                                        connection.commit()

                                    except:
                                        print("Error en la actualizacion de datos. ")

                                elif carro == "3":
                                    try:
                                        cls()

                                        column_names = [description[0] for description in cursor.description]
                                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                        print(tabla)

                                        nuevo_color = input("Ingrese su nuevo color: ")
                                        cursor.execute(f"UPDATE vehiculo SET color = '{nuevo_color}' WHERE vin_vehiculo = '{vin}'")
                                        connection.commit()

                                    except:
                                        print("Error en la actualizacion de datos. ")

                                elif carro == "4":
                                    try:

                                        cls()

                                        column_names = [description[0] for description in cursor.description]
                                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                        print(tabla)

                                        nuevo_km = input("Ingrese su nuevo kilometraje: ")
                                        cursor.execute(f"UPDATE vehiculo SET kilometraje = {nuevo_km} WHERE vin_vehiculo = '{vin}'")
                                        connection.commit()

                                    except:
                                        print("Error en la actualizacion de datos. ")

                                elif carro == "5":
                                    try:

                                        cls()

                                        column_names = [description[0] for description in cursor.description]
                                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                        print(tabla)

                                        nuevo_matricula = input("Ingrese su nueva matricula: ")
                                        cursor.execute(f"UPDATE vehiculo SET matricula_vehiculo = '{nuevo_matricula}' WHERE vin_vehiculo = '{vin}'")
                                        connection.commit()

                                    except:
                                        print("Error en la actualizacion de datos. ")
                                elif carro == "6":
                                    break
                                    
                    elif opc2 == "2":
                        try:
                            opctabla = input("Quieres ver la tabla de datos?(1 = Si)(2 = No) \n->")
                            if opctabla == "1":
                                column_names = [description[0] for description in cursor.description]
                                tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                print(tabla)

                            vin = input("Ingrese el VIM del vehiculo:  ")
                            cls()

                        except:
                            print("Error en la coleccion de datos.")
                            
                        cursor.execute(f"SELECT * FROM vehiculo WHERE vin_vehiculo = '{vin}'")
                        datos = cursor.fetchall()
                        
                        if not datos:
                            print("VIN no existente. ")
                            x1 = None
                            presiona(x1)
                        else:
                            column_names = [description[0] for description in cursor.description]
                            tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                            print(tabla)

                            print("-- Seguro que desea borrar el vehiculo? --")
                            carro = input("-> ")
                            if carro == 'Si' or 'si' or 'sI' or 'yes' or 'Yes' or 'yEs' or 'yeS' or 'YeS' or 'yES' or 'YEs':
                                try:

                                    cls()
                                    cursor.execute(f"DELETE FROM vehiculo WHERE vin_vehiculo ='{vin}'")
                                    connection.commit()
                                    print("Borrado exitoso. ")
                                    x1 = None
                                    presiona(x1)
                                except:
                                    print("Error en el borrado de datos. ")
                            else:
                                break
                
                elif opc == "2":
                    cls()
                    cursor.execute("SELECT * FROM proveedor")
                    datos = cursor.fetchall()

                    menu2()
                    opc2 = input("\nPor favor, ingrese una opción: ")

                    if opc2 == "1":
                        try:
                            opctabla = input("Quieres ver la tabla de datos?(1 = Si)(2 = No) \n->")
                            if opctabla == "1":
                                column_names = [description[0] for description in cursor.description]
                                tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                print(tabla)

                            vin = input("Ingrese el RIF del proveedor (Solo el numero):  ")
                            proveedor = "J"+vin
                            print(proveedor)
                            cls()

                        except:
                            print("Error en la coleccion de datos.")

                        while (True):
                            cls()
                            cursor.execute(f"SELECT * FROM proveedor WHERE rif_proveedor = '{proveedor}'")
                            datos = cursor.fetchall()
                            if not datos:
                                print("RIF no existente. ")
                                x1 = None
                                presiona(x1)
                                break
                            else:
                                column_names = [description[0] for description in cursor.description]
                                tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                print(tabla)

                                print("-- Qué desea actualizar? --")
                                print("1. RIF ")
                                print("2. Nombre ")
                                print("3. Direccion ")
                                print("4. Salir ")
                                opc3 = input("Porfavor, Ingrese una opción: ")
                                if opc3 == "1":
                                    try:

                                        cls()

                                        column_names = [description[0] for description in cursor.description]
                                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                        print(tabla)

                                        nuevo_rif = input("Ingrese su nuevo RIF(Solo numeros): ")
                                        result = "J"+nuevo_rif
                                        cursor.execute(f"UPDATE proveedor SET rif_proveedor = '{result}' WHERE rif_proveedor = '{proveedor}'")
                                        connection.commit()
                                        print("Modificación existosa. ")
                                        x1 = None
                                        presiona(x1)
                                        break

                                    except:
                                        print("Error en la actualizacion de datos. ")
                                        break
                                
                                elif opc3 == "2":
                                    try:
                                        cls()

                                        column_names = [description[0] for description in cursor.description]
                                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                        print(tabla)

                                        nuevo_nombre = input("Ingrese su nuevo nombre: ")
                                        cursor.execute(f"UPDATE proveedor SET nombre = '{nuevo_nombre}' WHERE rif_proveedor = '{proveedor}'")
                                        connection.commit()
                                        print("Modificación existosa. ")
                                        x1 = None
                                        presiona(x1)
                                        break

                                    except:
                                        print("Error en la actualizacion de datos. ")
                                        break

                                elif opc3 == "3":
                                    try:
                                        cls()

                                        column_names = [description[0] for description in cursor.description]
                                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                        print(tabla)

                                        nueva_direccion = input("Ingrese su nueva direccion: ")
                                        cursor.execute(f"UPDATE proveedor SET direccion = '{nueva_direccion}' WHERE rif_proveedor = '{proveedor}'")
                                        connection.commit()
                                        print("Modificación existosa. ")
                                        x1 = None
                                        presiona(x1)
                                        break

                                    except:
                                        print("Error en la actualizacion de datos. ")
                                        break

                                elif opc3 == "4":
                                    break
                            
                    elif opc2 == "2":
                        try:
                            opctabla = input("Quieres ver la tabla de datos?(1 = Si)(2 = No) \n->")
                            if opctabla == "1":
                                column_names = [description[0] for description in cursor.description]
                                tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                print(tabla)

                            RIF = input("Ingrese el RIF del proveedor (SOLO EN NUMEROS):  ")
                            result = "J"+RIF
                            cls()

                        except:
                            print("Error en la coleccion de datos.")
                            
                        cursor.execute(f"SELECT * FROM proveedor WHERE rif_proveedor = '{result}'")
                        datos = cursor.fetchall()
                        
                        if not datos:
                            print("RIF no existente. ")
                            x1 = None
                            presiona(x1)
                        else:
                            column_names = [description[0] for description in cursor.description]
                            tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                            print(tabla)

                            print("-- Seguro que desea borrar el proveedor? --")
                            carro = input("-> ")
                            if carro == 'Si' or 'si' or 'sI' or 'yes' or 'Yes' or 'yEs' or 'yeS' or 'YeS' or 'yES' or 'YEs':
                                try:

                                    cls()
                                    cursor.execute(f"DELETE FROM proveedor WHERE rif_proveedor ='{result}'")
                                    connection.commit()
                                    print("Borrado exitoso. ")
                                    x1 = None
                                    presiona(x1)
                                except:
                                    print("Error en el borrado de datos. ")
                            else:
                                break
                
                elif opc == "3":
                    cls()
                    cursor.execute("SELECT * FROM taller")
                    datos = cursor.fetchall()

                    menu2()
                    opc2 = input("\nPor favor, ingrese una opción: ")

                    if opc2 == "1":
                        try:
                            opctabla = input("Quieres ver la tabla de datos?(1 = Si)(2 = No) \n->")
                            if opctabla == "1":
                                column_names = [description[0] for description in cursor.description]
                                tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                print(tabla)

                            RIF = input("Ingrese el RIF del taller (Solo el numero):  ")
                            taller = "J"+RIF
                            cls()

                        except:
                            print("Error en la coleccion de datos.")

                        while (True):
                            cls()
                            cursor.execute(f"SELECT * FROM taller WHERE rif_taller = '{taller}'")
                            datos = cursor.fetchall()
                            
                            if not datos:
                                print("RIF no existente. ")
                                x1 = None
                                presiona(x1)
                                break
                            else:
                                column_names = [description[0] for description in cursor.description]
                                tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                print(tabla)

                                print("-- Qué desea actualizar? --")
                                print("1. RIF ")
                                print("2. Nombre ")
                                print("3. Direccion ")
                                print("4. Salir ")
                                opc3 = input("Porfavor, Ingrese una opción: ")
                                if opc3 == "1":
                                    try:

                                        cls()

                                        column_names = [description[0] for description in cursor.description]
                                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                        print(tabla)

                                        nuevo_rif = input("Ingrese su nuevo RIF(Solo numeros): ")
                                        result = "J"+nuevo_rif
                                        cursor.execute(f"UPDATE taller SET rif_taller = '{result}' WHERE rif_taller = '{taller}'")
                                        connection.commit()
                                        print("Modificación existosa. ")
                                        x1 = None
                                        presiona(x1)
                                        break

                                    except:
                                        print("Error en la actualizacion de datos. ")
                                        break
                                
                                elif opc3 == "2":
                                    try:
                                        cls()

                                        column_names = [description[0] for description in cursor.description]
                                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                        print(tabla)

                                        nuevo_nombre = input("Ingrese su nuevo nombre: ")
                                        cursor.execute(f"UPDATE taller SET nombre = '{nuevo_nombre}' WHERE rif_taller = '{taller}'")
                                        connection.commit()
                                        print("Modificación existosa. ")
                                        x1 = None
                                        presiona(x1)
                                        break

                                    except:
                                        print("Error en la actualizacion de datos. ")
                                        break

                                elif opc3 == "3":
                                    try:
                                        cls()

                                        column_names = [description[0] for description in cursor.description]
                                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                        print(tabla)

                                        nueva_direccion = input("Ingrese su nueva direccion: ")
                                        cursor.execute(f"UPDATE taller SET direccion = '{nueva_direccion}' WHERE rif_taller = '{taller}'")
                                        connection.commit()
                                        print("Modificación existosa. ")
                                        x1 = None
                                        presiona(x1)
                                        break

                                    except:
                                        print("Error en la actualizacion de datos. ")
                                        break

                                elif opc3 == "4":
                                    break
                            
                    elif opc2 == "2":
                        try:
                            opctabla = input("Quieres ver la tabla de datos?(1 = Si)(2 = No) \n->")
                            if opctabla == "1":
                                column_names = [description[0] for description in cursor.description]
                                tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                print(tabla)

                            RIF = input("Ingrese el RIF del taller (SOLO EN NUMEROS):  ")
                            result = "J"+RIF
                            cls()

                        except:
                            print("Error en la coleccion de datos.")
                            
                        cursor.execute(f"SELECT * FROM taller WHERE rif_taller = '{result}'")
                        datos = cursor.fetchall()
                        
                        if not datos:
                            print("RIF no existente. ")
                            x1 = None
                            presiona(x1)
                        else:
                            column_names = [description[0] for description in cursor.description]
                            tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                            print(tabla)

                            print("-- Seguro que desea borrar el taller? --")
                            carro = input("-> ")
                            if carro == 'Si' or 'si' or 'sI' or 'yes' or 'Yes' or 'yEs' or 'yeS' or 'YeS' or 'yES' or 'YEs':
                                try:

                                    cls()
                                    cursor.execute(f"DELETE FROM taller WHERE rif_taller ='{result}'")
                                    connection.commit()
                                    print("Borrado exitoso. ")
                                    x1 = None
                                    presiona(x1)
                                except:
                                    print("Error en el borrado de datos. ")
                            else:
                                break
                
                elif opc == "4":
                    cls()
                    cursor.execute("SELECT * FROM evento")
                    datos = cursor.fetchall()

                    menu2()
                    opc2 = input("\nPor favor, ingrese una opción: ")

                    if opc2 == "1":
                        try:
                            opctabla = input("Quieres ver la tabla de datos?(1 = Si)(2 = No) \n->")
                            if opctabla == "1":
                                column_names = [description[0] for description in cursor.description]
                                tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                print(tabla)

                            id = input("Ingrese el ID del evento:  ")
                            cls()

                        except:
                            print("Error en la coleccion de datos.")

                        while (True):
                            cls()
                            cursor.execute(f"SELECT * FROM evento WHERE id_evento = '{id}'")
                            datos = cursor.fetchall()
                            
                            if not datos:
                                print(" no existente. ")
                                x1 = None
                                presiona(x1)
                                break
                            else:
                                column_names = [description[0] for description in cursor.description]
                                tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                print(tabla)

                                print("-- Qué desea actualizar? --")
                                print("1. Nombre ")
                                print("2. Descripcion ")
                                print("3. fecha ")
                                print("4. Salir ")
                                opc3 = input("Porfavor, Ingrese una opción: ")
                                if opc3 == "1":
                                    try:

                                        cls()

                                        column_names = [description[0] for description in cursor.description]
                                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                        print(tabla)

                                        nuevo_nombre = input("Ingrese su nuevo nombre: ")
                                        cursor.execute(f"UPDATE evento SET nombre = '{nuevo_nombre}' WHERE id_evento = '{id}'")
                                        connection.commit()
                                        print("Modificación existosa. ")
                                        x1 = None
                                        presiona(x1)
                                        break

                                    except:
                                        print("Error en la actualizacion de datos. ")
                                        break
                                
                                elif opc3 == "2":
                                    try:
                                        cls()

                                        column_names = [description[0] for description in cursor.description]
                                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                        print(tabla)

                                        nueva_desc = input("Ingrese su nueva descripcion: ")
                                        cursor.execute(f"UPDATE evento SET descripcion = '{nueva_desc}' WHERE id_evento = '{id}'")
                                        connection.commit()
                                        print("Modificación existosa. ")
                                        x1 = None
                                        presiona(x1)
                                        break

                                    except:
                                        print("Error en la actualizacion de datos. ")
                                        break

                                elif opc3 == "3":
                                    try:
                                        cls()

                                        column_names = [description[0] for description in cursor.description]
                                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                        print(tabla)

                                        nueva_fecha = input("Ingrese su nueva fecha(YYYY-MM-DD): ")
                                        cursor.execute(f"UPDATE evento SET fecha = '{nueva_fecha}' WHERE id_evento = '{id}'")
                                        connection.commit()
                                        print("Modificación existosa. ")
                                        x1 = None
                                        presiona(x1)
                                        break

                                    except:
                                        print("Error en la actualizacion de datos. ")
                                        break

                                elif opc3 == "4":
                                    break
                            
                    elif opc2 == "2":
                        try:
                            opctabla = input("Quieres ver la tabla de datos?(1 = Si)(2 = No) \n->")
                            if opctabla == "1":
                                column_names = [description[0] for description in cursor.description]
                                tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                print(tabla)

                            id = input("Ingrese el ID del evento:  ")
                            cls()

                        except:
                            print("Error en la coleccion de datos.")
                            
                        cursor.execute(f"SELECT * FROM evento WHERE id_evento = '{id}'")
                        datos = cursor.fetchall()
                        
                        if not datos:
                            print("ID no existente. ")
                            x1 = None
                            presiona(x1)
                        else:
                            column_names = [description[0] for description in cursor.description]
                            tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                            print(tabla)

                            print("-- Seguro que desea borrar el evento? --")
                            carro = input("-> ")
                            if carro == 'Si' or 'si' or 'sI' or 'yes' or 'Yes' or 'yEs' or 'yeS' or 'YeS' or 'yES' or 'YEs':
                                try:

                                    cls()
                                    cursor.execute(f"DELETE FROM evento WHERE id_evento ='{id}'")
                                    connection.commit()
                                    print("Borrado exitoso. ")
                                    x1 = None
                                    presiona(x1)
                                except:
                                    print("Error en el borrado de datos. ")
                            else:
                                break
                    
                elif opc == "5":
                    cls()
                    cursor.execute("SELECT * FROM carrera")
                    datos = cursor.fetchall()

                    menu2()
                    opc2 = input("\nPor favor, ingrese una opción: ")

                    if opc2 == "1":
                        try:
                            opctabla = input("Quieres ver la tabla de datos?(1 = Si)(2 = No) \n->")
                            if opctabla == "1":
                                column_names = [description[0] for description in cursor.description]
                                tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                print(tabla)

                            id = input("Ingrese el ID de la carrera:  ")
                            cls()

                        except:
                            print("Error en la coleccion de datos.")

                        while (True):
                            cls()
                            cursor.execute(f"SELECT * FROM carrera WHERE id_carrera = '{id}'")
                            datos = cursor.fetchall()
                            if not datos:
                                print("ID no existente. ")
                                x1 = None
                                presiona(x1)
                                break
                            else:
                                column_names = [description[0] for description in cursor.description]
                                tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                print(tabla)

                                print("-- Qué desea actualizar? --")
                                print("1. Numero de Vueltas ")
                                print("2. Nombre de Carrera ")
                                print("3. Nombre del Circuito ")
                                print("4. Tipo de la carrera ")
                                print("5. Premio ")
                                print("6. Fecha ")
                                print("7. Salir ")
                                opc3 = input("Porfavor, Ingrese una opción: ")
                                if opc3 == "1":
                                    try:

                                        cls()

                                        column_names = [description[0] for description in cursor.description]
                                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                        print(tabla)

                                        num_vueltas = input("Ingrese su nuevo numero de vueltas: ")
                                        cursor.execute(f"UPDATE carrera SET numero_vueltas = {num_vueltas} WHERE id_carrera = '{id}'")
                                        connection.commit()
                                        print("Modificación existosa. ")
                                        x1 = None
                                        presiona(x1)
                                        break

                                    except:
                                        print("Error en la actualizacion de datos. ")
                                        break
                                
                                elif opc3 == "2":
                                    try:
                                        cls()

                                        column_names = [description[0] for description in cursor.description]
                                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                        print(tabla)

                                        nombre_car = input("Ingrese su nuevo nombre de carrera: ")
                                        cursor.execute(f"UPDATE carrera SET nombre_carrera = '{nombre_car}' WHERE id_carrera = '{id}'")
                                        connection.commit()
                                        print("Modificación existosa. ")
                                        x1 = None
                                        presiona(x1)
                                        break

                                    except:
                                        print("Error en la actualizacion de datos. ")
                                        break

                                elif opc3 == "3":
                                    try:
                                        cls()

                                        column_names = [description[0] for description in cursor.description]
                                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                        print(tabla)

                                        nombre_cir = input("Ingrese su nuevo nombre del circuito: ")
                                        cursor.execute(f"UPDATE carrera SET nombre_circuito = '{nombre_cir}' WHERE id_carrera = '{id}'")
                                        connection.commit()
                                        print("Modificación existosa. ")
                                        x1 = None
                                        presiona(x1)
                                        break

                                    except:
                                        print("Error en la actualizacion de datos. ")
                                        break

                                elif opc3 == "4":
                                    try:
                                        cls()

                                        column_names = [description[0] for description in cursor.description]
                                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                        print(tabla)

                                        tipo = input("Ingrese su nuevo tipo de carrera: ")
                                        cursor.execute(f"UPDATE carrera SET tipo_carrera = '{tipo}' WHERE id_carrera = '{id}'")
                                        connection.commit()
                                        print("Modificación existosa. ")
                                        x1 = None
                                        presiona(x1)
                                        break

                                    except:
                                        print("Error en la actualizacion de datos. ")
                                        break
                                    
                                elif opc3 == "5":
                                    try:
                                        cls()

                                        column_names = [description[0] for description in cursor.description]
                                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                        print(tabla)

                                        premio = input("Ingrese su nuevo premio: ")
                                        cursor.execute(f"UPDATE carrera SET premio = {premio} WHERE id_carrera = '{id}'")
                                        connection.commit()
                                        print("Modificación existosa. ")
                                        x1 = None
                                        presiona(x1)
                                        break

                                    except:
                                        print("Error en la actualizacion de datos. ")
                                        break
                                    
                                elif opc3 == "6":
                                    try:
                                        cls()

                                        column_names = [description[0] for description in cursor.description]
                                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                        print(tabla)

                                        fecha = input("Ingrese su nueva fecha (YYYY-MM-DD): ")
                                        cursor.execute(f"UPDATE carrera SET fecha = '{fecha}' WHERE id_carrera = '{id}'")
                                        connection.commit()
                                        print("Modificación existosa. ")
                                        x1 = None
                                        presiona(x1)
                                        break

                                    except:
                                        print("Error en la actualizacion de datos. ")
                                        break
                                
                                elif opc3 == "7":
                                    break
                            
                    elif opc2 == "2":
                        try:
                            opctabla = input("Quieres ver la tabla de datos?(1 = Si)(2 = No) \n->")
                            if opctabla == "1":
                                column_names = [description[0] for description in cursor.description]
                                tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                print(tabla)

                            id = input("Ingrese el ID de la carrera:  ")
                            cls()

                        except:
                            print("Error en la coleccion de datos.")
                            
                        cursor.execute(f"SELECT * FROM carrera WHERE id_carrera = '{id}'")
                        datos = cursor.fetchall()
                        
                        if not datos:
                            print("ID no existente. ")
                            x1 = None
                            presiona(x1)
                        else:
                            column_names = [description[0] for description in cursor.description]
                            tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                            print(tabla)

                            print("-- Seguro que desea borrar la carrera? --")
                            carro = input("-> ")
                            if carro == 'Si' or 'si' or 'sI' or 'yes' or 'Yes' or 'yEs' or 'yeS' or 'YeS' or 'yES' or 'YEs':
                                try:

                                    cls()
                                    cursor.execute(f"DELETE FROM evento WHERE id_evento ='{id}'")
                                    connection.commit()
                                    print("Borrado exitoso. ")
                                    x1 = None
                                    presiona(x1)
                                except:
                                    print("Error en el borrado de datos. ")
                            else:
                                break

                elif opc == "6":
                    cls()
                    cursor.execute("SELECT * FROM repuesto")
                    datos = cursor.fetchall()

                    menu2()
                    opc2 = input("\nPor favor, ingrese una opción: ")

                    if opc2 == "1":
                        try:
                            opctabla = input("Quieres ver la tabla de datos?(1 = Si)(2 = No) \n->")
                            if opctabla == "1":
                                column_names = [description[0] for description in cursor.description]
                                tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                print(tabla)

                            num = input("Ingrese el numero de la parte:  ")
                            cls()

                        except:
                            print("Error en la coleccion de datos.")

                        while (True):
                            cls()
                            cursor.execute(f"SELECT * FROM repuesto WHERE numero_parte = '{num}'")
                            datos = cursor.fetchall()
                            if not datos:
                                print("ID no existente. ")
                                x1 = None
                                presiona(x1)
                                break
                            else:
                                column_names = [description[0] for description in cursor.description]
                                tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                print(tabla)

                                print("-- Qué desea actualizar? --")
                                print("1. Numero de Parte ")
                                print("2. Nombre ")
                                print("3. Salir ")
                                opc3 = input("Porfavor, Ingrese una opción: ")
                                if opc3 == "1":
                                    try:

                                        cls()

                                        column_names = [description[0] for description in cursor.description]
                                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                        print(tabla)

                                        nuevo_num = input("Ingrese su nuevo numero de parte: ")
                                        cursor.execute(f"UPDATE repuesto SET numero_parte = '{nuevo_num}' WHERE numero_parte = '{num}'")
                                        connection.commit()
                                        print("Modificación existosa. ")
                                        x1 = None
                                        presiona(x1)
                                        break

                                    except:
                                        print("Error en la actualizacion de datos. ")
                                        break
                                
                                elif opc3 == "2":
                                    try:
                                        cls()

                                        column_names = [description[0] for description in cursor.description]
                                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                        print(tabla)

                                        nombre_repues = input("Ingrese su nuevo nombre de repuesto: ")
                                        cursor.execute(f"UPDATE repuesto SET nombre = '{nombre_repues}' WHERE numero_parte = '{num}'")
                                        connection.commit()
                                        print("Modificación existosa. ")
                                        x1 = None
                                        presiona(x1)
                                        break

                                    except:
                                        print("Error en la actualizacion de datos. ")
                                        break
                                elif opc3 == "3":
                                    break
                            
                    elif opc2 == "2":
                        try:
                            opctabla = input("Quieres ver la tabla de datos?(1 = Si)(2 = No) \n->")
                            if opctabla == "1":
                                column_names = [description[0] for description in cursor.description]
                                tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                print(tabla)

                            id = input("Ingrese el numero de la parte:  ")
                            cls()

                        except:
                            print("Error en la coleccion de datos.")
                            
                        cursor.execute(f"SELECT * FROM repuesto WHERE numero_parte = '{num}'")
                        datos = cursor.fetchall()
                        
                        if not datos:
                            print("ID no existente. ")
                            x1 = None
                            presiona(x1)
                        else:
                            column_names = [description[0] for description in cursor.description]
                            tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                            print(tabla)

                            print("-- Seguro que desea borrar el repuesto? --")
                            carro = input("-> ")
                            if carro == 'Si' or 'si' or 'sI' or 'yes' or 'Yes' or 'yEs' or 'yeS' or 'YeS' or 'yES' or 'YEs' or " ":
                                try:

                                    cls()
                                    cursor.execute(f"DELETE FROM repuesto WHERE numero_parte ='{num}'")
                                    connection.commit()
                                    print("Borrado exitoso. ")
                                    x1 = None
                                    presiona(x1)
                                except:
                                    print("Error en el borrado de datos. ")
                            else:
                                break
                            
                elif opc == "7":
                    cls()
                    cursor.execute("SELECT * FROM factura")
                    datos = cursor.fetchall()

                    menu2()
                    opc2 = input("\nPor favor, ingrese una opción: ")

                    if opc2 == "1":
                        try:
                            opctabla = input("Quieres ver la tabla de datos?(1 = Si)(2 = No) \n->")
                            if opctabla == "1":
                                column_names = [description[0] for description in cursor.description]
                                tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                print(tabla)

                            id = input("Ingrese el id de la factura:  ")
                            cls()

                        except:
                            print("Error en la coleccion de datos.")

                        while (True):
                            cls()
                            cursor.execute(f"SELECT * FROM factura WHERE id_factura = '{id}'")
                            datos = cursor.fetchall()
                            if not datos:
                                print("ID no existente. ")
                                x1 = None
                                presiona(x1)
                                break
                            else:
                                column_names = [description[0] for description in cursor.description]
                                tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                print(tabla)

                                print("-- Qué desea actualizar? --")
                                print("1. Dia ")
                                print("2. Hora ")
                                print("3. Salir ")
                                opc3 = input("Porfavor, Ingrese una opción: ")
                                if opc3 == "1":
                                    try:

                                        cls()

                                        column_names = [description[0] for description in cursor.description]
                                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                        print(tabla)

                                        Dia = input("Ingrese su nuevo dia (YYYY-MM-DD): ")
                                        cursor.execute(f"UPDATE factura SET dia = '{Dia}' WHERE id_factura = '{id}'")
                                        connection.commit()
                                        print("Modificación existosa. ")
                                        x1 = None
                                        presiona(x1)
                                        break

                                    except:
                                        print("Error en la actualizacion de datos. ")
                                        break
                                
                                elif opc3 == "2":
                                    try:
                                        cls()

                                        column_names = [description[0] for description in cursor.description]
                                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                        print(tabla)

                                        Hora = input("Ingrese su nueva hora (HH:MM:SS): ")
                                        cursor.execute(f"UPDATE factura SET hora = '{Hora}' WHERE id_factura = '{id}'")
                                        connection.commit()
                                        print("Modificación existosa. ")
                                        x1 = None
                                        presiona(x1)
                                        break

                                    except:
                                        print("Error en la actualizacion de datos. ")
                                        break
                                elif opc3 == "3":
                                    break
                            
                    elif opc2 == "2":
                        try:
                            opctabla = input("Quieres ver la tabla de datos?(1 = Si)(2 = No) \n->")
                            if opctabla == "1":
                                column_names = [description[0] for description in cursor.description]
                                tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                print(tabla)

                            id = input("Ingrese la id de la factura:  ")
                            cls()

                        except:
                            print("Error en la coleccion de datos.")
                            
                        cursor.execute(f"SELECT * FROM factura WHERE id_factura = '{id}'")
                        datos = cursor.fetchall()
                        
                        if not datos:
                            print("ID no existente. ")
                            x1 = None
                            presiona(x1)
                        else:
                            column_names = [description[0] for description in cursor.description]
                            tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                            print(tabla)

                            print("-- Seguro que desea borrar la factura? --")
                            carro = input("-> ")
                            if carro == 'Si' or 'si' or 'sI' or 'yes' or 'Yes' or 'yEs' or 'yeS' or 'YeS' or 'yES' or 'YEs' or " ":
                                try:

                                    cls()
                                    cursor.execute(f"DELETE FROM factura WHERE id_factura ='{id}'")
                                    connection.commit()
                                    print("Borrado exitoso. ")
                                    x1 = None
                                    presiona(x1)
                                except:
                                    print("Error en el borrado de datos. ")
                            else:
                                break
                    
                elif opc == "8":
                    cls()
                    cursor.execute("SELECT * FROM empleado")
                    datos = cursor.fetchall()

                    menu2()
                    opc2 = input("\nPor favor, ingrese una opción: ")

                    if opc2 == "1":
                        try:
                            opctabla = input("Quieres ver la tabla de datos?(1 = Si)(2 = No) \n->")
                            if opctabla == "1":
                                column_names = [description[0] for description in cursor.description]
                                tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                print(tabla)

                            ced = input("Ingrese la cedula del empleado:  ")
                            cls()

                        except:
                            print("Error en la coleccion de datos.")

                        while (True):
                            cls()
                            cursor.execute(f"SELECT * FROM empleado WHERE ci_empleado = '{ced}'")
                            datos = cursor.fetchall()
                            if not datos:
                                print("cédula no existente. ")
                                x1 = None
                                presiona(x1)
                                break
                            else:
                                column_names = [description[0] for description in cursor.description]
                                tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                print(tabla)

                                print("-- Qué desea actualizar? --")
                                print("1. Cédula ")
                                print("2. Nombre ")
                                print("3. Apellido ")
                                print("4. Cargo ")
                                print("5. Sueldo")
                                print("6. Salir ")
                                opc3 = input("Porfavor, Ingrese una opción: ")
                                if opc3 == "1":
                                    try:

                                        cls()

                                        column_names = [description[0] for description in cursor.description]
                                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                        print(tabla)

                                        nueva_ced = input("Ingrese su nueva cédula: ")
                                        cursor.execute(f"UPDATE empleado SET ci_empleado = {nueva_ced} WHERE ci_empleado = '{ced}'")
                                        connection.commit()
                                        print("Modificación existosa. ")
                                        x1 = None
                                        presiona(x1)
                                        break

                                    except:
                                        print("Error en la actualizacion de datos. ")
                                        break
                                
                                elif opc3 == "2":
                                    try:
                                        cls()

                                        column_names = [description[0] for description in cursor.description]
                                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                        print(tabla)

                                        nombre = input("Ingrese su nuevo nombre: ")
                                        cursor.execute(f"UPDATE empleado SET nombre = '{nombre}' WHERE ci_empleado = '{ced}'")
                                        connection.commit()
                                        print("Modificación existosa. ")
                                        x1 = None
                                        presiona(x1)
                                        break

                                    except:
                                        print("Error en la actualizacion de datos. ")
                                        break
                                    
                                elif opc3 == "3":
                                    try:
                                        cls()

                                        column_names = [description[0] for description in cursor.description]
                                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                        print(tabla)

                                        apellido = input("Ingrese su nuevo apellido: ")
                                        cursor.execute(f"UPDATE empleado SET apellido = '{apellido}' WHERE ci_empleado = '{ced}'")
                                        connection.commit()
                                        print("Modificación existosa. ")
                                        x1 = None
                                        presiona(x1)
                                        break

                                    except:
                                        print("Error en la actualizacion de datos. ")
                                        break
                                    
                                elif opc3 == "4":
                                    try:
                                        cls()

                                        column_names = [description[0] for description in cursor.description]
                                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                        print(tabla)

                                        cargo = input("Ingrese su nuevo cargo: ")
                                        cursor.execute(f"UPDATE empleado SET cargo = '{cargo}' WHERE ci_empleado = '{ced}'")
                                        connection.commit()
                                        print("Modificación existosa. ")
                                        x1 = None
                                        presiona(x1)
                                        break

                                    except:
                                        print("Error en la actualizacion de datos. ")
                                        break
                                    
                                elif opc3 == "5":
                                    try:
                                        cls()

                                        column_names = [description[0] for description in cursor.description]
                                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                        print(tabla)

                                        sueldo = input("Ingrese su nuevo sueldo: ")
                                        cursor.execute(f"UPDATE empleado SET sueldo = {sueldo} WHERE ci_empleado = '{ced}'")
                                        connection.commit()
                                        print("Modificación existosa. ")
                                        x1 = None
                                        presiona(x1)
                                        break

                                    except:
                                        print("Error en la actualizacion de datos. ")
                                        break
        
                                elif opc3 == "6":
                                    break
                            
                    elif opc2 == "2":
                        try:
                            opctabla = input("Quieres ver la tabla de datos?(1 = Si)(2 = No) \n->")
                            if opctabla == "1":
                                column_names = [description[0] for description in cursor.description]
                                tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                print(tabla)

                            ci = input("Ingrese la id de la factura:  ")
                            cls()

                        except:
                            print("Error en la coleccion de datos.")
                            
                        cursor.execute(f"SELECT * FROM empleado WHERE ci_empleado = '{ci}'")
                        datos = cursor.fetchall()
                        
                        if not datos:
                            print("ID no existente. ")
                            x1 = None
                            presiona(x1)
                        else:
                            column_names = [description[0] for description in cursor.description]
                            tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                            print(tabla)

                            print("-- Seguro que desea borrar al empleado? --")
                            carro = input("-> ")
                            if carro == 'Si' or 'si' or 'sI' or 'yes' or 'Yes' or 'yEs' or 'yeS' or 'YeS' or 'yES' or 'YEs' or " ":
                                try:

                                    cls()
                                    cursor.execute(f"DELETE FROM empleado WHERE ci_empleado ='{ci}'")
                                    connection.commit()
                                    print("Borrado exitoso. ")
                                    x1 = None
                                    presiona(x1)
                                except:
                                    print("Error en el borrado de datos. ")
                            else:
                                break

                elif opc == "9":
                    cls()
                    cursor.execute("SELECT * FROM ente")
                    datos = cursor.fetchall()

                    menu2()
                    opc2 = input("\nPor favor, ingrese una opción: ")

                    if opc2 == "1":
                        try:
                            opctabla = input("Quieres ver la tabla de datos?(1 = Si)(2 = No) \n->")
                            if opctabla == "1":
                                column_names = [description[0] for description in cursor.description]
                                tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                print(tabla)

                            id = input("Ingrese el id del ente:  ")
                            cls()

                        except:
                            print("Error en la coleccion de datos.")

                        while (True):
                            cls()
                            cursor.execute(f"SELECT * FROM ente WHERE id_ente = '{id}'")
                            datos = cursor.fetchall()
                            if not datos:
                                print("ID no existente. ")
                                x1 = None
                                presiona(x1)
                                break
                            else:
                                column_names = [description[0] for description in cursor.description]
                                tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                print(tabla)

                                print("-- Qué desea actualizar? --")
                                print("1. Telefono ")
                                print("2. Direccion ")
                                print("3. Salir ")
                                opc3 = input("Porfavor, Ingrese una opción: ")
                                if opc3 == "1":
                                    try:
                                        cls()

                                        column_names = [description[0] for description in cursor.description]
                                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                        print(tabla)

                                        nuevo_telefono = input("Ingrese su nuevo telefono (XXX-XXX-XXXX): ")
                                        cursor.execute(f"UPDATE ente SET telefono = '{nuevo_telefono}' WHERE id_ente = '{id}'")
                                        connection.commit()
                                        print("Modificación existosa. ")
                                        x1 = None
                                        presiona(x1)
                                        break

                                    except:
                                        print("Error en la actualizacion de datos. ")
                                        break
                                    
                                elif opc3 == "2":
                                    try:
                                        cls()

                                        column_names = [description[0] for description in cursor.description]
                                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                        print(tabla)

                                        nueva_direccion = input("Ingrese su nueva direccion: ")
                                        cursor.execute(f"UPDATE ente SET direccion = '{nueva_direccion}' WHERE id_ente = '{id}'")
                                        connection.commit()
                                        print("Modificación existosa. ")
                                        x1 = None
                                        presiona(x1)
                                        break

                                    except:
                                        print("Error en la actualizacion de datos. ")
                                        break
        
                                elif opc3 == "3":
                                    break
                            
                    elif opc2 == "2":
                        try:
                            opctabla = input("Quieres ver la tabla de datos?(1 = Si)(2 = No) \n->")
                            if opctabla == "1":
                                column_names = [description[0] for description in cursor.description]
                                tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                                print(tabla)

                            id = input("Ingrese la id del ente:  ")
                            cls()

                        except:
                            print("Error en la coleccion de datos.")
                            
                        cursor.execute(f"SELECT * FROM ente WHERE id_ente = '{id}'")
                        datos = cursor.fetchall()
                        
                        if not datos:
                            print("ID no existente. ")
                            x1 = None
                            presiona(x1)
                        else:
                            column_names = [description[0] for description in cursor.description]
                            tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                            print(tabla)

                            print("-- Seguro que desea borrar al empleado? --")
                            carro = input("-> ")
                            if carro == 'Si' or 'si' or 'sI' or 'yes' or 'Yes' or 'yEs' or 'yeS' or 'YeS' or 'yES' or 'YEs' or " ":
                                try:

                                    cls()
                                    cursor.execute(f"DELETE FROM ente WHERE id_ente ='{id}'")
                                    connection.commit()
                                    print("Borrado exitoso. ")
                                    x1 = None
                                    presiona(x1)
                                except:
                                    print("Error en el borrado de datos. ")
                            else:
                                break
                            
                elif opc == "10":
                    break    

    except DatabaseError as ex:
        print("Error durante la conexión: {}".format(ex))