import psycopg2
from psycopg2 import DatabaseError

# Hacer un reporte de ganancias del mes en eventos, carreras, seguro y ventas #

def menu():
    print("\n--     Reporte de ganancias del mes    --")
    print("1. Evento ")
    print("2. Carreras ")
    print("3. Seguro ")
    print("4. Salir ")
     
def main():
    
    try:
        connection = psycopg2.connect(
                host='localhost', 
                user='postgres',
                password='123', # Clave para acceder a la base de datos
                database='concesionaria',
                port = "5433" # En caso de tener versiones diferentes de sql usar el puerto de la version.
        )
        print("Conexión exitosa. ")
        
        while True:
            menu()
            x = input("Por favor, Ingresa una opcion: ")
            
            if x == "1":
                mesus = input("\nIngrese el mes a elegir: ")
                yearus = input("Ingrese el año a elegir: ")
                cursor = connection.cursor()
                
                cursor.execute(f"SELECT * FROM evento WHERE extract(month FROM fecha) = {mesus} AND extract(year FROM fecha) = {yearus};")
                
                print("No hubo ganancias ese mes. ")
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
            
            elif x == "2":
                mesus = input("\nIngrese el mes a elegir: ")
                yearus = input("Ingrese el año a elegir: ")
                cursor = connection.cursor()
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
                
            elif x == "3":
                pass
            
    except DatabaseError as ex:
        print("Error durante la conexión: {}".format(ex))
        
        
main()

    
    
    

    