import psycopg2
from psycopg2 import DatabaseError
from tabulate import tabulate

def get_event_and_exposition_by_id(event_id):
    try:
        connection_string = "postgresql://concesionaria_owner:WtN7HmGxF9pg@ep-weathered-glitter-a4gsgrak.us-east-1.aws.neon.tech/CONCESIONARIA?sslmode=require"
        connection = psycopg2.connect(connection_string)

        cursor = connection.cursor()

        # Consulta para obtener los detalles del evento
        cursor.execute(f"SELECT * FROM EVENTO WHERE id_evento = {event_id}")
        row = cursor.fetchone()
        if row is not None:
            print(f"Detalles del evento {event_id}:")
            for dato in row:
                print(f"{dato} | ", end=" ")
        else:
            print(f"No se encontró ningún evento con el ID {event_id}")

        # Consulta para obtener las transacciones de la exposición del evento
        cursor.execute(f"SELECT * FROM EXPOSICION_EVENTO WHERE id_evento = {event_id}")
        rows = cursor.fetchall()
        print(f"\nTransacciones de la exposición del evento {event_id}:")
        
        column_names = [description[0] for description in cursor.description]
        tabla = tabulate(rows, headers= column_names, tablefmt="psql")
        print(tabla)

        

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
