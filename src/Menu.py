import R1
import R2
import R4
import R6
import R7
import R9
import R11
import R14
import R3
import R8
import R12
import os

def cls():
    if os.name == "nt":
        os.system("cls")
    else: 
        os.system("clear")

while (True):
    
    cls()
    print("                                             --  Menú de concesioria los carros hermanos.  --                                                         ")
    print("1. Borrar, crear, modificar de una compra o venta.                                                                                                    ")
    print("2. Ver las estadisticas de vehiculos comprados y vendidos (dias mes o años).                                                                          ")
    print("3. mostrar los datos del dueño actual o anterios del vehiculo correspondiente.                                                                        ")
    print("4. Mostrar los datos del empleados que vendieron o compraron un carro y el cliente o vendedor.                                                        ")
    print("5. Administrar la compra de seguro de los clientes.                                                                                                   ")
    print("6. Mostrar los repuestos necesarios para un carro junto a la descripción dada por el taller de las reparaciones. Indicar por cada pieza el proveedor. ")
    print("7. Mostrar historial de compras y ventas en un evento.                                                                                                ")
    print("8. Mostrar los premios que ha ganado un carro si participo en un evento o carrera, en caso de ser una carrera, mostrar también la posición, los datos del piloto y los pits")
    print("9. Modificar o eliminar registro de cada entidad en la base de datos (Solo administradores).                                                          ")
    print("10. Si se presta uno o varios vehículos a una empresa para una exhibición o evento, mostrar una descripción del evento, días de préstamo, y pago por posibles daños")
    print("11. Hacer un reporte de ganancias del mes en eventos, carreras, seguro y ventas                                                                        ")
    print("12. Salir                                                                                                                                              ")
    print("Por favor, Ingrese una opción                                                                                                                         ")
    x = input("-> ")

    if x == "1":
        cls()
        R1.main()
    elif x == "2":
        cls()
        R2.main()
    elif x == '3':
        cls()
        R3.main()
    elif x == "4":
        cls()
        R4.main()
    elif x == "5":
        cls()
        R6.main()
    elif x == "6":
        cls()
        R7.main()
    elif x == "7":
        cls()
        R9.main()
    elif x == "8":
        cls()
        R8.main()
    elif x == "9":
        cls()
        R11.main()
    elif x == "10":
        cls()
        R12.main()
    elif x == "11":
        cls()
        R14.main()
    elif x == "12":
        break
