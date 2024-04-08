import psycopg2
from psycopg2 import DatabaseError
import os
from tabulate import tabulate

# Hacer un reporte de ganancias del mes en eventos, carreras, seguro y ventas #

def cls():
    if os.name == "nt":
        os.system("cls")
    else: 
        os.system("clear")
        
def presiona(x):
    x = input("Presiona para continuar...")
    cls()

def menu():
    print("\n--     Reporte de ganancias del mes    --")
    print("1. Evento ")
    print("2. Carreras ")
    print("3. Ventas ")
    print("4. Seguro")
    print("5. Salir ")
     
def main():
    try:
        connection_string = "postgresql://concesionaria_owner:WtN7HmGxF9pg@ep-weathered-glitter-a4gsgrak.us-east-1.aws.neon.tech/CONCESIONARIA?sslmode=require"
        connection = psycopg2.connect(connection_string)
        cursor = connection.cursor()
        
        while True:
            menu()
            x = input("Por favor, Ingresa una opcion: ")
            cls()
            
            if x == "1":
                try:
                    cursor.execute(f"SELECT * FROM evento")
                    datos = cursor.fetchall()
                    opctabla = input("Quieres ver la tabla de datos?(1 = Si)(2 = No) \n->")
                    if opctabla == "1":
                        column_names = [description[0] for description in cursor.description]
                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                        print(tabla)
                        
                    mesus = input("\nIngrese el mes a elegir: ")
                    yearus = input("Ingrese el año a elegir: ")
                    cls()
                    cursor.execute(f"SELECT * FROM evento WHERE extract(month FROM fecha) = {mesus} AND extract(year FROM fecha) = {yearus};")
                
                    print(f"\nCarros vendidos en el mes {mesus} y del año {yearus}")
                    datos = cursor.fetchall()
            
                    id_evento = []
            
                    for row in datos:
                        id_evento.append(row[0])

                    cadena = str(id_evento)[1:-1]
            
                    cursor.execute(f"SELECT * FROM exposicion_evento WHERE id_evento IN ({cadena})")
                    datos1 = cursor.fetchall()

                    vin_vehiculo = []
            
                    for row in datos1:
                         vin_vehiculo.append(row[1])
                
                    cadena1 = str(vin_vehiculo)[1:-1]
                
                    cursor.execute(f"SELECT * FROM vehiculo WHERE vin_vehiculo IN ({cadena1})")
                    datos2 = cursor.fetchall()
            
                    column_names = [description[0] for description in cursor.description]
                    tabla = tabulate(datos2, headers= column_names, tablefmt="psql")
                    print(tabla)
                
                    precio_evento = 0
            
                    for row in datos2:
                        precio_evento += row[2]
                    
                    print(f"\nPrecio total de ventas en los eventos: {precio_evento}")
                    x1 = None
                    presiona(x1)
                    pass
                
                except:
                    print("No existe registro de ese mes. ")
                    x1 = None
                    presiona(x1)
            
            elif x == "2":
                try:
                    
                    cursor.execute(f"SELECT * FROM carrera")
                    datos = cursor.fetchall()
                    
                    opctabla = input("Quieres ver la tabla de datos?(1 = Si)(2 = No) \n->")
                    if opctabla == "1":
                        column_names = [description[0] for description in cursor.description]
                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                        print(tabla)
                    
                    mesus = input("\nIngrese el mes a elegir: ")
                    yearus = input("Ingrese el año a elegir: ")
                    cursor.execute(f"SELECT * FROM carrera WHERE extract(month FROM fecha) = {mesus} AND extract(year FROM fecha) = {yearus};")
                    datos = cursor.fetchall()
                
                    precio_carrera = 0
                
                    for row in datos:
                        precio_carrera += row[5]
                
                    if precio_carrera == 0:
                        print("No hubo carreras ganadas ese mes. ")
                        x1 = None
                        presiona(x1)
                    
                    else:    
                        print(f"\nPrecio total de dinero ganado en carreras: {precio_carrera}")
                        x1 = None
                        presiona(x1)
                    pass
                except:
                    print("No existe registro de ese mes. ")
                    x1 = None
                    presiona(x1)
                    
            elif x == "3":
                #try:
                    
                    cursor.execute(f"SELECT * FROM factura")
                    datos = cursor.fetchall()
                    
                    opctabla = input("Quieres ver la tabla de datos?(1 = Si)(2 = No) \n->")
                    if opctabla == "1":
                        column_names = [description[0] for description in cursor.description]
                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                        print(tabla)
                
                    
                    mesus = input("\nIngrese el mes a elegir: ")
                    yearus = input("Ingrese el año a elegir: ")
                    cursor.execute(f"SELECT * FROM factura WHERE extract(year from dia) = {yearus} AND extract(month from dia) = {mesus};")
                    datos = cursor.fetchall()
                
                    id_factura = []
                
                    for row in datos:
                        id_factura.append(row[0])
                
                    cadena = str(id_factura)[1:-1]
                
                    cursor.execute(f"SELECT * FROM detalle WHERE id_factura IN ({cadena})")
                    datos1 = cursor.fetchall()
                
                    id_detalle = []
                
                    for row in datos1:
                        id_detalle.append(row[0])
            
                    cadena1 = str(id_detalle)[1:-1]
                    
                    cursor.execute(f"SELECT * FROM detalle_total WHERE id_detalle IN ({cadena1})")
                    datos2 = cursor.fetchall()
                
                    precio_ventas = 0
                
                    for row in datos2:
                        precio_ventas += row[1]
                    print(f"Estas son las ventas totales en el mes {mesus} y el año {yearus}: {precio_ventas}")
                    x1 = None
                    presiona(x1)
                #except:
                    print("No existe registro de ese mes. ")
                    x1 = None
                    presiona(x1)
                #pass
            elif x == "4":
                try:
                    
                    cursor.execute(f"SELECT * FROM factura")
                    datos = cursor.fetchall()
                    
                    opctabla = input("Quieres ver la tabla de datos?(1 = Si)(2 = No) \n->")
                    if opctabla == "1":
                        column_names = [description[0] for description in cursor.description]
                        tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                        print(tabla)
                    
                    mesus = input("\nIngrese el mes a elegir: ")
                    yearus = input("Ingrese el año a elegir: ")
                    cursor.execute(f"SELECT * FROM factura WHERE extract(year from dia) = {yearus} AND extract(month from dia) = {mesus};")
                    datos = cursor.fetchall()
                    
                    id_factura = []
                    
                    for row in datos:
                        id_factura.append(row[0])
                
                    cadena = str(id_factura)[1:-1]
                    cursor.execute(f"SELECT * FROM detalle WHERE id_factura IN ({cadena});")
                    datos1 = cursor.fetchall()
                    
                    id_seguro = []
                    
                    for row in datos1:
                        id_seguro.append(row[3])
                    
                    precio_total = 0
                    
                    id_seguro_copy = id_seguro
                    count = len(id_seguro_copy)


                    for elemento in range(count):
                        if id_seguro_copy[elemento] == 1:
                            precio_total += 200
                        elif id_seguro_copy[elemento] == 2:
                            precio_total += 700
                        elif id_seguro_copy[elemento] == 3:
                            precio_total += 500
                        elif id_seguro_copy[elemento] == 4:
                            precio_total += 1000
                        elif id_seguro_copy[elemento] == 5:
                            precio_total += 0
                            
                    print(f"El precio total en seguros en el mes de {mesus} con el año {yearus} es de: {precio_total}")
                    x1 = None
                    presiona(x1)
                except:
                    print("No existe registro de ese mes. ")
                    x1 = None
                    presiona(x1)
                    
            elif x == "5" :
                print("Bye bye!")
                break
            
            
    except DatabaseError as ex:
        print("Error durante la conexión: {}".format(ex))
    

    