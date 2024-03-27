import psycopg2
from psycopg2 import DatabaseError

def get_event_and_exposition_by_id(event_id):
    try:
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='', # Clave para acceder a la base de datos
            database='concesionaria'
        )

        cursor = connection.cursor()

        # Consulta para obtener los detalles del evento
        cursor.execute(f"SELECT * FROM EVENTO WHERE id_evento = {event_id}")
        row = cursor.fetchone()
        if row is not None:
            print(f"Detalles del evento {event_id}:")
            print(row)
        else:
            print(f"No se encontró ningún evento con el ID {event_id}")

        # Consulta para obtener las transacciones de la exposición del evento
        cursor.execute(f"SELECT * FROM EXPOSICION_EVENTO WHERE id_evento = {event_id}")
        rows = cursor.fetchall()
        print(f"Transacciones de la exposición del evento {event_id}:")
        for row in rows:
            print(row)

    except DatabaseError as ex:
        print("Error durante la conexión: {}".format(ex))
    finally:
        connection.close()

def main():
    while True:
        print("\n1. Ver detalles de un evento y su exposición")
        print("2. Salir")
        option = input("Por favor, elige una opción: ")
        if option == '1':
            event_id = input("Por favor, introduce el ID del evento: ")
            get_event_and_exposition_by_id(event_id)
        elif option == '2':
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()
