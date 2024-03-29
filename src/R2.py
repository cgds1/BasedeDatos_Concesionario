import psycopg2
from psycopg2 import DatabaseError

def menu():
    print("-- Estadisticas de vehiculos comprados. --")
    print("   1. Dia   ")
    print("   2. Mes   ")
    print("   3. Año   ")
    print("   4. Salir ")

def main():
    
    try:
        connection = psycopg2.connect(
                host='localhost', 
                user='postgres',
                password='', # Clave para acceder a la base de datos
                database='concesionaria',
                port = "" # En caso de tener versiones diferentes de sql usar el puerto de la version.
        )
        print("Conexión exitosa.")

        while True:
            menu()
            x = input("Por favor, elige una opción: ")
            cursor = connection.cursor()
            
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
        
main()