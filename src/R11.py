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
    print("9. Cliente                    ")
    print("10. Ente                      ")
    print("11. Salir                     ")

def menu2():
    print("-- Qué desea hacer? --")
    print("1. Modificar")
    print("2. Eliminar")

def cls():
    if os.name == "nt":
        os.system("cls")
    else: 
        os.system("clear")


def main():
    try:
        connection_string = "postgresql://concesionaria_owner:WtN7HmGxF9pg@ep-weathered-glitter-a4gsgrak.us-east-1.aws.neon.tech/CONCESIONARIA?sslmode=require"
        connection = psycopg2.connect(connection_string)
        cursor = connection.cursor()
        print("Conexión exitosa. ")

        menu()
        while(True):
            opc = input("\nPor favor, ingrese una opción: ")

            if opc == "1":
                cls()
                cursor.execute("SELECT * FROM vehiculo")
                datos = cursor.fetchall()

                menu2()
                opc2 = input("\nPor favor, ingrese una opción: ")

                if opc2 == "1":

                    column_names = [description[0] for description in cursor.description]
                    tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                    print(tabla)

                    var = input("Ingrese el VIM del vehiculo:  ")
                    cls()

                    cursor.execute(f"SELECT * FROM vehiculo WHERE vin_vehiculo = '{var}'")
                    datos = cursor.fetchall()

                    column_names = [description[0] for description in cursor.description]
                    tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                    print(tabla)

                    print("-- Qué desea actualizar? --")
                    print("1. VIN ")
                    print("2. Precio ")
                    print("3. Color ")
                    print("4. Kilometraje ")
                    print("5. Matricula ")
                    print("6. Todo ")
                    print("7. Salir ")
                    carro = input("Porfavor, Ingrese una opción: ")

                    while (True):
                        if carro == "1":
                            cls()

                            column_names = [description[0] for description in cursor.description]
                            tabla = tabulate(datos, headers= column_names, tablefmt="psql")
                            print(tabla)

                            nuevo_vin = input("Ingrese su nuevo VIM: ")
                            cursor.execute(f"UPDATE vehiculo SET vin_vehiculo = '{nuevo_vin}' WHERE vin_vehiculo = '{var}'")
                            cursor.commit()
                        



 




                

    except DatabaseError as ex:
        print("Error durante la conexión: {}".format(ex))

main()