import psycopg2
from psycopg2 import DatabaseError
from tabulate import tabulate
import os

def cls():
    if os.name == "nt":
        os.system("cls")
    else: 
        os.system("clear")
        
def presiona(x):
    x = input("Presiona para continuar...")
        
def main():
    try:
        connection_string = "postgresql://concesionaria_owner:WtN7HmGxF9pg@ep-weathered-glitter-a4gsgrak.us-east-1.aws.neon.tech/CONCESIONARIA?sslmode=require"    
        connection = psycopg2.connect(connection_string)
        cursor = connection.cursor()
        cls()


        cursor.execute("""
            SELECT 
                v.vin_vehiculo,
                d.marca,
                d.modelo,
                e.ci_empleado,
                e.nombre AS nombre_empleado,
                f.tipo_factura,
                cn.ci_cliente_natural,
                cn.nombre AS nombre_cliente_natural
            FROM 
                factura f
            JOIN 
                detalle dt ON f.id_factura = dt.id_factura
            JOIN 
                vehiculo v ON dt.vin_vehiculo = v.vin_vehiculo
            JOIN 
                descripcion_vehiculo d ON v.id_descripcion = d.id_descripcion
            JOIN 
                empleado e ON f.ci_empleado = e.ci_empleado
            LEFT JOIN 
                cliente_natural cn ON f.id_cliente = cn.id_cliente
            LIMIT 20;
        """)
        rows = cursor.fetchall()
        
        column_names = [description[0] for description in cursor.description]
        tabla = tabulate(rows, headers= column_names, tablefmt="psql")
        print(tabla)

            
        x1 = None
        presiona(x1)

    except DatabaseError as ex:
        print("Error durante la conexión: {}".format(ex))

    finally:
        connection.close()  # Se cerró la conexión a la BD.
        print("La conexión ha finalizado.")
