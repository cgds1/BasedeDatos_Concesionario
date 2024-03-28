import psycopg2
from psycopg2 import DatabaseError

def main():
    
    try:
        connection = psycopg2.connect(
                host='localhost', 
                user='postgres',
                password='123', # Clave para acceder a la base de datos
                database='concesionaria',
                port = "" # En caso de tener versiones diferentes de sql usar el puerto de la version.
        )
        print("Conexión exitosa.")
        
    except DatabaseError as ex:
        print("Error durante la conexión: {}".format(ex))
        
main()