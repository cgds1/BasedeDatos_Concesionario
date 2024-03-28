import psycopg2
from psycopg2 import DatabaseError

def mostrar_menu():
    print("1. Crear una factura")
    print("2. Modificar una factura")
    print("3. Borrar una factura")
    print("4. Salir")

def main():
    try:
        connection = psycopg2.connect(
            host="localhost", 
            user="postgres",
            password="123", # Clave para acceder a la base de datos
            database="concesionaria",
            port = "" # En caso de tener versiones diferentes de sql usar el puerto de la version.
        )

        print(f"Conexión exitosa.")
        cursor = connection.cursor()

        while True:
            mostrar_menu()
            opcion = input("Por favor, elige una opción: ")

            if opcion == "1":
            
                cursor.execute("SELECT MAX(id_factura) FROM factura")
                id_factura = cursor.fetchone()[0]
                if id_factura is None:
                    id_factura = 1
                else:
                    id_factura += 1
                    
                ci_empleado = input("Cedula del empleado: ")
                id_cliente = input("Introduce el ID del cliente: ")
                tipo_factura = input("Introduce el tipo (Compra o Venta): ")
                bono = input("Introduce el bono del empleado: ")
                dia = input("Introduce la fecha de la factura (YYYY-MM-DD): ")
                hora = input("Introduce la hora (HH:MM:SS): ")
                cursor.execute("""
                    INSERT INTO factura (id_factura, ci_empleado, id_cliente, tipo_factura, bono, dia, hora)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (id_factura, ci_empleado, id_cliente, tipo_factura, bono, dia, hora))
                connection.commit()
                print("Factura creada con éxito.")

            elif opcion == "2":
                
                id_factura = input("Introduce el ID de la factura que quieres modificar: ")
                ci_empleado = input("Introduce la cedula del empleado que quieres modificar: ")
                id_cliente = input("Introduce el ID del cliente que quieres modificar: ")
                tipo_factura = input("Introduce el tipo (Compra o Venta): ")
                nuevo_bono = input("Introduce el nuevo bono de la factura: ")
                nueva_fecha = input("Introduce la nueva fecha de la factura (YYYY-MM-DD): ")
                nueva_hora = input("Introduce la nueva hora de la factura (HH:MM:SS): ")
                cursor.execute("""
                    UPDATE factura
                    SET ci_empleado = %s, id_cliente = %s, tipo_factura = %s, bono = %s, dia = %s, hora = %s
                    WHERE id_factura = %s;
                """, (ci_empleado, id_cliente, tipo_factura, nuevo_bono, nueva_fecha, nueva_hora, id_factura))
                connection.commit()
                print("Factura modificada con éxito.")

            elif opcion == "3":
            
                id_factura = input("Introduce el ID de la factura que quieres borrar: ")
                cursor.execute("""
                    DELETE FROM factura
                    WHERE id_factura = %s
                """, (id_factura,))
                connection.commit()
                print("Factura borrada con éxito.")

            elif opcion == "4":
                print("Has elegido salir. ¡Hasta luego!")
                break

            else:
                print("Opción no válida. Por favor, elige una opción del menú.")

    except DatabaseError as ex:
        print("Error durante la conexión: {}".format(ex))

    finally:
        connection.close()  # Se cerró la conexión a la BD.
        print("La conexión ha finalizado.")

if __name__ == "__main__":
    main()
