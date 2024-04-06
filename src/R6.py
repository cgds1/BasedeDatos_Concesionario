import psycopg2
from psycopg2 import DatabaseError
import os

def menu():
    print("1. Mostrar clientes con seguro")
    print("2. Modificar seguro de un cliente (SI DESEA ELIMINAR DEL SEGURO PONGA ID 5 AL INGRESAR NUEVO ID)")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

def mostrar_clientes_con_seguro(cursor):
    cursor.execute("SELECT * FROM detalle WHERE id_seguro IN (1, 2, 3, 4)")
    rows = cursor.fetchall()
    for row in rows:
        id_factura = row[1]
        cursor.execute(f"SELECT * FROM factura WHERE id_factura = {id_factura}")
        factura = cursor.fetchone()
        if factura is not None:
            id_cliente = factura[2]
            cursor.execute(f"SELECT * FROM cliente_natural WHERE id_cliente = {id_cliente}")
            cliente_natural = cursor.fetchone()
            if cliente_natural is not None:
                print(f"Cliente Natural: {cliente_natural[2]} {cliente_natural[3]}")
            else:
                cursor.execute(f"SELECT * FROM cliente_juridico WHERE id_cliente = {id_cliente}")
                cliente_juridico = cursor.fetchone()
                if cliente_juridico is not None:
                    print(f"Cliente Jurídico: {cliente_juridico[2]}")
            cursor.execute(f"SELECT * FROM seguro WHERE id_seguro = {row[3]}")
            seguro = cursor.fetchone()
            if seguro is not None:
                print(f"Seguro: {seguro[1]}")


def modificar_seguro_de_cliente(cursor, connection):
    id_detalle = input("Ingrese el ID del detalle que desea modificar: ")
    nuevo_id_seguro = input("Ingrese el nuevo ID del seguro: ")
    cursor.execute(f"UPDATE detalle SET id_seguro = {nuevo_id_seguro} WHERE id_detalle = {id_detalle}")
    connection.commit()
    print("Seguro de cliente modificado con éxito.")
    
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
        cls()
        
        while True:
            opcion = menu()
            if opcion == '1':
                mostrar_clientes_con_seguro(cursor)
            elif opcion == '2':
                modificar_seguro_de_cliente(cursor, connection)
            elif opcion == '3':
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")

    except DatabaseError as ex:
        print("Error durante la conexión: {}".format(ex))
    finally:
        connection.close()  # Se cerró la conexión a la BD.
        print("La conexión ha finalizado.")