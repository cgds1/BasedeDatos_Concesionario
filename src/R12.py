import psycopg2
from psycopg2 import DatabaseError
from os import system

def main():
    try:
        connection = psycopg2.connect("postgresql://concesionaria_owner:WtN7HmGxF9pg@ep-weathered-glitter-a4gsgrak.us-east-1.aws.neon.tech/CONCESIONARIA?sslmode=require")
        cursor = connection.cursor()
        while True:
            print("\t.:VEHICULOS EXHIBIDOS:.")
            print("1)Ver que vehiculos tenemos prestados para exhibir.")
            print("2)Volver al menu principal.")
            option = int(input("Ingrese su opcion: "))
            system("cls")
            if option == 1:
                menu_1(cursor)
            elif option == 2:
                break
            else:
                print("No ingreso una opcion valida, vuelva a intentarlo.")
                print("Pulse una tecla para continuar...")
                input()
            system("cls")
    except DatabaseError as ex:
        print("Error durante la conexión: {}".format(ex))

    finally:
        connection.close()

def menu_1(cursor):
    evento = input("Ingrese el nombre del evento a consultar: ")
    cursor.execute(f"""select a.vin_vehiculo, b.descripcion, c.precio from exposicion_evento as a
    inner join evento as b
    on a.id_evento = b.id_evento
    inner join vehiculo as c
    on c.vin_vehiculo = a.vin_vehiculo
    where b.nombre = '{evento}'""")
    lista = cursor.fetchall()
    if lista:
        print("Estos son los vehiculos que hemos cedido y sus condiciones: ")
        for i in lista:
            print(f"Numero de chasis de vehiculo cedido: {i[0]}")
            print(f"Descripcion del evento al que fue cedido: {i[1]}")
            if i[2] < 25000:
                print("Plazo por el que fue cedido el vehiculo: 60 dias.")
            else:
                print("Plazo por el que fue cedido el coche: 30 dias.")
            print(f"Monto a pagar en caso de sufrir algun incidente el vehiculo: {i[2]/10}")
            print()
    else:
        print("No le hemos cedido ningun vehiculo a alguna empresa que participe en este evento.")
    print("Pulse una tecla para continuar...")
    input()