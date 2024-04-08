import psycopg2
import random
from os import system
from psycopg2 import DatabaseError

def main():
    try:
        connection = psycopg2.connect("postgresql://concesionaria_owner:WtN7HmGxF9pg@ep-weathered-glitter-a4gsgrak.us-east-1.aws.neon.tech/CONCESIONARIA?sslmode=require")
        cursor = connection.cursor()
        while True:
            print("\t.:CONSULTA PREMIO VEHICULOS:.")
            print("1)Consultar si un vehiculo ha participado en un evento.")
            print("2)Consultar si un vehiculo ha participado en una carrera.")
            print("3)Volver al menu principal.")
            option = int(input("Ingrese su opcion: "))
            system("cls")
            if option == 1:
                menu_1(cursor)
            elif option == 2:
                menu_2(cursor)
            elif option == 3:
                 break
            else:
                print("No ingreso una opcion correcta, vuelva a intentarlo.")
                print("Presione una tecla para continuar...")
                input()
            system("cls")
    except DatabaseError as ex:
            print("Error durante la conexión: {}".format(ex))

    finally:
        connection.close()

def menu_1(cursor):
    vin = input("Ingrese el numero de chasis del vehiculo: ")
    cursor.execute(f"""select b.nombre, b.descripcion, b.fecha, tipo_transaccion from exposicion_evento as a
    inner join evento as b
    on a.id_evento = b.id_evento
    where a.vin_vehiculo = '{vin}'""")
    lista = cursor.fetchall()
    if lista:
        for i in lista:
            print(f"Nombre del evento: {i[0]}")
            print(f"Descripcion del evento: {i[1]}")
            print(f"Fecha de realizacion del evento: {i[2]}")
            print(f"Premio vehiculo por su participacion en el evento: {random.randint(10000, 30000)}$.")
            print(f"El premio fue entregado por via: {i[3]}")
    else:
        print("No existe informacion que este vehiculo haya participado en un evento.")
    print("Presione una tecla para continuar...")
    input()

def menu_2(cursor):
    vin = input("Ingrese el numero de chasis del vehiculo: ")
    cursor.execute(f"""select nombre_carrera, nombre_circuito, tipo_carrera, fecha, c.primer_nombre, c.apellido,
    e.nombre, e.direccion, premio from carrera as a
    inner join participante_carrera as b
    on a.id_carrera = b.id_carrera
    inner join piloto as c
    on c.id_piloto = b.id_piloto
    inner join pits as d
    on d.id_carrera = b.id_carrera
    inner join taller as e
    on e.rif_taller = d.rif_taller
    where b.id_carro = '{vin}'""")
    lista = cursor.fetchall()
    if lista:
        posicion = random.randint(1, 20)
        for i in lista:
            print(f"Nombre de la carrera: {i[0]}")
            print(f"Nombre del circuito: {i[1]}")
            print(f"Tipo de carrera: {i[2]}")
            print(f"Fecha de realizacion de la carrera: {i[3]}")
            print(f"Nombre del piloto: {i[4]}")
            print(f"Apellido del piloto: {i[5]}")
            print(f"Posicion durante la carrera: {posicion}")
            print(f"Nombre del taller de los pits: {i[6]}")
            print(f"Direccion del taller de los pits: {i[7]}")
            print(f"Premio vehiculo por su participacion en el evento: {random.randint(10000, 30000)}$.")
            print(f"El premio de la carrera fue de: {i[8]}")
            if(posicion == 1):
                print("El vehiculo que usted consulto, fue el ganador de la carrera. Llevandose la totalidad del premio.")
            else:
                print("Debido que el vehiculo que consulto, no gano la carrera, no se llevo el premio.")
    else:
        print("No existe informacion que este vehiculo haya participado en un evento.")
    print("Presione una tecla para continuar...")
    input()