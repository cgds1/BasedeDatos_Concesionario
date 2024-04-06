import psycopg2
from psycopg2 import DatabaseError
import os

def menu():
    print("1. Ver todos los datos")
    print("2. Ver datos por ID")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

def cls():
    if os.name == "nt":
        os.system("cls")
    else: 
        os.system("clear")

def ver_todos_los_datos(cursor):
    cursor.execute("SELECT * FROM vehiculo_reparado")
    vehiculos_reparados = cursor.fetchall()
    for vehiculo in vehiculos_reparados:
        id_rsuministrado = vehiculo[0]
        vin_vehiculo = vehiculo[1]
        cursor.execute(f"SELECT * FROM repuesto_suministrado WHERE id_rsuministrado = {id_rsuministrado}")
        repuesto_suministrado = cursor.fetchone()
        if repuesto_suministrado is not None:
            numero_parte = repuesto_suministrado[3]
            rif_taller = repuesto_suministrado[1]
            rif_proveedor = repuesto_suministrado[2]
            cursor.execute(f"SELECT * FROM repuesto WHERE numero_parte = '{numero_parte}'")
            repuesto = cursor.fetchone()
            if repuesto is not None:
                nombre_repuesto = repuesto[1]
                cursor.execute(f"SELECT nombre FROM proveedor WHERE rif_proveedor = '{rif_proveedor}'")
                nombre_proveedor = cursor.fetchone()[0]
                cursor.execute(f"SELECT nombre FROM taller WHERE rif_taller = '{rif_taller}'")
                nombre_taller = cursor.fetchone()[0]
                print(f"VIN del Vehículo: {vin_vehiculo}, Número de Parte: {numero_parte}, Descripción de la Parte: {nombre_repuesto}, Nombre del Proveedor: {nombre_proveedor}, Nombre del Taller: {nombre_taller}")

def ver_datos_por_id(cursor):
    id = input("Ingrese el ID: ")
    cursor.execute(f"SELECT * FROM vehiculo_reparado WHERE id_rsuministrado = {id}")
    vehiculo = cursor.fetchone()
    if vehiculo is not None:
        id_rsuministrado = vehiculo[0]
        vin_vehiculo = vehiculo[1]
        cursor.execute(f"SELECT * FROM repuesto_suministrado WHERE id_rsuministrado = {id_rsuministrado}")
        repuesto_suministrado = cursor.fetchone()
        if repuesto_suministrado is not None:
            numero_parte = repuesto_suministrado[3]
            rif_taller = repuesto_suministrado[1]
            rif_proveedor = repuesto_suministrado[2]
            cursor.execute(f"SELECT * FROM repuesto WHERE numero_parte = '{numero_parte}'")
            repuesto = cursor.fetchone()
            if repuesto is not None:
                nombre_repuesto = repuesto[1]
                cursor.execute(f"SELECT nombre FROM proveedor WHERE rif_proveedor = '{rif_proveedor}'")
                nombre_proveedor = cursor.fetchone()[0]
                cursor.execute(f"SELECT nombre FROM taller WHERE rif_taller = '{rif_taller}'")
                nombre_taller = cursor.fetchone()[0]
                print(f"VIN del Vehículo: {vin_vehiculo}, Número de Parte: {numero_parte}, Descripción de la Parte: {nombre_repuesto}, Nombre del Proveedor: {nombre_proveedor}, Nombre del Taller: {nombre_taller}")
    else:
        print("No se encontraron datos con ese ID.")

def main():
    try:
        connection_string = "postgresql://concesionaria_owner:WtN7HmGxF9pg@ep-weathered-glitter-a4gsgrak.us-east-1.aws.neon.tech/CONCESIONARIA?sslmode=require"
        connection = psycopg2.connect(connection_string)
        cursor = connection.cursor()
        cls()
        
        while True:
            opcion = menu()
            if opcion == '1':
                ver_todos_los_datos(cursor)
            elif opcion == '2':
                ver_datos_por_id(cursor)
            elif opcion == '3':
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")

    except DatabaseError as ex:
        print("Error durante la conexión: {}".format(ex))
    finally:
        connection.close()  # Se cerró la conexión a la BD.
        print("La conexión ha finalizado.")
