import psycopg2
from psycopg2 import DatabaseError
from os import system

def main():
    try:
        connection_string = "postgresql://concesionaria_owner:WtN7HmGxF9pg@ep-weathered-glitter-a4gsgrak.us-east-1.aws.neon.tech/CONCESIONARIA?sslmode=require"
        connection = psycopg2.connect(connection_string)
        cursor = connection.cursor()
        while True:
            print("\t.:CONSULTA PROPIETARIOS:.")
            print("1)Ver el historial de clientes naturales de un vehiculo.")
            print("2)Ver los cliente juridicos de un vehiculo.")
            print("3)Volver al menu principal.")
            option = int(input("Ingrese su opcion: "))
            system("cls")
            if option == 1:
                matricula = input("Ingrese la matricula del vehiculo a consultar: ")
                cursor.execute(f'''select ci_cliente_natural, nombre, apellido, (select telefono from ente as c where c.id_ente = a.id_cliente),
                (select direccion from ente as c where c.id_ente = a.id_cliente), b.propietario_actual from cliente_natural as a
                inner join propietario_vehiculo as b
                on a.id_cliente = b.id_cliente
                where b.vin_vehiculo = '{matricula}' ''')
                lista = cursor.fetchall()
                for elementos in lista:
                    print(f"Cedula del cliente: {elementos[0]}")
                    print(f"Nombre del cliente: {elementos[1]}")
                    print(f"Apellido del cliente: {elementos[2]}")
                    print(f"Numero de telefono del cliente: {elementos[3]}")
                    print(f"Direccion del cliente: {elementos[4]}")
                    if elementos[5]:
                        print("El cliente es el actual dueño del vehiculo")
                    else:
                        print("El cliente es un antiguo propietario del vehiculo.")
                    print()
                print("Pulse una tecla para continuar...")
                input()
            elif option == 2:
                matricula = input("Ingrese la matricula del vehiculo a consultar: ")
                cursor.execute(f'''select rif, nombre, (select telefono from ente as c where c.id_ente = a.id_cliente),
                (select direccion from ente as c where c.id_ente = a.id_cliente), b.propietario_actual from cliente_juridico as a
                inner join propietario_vehiculo as b
                on a.id_cliente = b.id_cliente
                where b.vin_vehiculo = '{matricula}' ''')
                lista = cursor.fetchall()
                for elementos in lista:
                    print(f"RIF del cliente: {elementos[0]}")
                    print(f"Nombre del cliente: {elementos[1]}")
                    print(f"Numero de telefono del cliente: {elementos[2]}")
                    print(f"Direccion del cliente: {elementos[3]}")
                    if elementos[4]:
                        print("El cliente es el actual dueño del vehiculo")
                    else:
                        print("El cliente es un antiguo propietario del vehiculo.")
                    print()
                print("Pulse una tecla para continuar...")
                input()
            elif option == 3:
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

main()