import psycopg2
from psycopg2 import DatabaseError
import os

def mostrar_menu():
    print("1. Crear una factura")
    print("2. Modificar una factura")
    print("3. Borrar una factura")
    print("4. Salir")
    
def mostrar_menu_modificar():
    print("Selecciona el campo que quieres modificar:")
    print("1. Cedula del empleado")
    print("2. ID del cliente")
    print("3. Tipo de factura")
    print("4. Bono de la factura")
    print("5. Fecha de la factura")
    print("6. Hora de la factura")
    
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

        while True:
            mostrar_menu()
            opcion = input("Por favor, elige una opción: ")
            cls()
            
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

                mostrar_menu_modificar()
                opcion_campo = input("Introduce el número de la opción: ")

                if opcion_campo == "1":
                    nuevo_valor = input("Introduce la nueva cedula del empleado: ")
                    campo = "ci_empleado"
                elif opcion_campo == "2":
                    nuevo_valor = input("Introduce el nuevo ID del cliente: ")
                    campo = "id_cliente"
                elif opcion_campo == "3":
                    nuevo_valor = input("Introduce el nuevo tipo (Compra o Venta): ")
                    campo = "tipo_factura"
                elif opcion_campo == "4":
                    nuevo_valor = input("Introduce el nuevo bono de la factura: ")
                    campo = "bono"
                elif opcion_campo == "5":
                    nuevo_valor = input("Introduce la nueva fecha de la factura (YYYY-MM-DD): ")
                    campo = "dia"
                elif opcion_campo == "6":
                    nuevo_valor = input("Introduce la nueva hora de la factura (HH:MM:SS): ")
                    campo = "hora"

                cursor.execute(f"""
                    UPDATE factura
                    SET {campo} = %s
                    WHERE id_factura = %s;
                """, (nuevo_valor, id_factura))
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
                break

            else:
                print("Opción no válida. Por favor, elige una opción del menú.")

    except DatabaseError as ex:
        print("Error durante la conexión: {}".format(ex))

    finally:
        connection.close()  # Se cerró la conexión a la BD.
        print("La conexión ha finalizado.")

