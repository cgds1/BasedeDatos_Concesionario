import psycopg2
from psycopg2 import DatabaseError
import os

def menu():
    print("-- Estadisticas de vehiculos comprados. --")
    print("   1. Dia   ")
    print("   2. Mes   ")
    print("   3. Año   ")
    print("   4. Salir ")
    
def cls():
    if os.name == "nt":
        os.system("cls")
    else: 
        os.system("clear")

def main():
    
    try:
        connection_string = "postgresql://concesionaria_owner:WtN7HmGxF9pg@ep-weathered-glitter-a4gsgrak.us-east-1.aws.neon.tech/CONCESIONARIA?sslmode=require"
        connection = psycopg2.connect(connection_string)

        while True:
            menu()
            x = input("Por favor, elige una opción: ")
            cursor = connection.cursor()
            cls()
            
            if x == "1":    
                print("-- Datos del dia especifico --")
                yearus = input("Ingresa el año: ")
                monthus = input("Ingresa el mes: ")
                dayus = input("Ingresa el dia: ")
                
                text1 = "Compra"
                text2 = "Venta"
                cursor.execute(f"SELECT COUNT(*) AS total_filas FROM factura WHERE extract(year FROM dia) = {yearus} AND extract(month FROM dia) = {monthus} AND extract(day FROM dia) = {dayus} AND tipo_factura ILIKE '%{text1}%';")
                datos = cursor.fetchall()
                for row in datos:
                    print(f"El dia {yearus}-{monthus}-{dayus} se ha comprado una cantidad de: {row[0]}")
                    
                cursor.execute(f"SELECT COUNT(*) AS total_filas FROM factura WHERE extract(year FROM dia) = {yearus} AND extract(month FROM dia) = {monthus} AND extract(day FROM dia) = {dayus} AND tipo_factura ILIKE '%{text2}%';")
                datos = cursor.fetchall()
                for row in datos:
                        print(f"El dia {yearus}-{monthus}-{dayus} se ha vendido una cantidad de: {row[0]}")
                
            elif x == "2":
                print("-- Datos del mes especifico --")
                yearus = input("Ingresa el año: ")
                monthus = input("Ingresa el mes: ")
                
                text1 = "Compra"
                text2 = "Venta"
                cursor.execute(f"SELECT COUNT(*) AS total_filas FROM factura WHERE extract(year FROM dia) = {yearus} AND extract(month FROM dia) = {monthus} AND tipo_factura ILIKE '%{text1}%';")
                datos = cursor.fetchall()
                for row in datos:
                    print(f"El dia {yearus}-{monthus} se ha comprado una cantidad de: {row[0]}")
                    
                cursor.execute(f"SELECT COUNT(*) AS total_filas FROM factura WHERE extract(year FROM dia) = {yearus} AND extract(month FROM dia) = {monthus} AND tipo_factura ILIKE '%{text2}%';")
                datos = cursor.fetchall()
                for row in datos:
                        print(f"El dia {yearus}-{monthus} se ha vendido una cantidad de: {row[0]}")
                
            elif x == "3":
                print("-- Datos del año especifico --")
                yearus = input("Ingresa el año: ")
                
                text1 = "Compra"
                text2 = "Venta"
                cursor.execute(f"SELECT COUNT(*) AS total_filas FROM factura WHERE extract(year FROM dia) = {yearus} AND tipo_factura ILIKE '%{text1}%';")
                datos = cursor.fetchall()
                for row in datos:
                    print(f"El dia {yearus} se ha comprado una cantidad de: {row[0]}")
                    
                cursor.execute(f"SELECT COUNT(*) AS total_filas FROM factura WHERE extract(year FROM dia) = {yearus} AND tipo_factura ILIKE '%{text2}%';")
                datos = cursor.fetchall()
                for row in datos:
                        print(f"El dia {yearus} se ha vendido una cantidad de: {row[0]}")
                        
            elif x == "4":
                print("Has elegido salir. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, elige una opción del menú.")
        
        connection.close()
                
                
    except DatabaseError as ex:
        print("Error durante la conexión: {}".format(ex))
        connection.close()