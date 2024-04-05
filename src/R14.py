import psycopg2
from psycopg2 import DatabaseError

# Hacer un reporte de ganancias del mes en eventos, carreras, seguro y ventas #

def menu():
    print("\n--     Reporte de ganancias del mes    --")
    print("1. Evento ")
    print("2. Carreras ")
    print("3. Ventas ")
    print("4. Seguro")
    print("5. Salir ")
     
def main():
    try:
        connection_string = "postgresql://concesionaria_owner:WtN7HmGxF9pg@ep-weathered-glitter-a4gsgrak.us-east-1.aws.neon.tech/CONCESIONARIA?sslmode=require"
        connection = psycopg2.connect(connection_string)
        cursor = connection.cursor()
        print("Conexión exitosa. ")
        
        while True:
            menu()
            x = input("Por favor, Ingresa una opcion: ")
            
            if x == "1":
                try:
                    mesus = input("\nIngrese el mes a elegir: ")
                    yearus = input("Ingrese el año a elegir: ")
                
                    cursor.execute(f"SELECT * FROM evento WHERE extract(month FROM fecha) = {mesus} AND extract(year FROM fecha) = {yearus};")
                
                    print(f"\nCarros vendidos en el mes {mesus} y del año {yearus}")
                    datos = cursor.fetchall()
            
                    id_evento = []
            
                    for row in datos:
                        id_evento.append(row[0])

                    cadena = str(id_evento)[1:-1]
            
                    cursor.execute(f"SELECT * FROM exposicion_evento WHERE id_evento IN ({cadena})")
                    datos1 = cursor.fetchall()

                    vin_vehiculo = []
            
                    for row in datos1:
                         vin_vehiculo.append(row[1])
                
                    cadena1 = str(vin_vehiculo)[1:-1]
                
                    cursor.execute(f"SELECT * FROM vehiculo WHERE vin_vehiculo IN ({cadena1})")
                    datos2 = cursor.fetchall()
            
                    for row in datos2:
                        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]}")
                
                    precio_evento = 0
            
                    for row in datos2:
                        precio_evento += row[2]
                    
                    print(f"\nPrecio total de ventas en los eventos: {precio_evento}")
                    pass
                
                except:
                    print("No existe registro de ese mes. ")
            
            elif x == "2":
                try:
                    mesus = input("\nIngrese el mes a elegir: ")
                    yearus = input("Ingrese el año a elegir: ")
                    cursor.execute(f"SELECT * FROM carrera WHERE extract(month FROM fecha) = {mesus} AND extract(year FROM fecha) = {yearus};")
                    datos = cursor.fetchall()
                
                    precio_carrera = 0
                
                    for row in datos:
                        precio_carrera += row[5]
                
                    if precio_carrera == 0:
                        print("No hubo carreras ganadas ese mes. ")
                    
                    else:    
                        print(f"\nPrecio total de dinero ganado en carreras: {precio_carrera}")
                    pass
                except:
                    print("No existe registro de ese mes. ")
                    
            elif x == "3":
                try:
                    mesus = input("\nIngrese el mes a elegir: ")
                    yearus = input("Ingrese el año a elegir: ")
                    cursor.execute(f"SELECT * FROM factura WHERE extract(year from dia) = {yearus} AND extract(month from dia) = {mesus};")
                    datos = cursor.fetchall()
                
                    id_factura = []
                
                    for row in datos:
                        id_factura.append(row[0])
                
                    cadena = str(id_factura)[1:-1]
                
                    cursor.execute(f"SELECT * FROM detalle WHERE id_factura IN ({cadena})")
                    datos1 = cursor.fetchall()
                
                    id_detalle = []
                
                    for row in datos1:
                        id_detalle.append(row[0])
            
                    cadena1 = str(id_detalle)[1:-1]
                    
                    cursor.execute(f"SELECT * FROM detalle_total WHERE id_detalle IN ({cadena1})")
                    datos2 = cursor.fetchall()
                
                    precio_ventas = 0
                
                    for row in datos2:
                        precio_ventas += row[1]
                    print(f"Estas son las ventas totales en el mes {mesus} y el año {yearus}: {precio_ventas}")
                except:
                    print("No existe registro de ese mes. ")
                pass
            elif x == "4":
                try:
                    mesus = input("\nIngrese el mes a elegir: ")
                    yearus = input("Ingrese el año a elegir: ")
                    cursor.execute(f"SELECT * FROM factura WHERE extract(year from dia) = {yearus} AND extract(month from dia) = {mesus};")
                    datos = cursor.fetchall()
                    
                    id_factura = []
                    
                    for row in datos:
                        id_factura.append(row[0])
                
                    cadena = str(id_factura)[1:-1]
                    cursor.execute(f"SELECT * FROM detalle WHERE id_factura IN ({cadena});")
                    datos1 = cursor.fetchall()
                    
                    id_seguro = []
                    
                    for row in datos1:
                        id_seguro.append(row[3])
                    
                    precio_total = 0
                    
                    id_seguro_copy = id_seguro
                    count = len(id_seguro_copy)


                    for elemento in range(count):
                        if id_seguro_copy[elemento] == 1:
                            precio_total += 200
                        elif id_seguro_copy[elemento] == 2:
                            precio_total += 700
                        elif id_seguro_copy[elemento] == 3:
                            precio_total += 500
                        elif id_seguro_copy[elemento] == 4:
                            precio_total += 1000
                        elif id_seguro_copy[elemento] == 5:
                            precio_total += 0
                            
                    print(precio_total)
                except:
                    print("No existe registro de ese mes. ")
                    
            elif x == "5" :
                print("Bye bye!")
                break
            
            
    except DatabaseError as ex:
        print("Error durante la conexión: {}".format(ex))
        
        
main()

    
    
    

    