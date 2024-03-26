import psycopg2
from psycopg2 import DatabaseError

try:
    connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='', # Clave para acceseder a la base de datos
        database='concesionaria'
    )

    print("Conexión exitosa.")
    cursor = connection.cursor()
    
    print("vin_vehiculo | marca | modelo | ci_empleado | nombre_empleado | tipo_factura | ci_cliente_natural | nombre_cliente_natural")

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
    for row in rows:
        print(row)

except DatabaseError as ex:
    print("Error durante la conexión: {}".format(ex))

finally:
    connection.close()  # Se cerró la conexión a la BD.
    print("La conexión ha finalizado.")
