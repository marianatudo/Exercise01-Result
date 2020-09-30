"""
cliente:
    mira esta buenisimo peeeerroooooo, fijate que mi clientela a aumentado a veces tengo
    3 a veces 5  a veces 10 osea ya no se cuantos clientes tendre en un dia, podrias
    agregarle alguna forma de que yo le diga cuando quiero que se detenga y que me muestre
    el reporte de lo que llevo en costo total hasta ese momento.
"""

# creando la lista vacia
listaRegistro = []
clientes = 0
opcion = 0
costototal = 0

while opcion != 3:
    print("1. Ingresar cliente")
    print("2. Finalizar día")
    print("3. Salir")
    print(" ")
    opcion = int(input("¿Qué desea hacer? "))

    if opcion == 1:
        # Ingresar datos del cliente
        cliente = input("Nombre del cliente: ")
        producto = input("Producto: ")
        costo = float(input("Costo ($0.00): "))
        print(" ")
        # registro = {"cliente": cliente, "producto": producto, "costo": costo}
        registro = dict(cliente=cliente, producto=producto, costo=costo)
        # Guardar los datos a la lista
        listaRegistro.append(registro)
        # Agregar uno al total de clientes de ese día
        clientes += 1
        # Sumando el valor del costo
        costototal += float(registro["costo"])

    if opcion == 2:
        print("Reporte del día")
        print("Total de clientes: " + str(clientes))
        print("Costo Total: $" + str(costototal))
        print(" ")
        registro.clear()
        clientes = 0
        costototal = 0
