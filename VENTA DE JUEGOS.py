import datetime
import json

# Catálogo de pizzas con sus precios según tamaño
catalogo_juegos = {"nintendo corporation":{"nintendo switch":{"aventura":{"Princess Peach: Showtime!":28990,"Mario vs. Donkey Kong":31990,"Hogwarts Legacy":28990}}},
                   "playstation":{"ps5":{"accion":{"METAL SLUG ATTACK RELOADED":9990,"Crown Wars":36990},"deporte":{"EA SPORTS FC 24 FIFA 24":26990,"TopSpin 2K25":22990,"Rugby 22":32990}},"ps4":{"disparos":{"Call of Duty Black Black Ops 6":42990,"Red Dead Redemption + Undead Nightmare":32990}}},
                   "xbox":{"xbox one":{"rpg":{"Karos: Cronicas de Rosh":59990,"Crash bandicoot":39990}}}}

# Registro de ventas (inicialmente vacío)
ventas = []

def mostrar_menu():
    print("\nBienvenido a GAME DUOC UC ")
    print("1. Registrar una venta")
    print("2. Mostrar todas las ventas")
    print("3. Buscar ventas por cliente")
    print("4. Guardar las ventas en un archivo")
    print("5. Cargar las ventas desde un archivo")
    print("6. Generar Factura")
    print("7. Salir del programa")

def registrar_venta():
    cliente = input("\nIngrese el nombre del cliente: ")

    empresa = input("\nElija la consola del juego:\n1.Nintendo Corporation\n2.Playstation\n3.XBOX\n : ")
    if empresa=="1":
        empresa="nintendo corporation"
    elif empresa=="2":
        empresa="playstation"
    elif empresa=="3":
        empresa="xbox"  
    else:
        print("Compañia no existente")
        return

    consola = input("\ntipo de consola: \n1.Nintendo Switch\n2.Ps5\n3.Ps4\n4.XBOX one\n5.XBOX S\n : ")
    if consola=="1":
        consola="nintendo switch"
        genero = input("\nGenero del juego:\n1.aventura\n : ") 
        if genero=="1":
            genero="aventura"
            juego = input("\nSeleccione Juego :\n1.Princess Peach: Showtime!\n2.Mario vs. Donkey Kong\n3.Hogwarts Legacy\n : ")
            if juego=="1":
                    juego="Princess Peach: Showtime!"
            elif juego=="2":
                juego="Mario vs. Donkey Kong"  
            elif juego=="3":
                juego="Hogwarts Legacy"
            else:
                print("Tipo de juego no existente")  
                return
        else:
            print("No tenemos juegos de ese genero")
            return

    elif consola=="2":
        consola="ps5"
        genero = input("\nGenero del juego:\n1.accion\n2.deporte\n : ")    
        if genero=="1":
            genero="accion"
            juego = input("\nSeleccione Juego :\n1.METAL SLUG ATTACK RELOADED\n2.Crown Wars")
            if juego=="1":
                    juego="METAL SLUG ATTACK RELOADED"
            elif juego=="2":
                juego="Crown Wars"  
            else:
                print("Tipo de juego no existente")  
                return
        elif genero=="2":
            genero="deporte"
            juego = input("\nSeleccione Juego :\n1.EA SPORTS FC 24 FIFA 24\n2.TopSpin 2K25\n3.Rugby 22\n : ")
            if juego=="1":              
                    juego="EA SPORTS FC 24 FIFA 24"
            elif juego=="2":
                juego="TopSpin 2K25"  
            elif juego=="3":
                juego="Rugby 22" 
            else:
                print("Tipo de juego no existente")  
                return       
        else:
            print("No tenemos juegos de ese genero")    
            return
        
    elif consola=="3":
        consola="ps4"
        genero = input("\nGenero del juego:\n1.disparos\n : ")
        if genero=="1":
            genero="disparos"
            juego = input("\nSeleccione Juego :\n1.Call of Duty Black Black Ops 6\n2.Red Dead Redemption + Undead Nightmare\n : ")
            if juego=="1":
                juego="Call of Duty Black Black Ops 6"
            elif juego=="2":
                juego="Red Dead Redemption + Undead Nightmare"  
            else:
                print("Tipo de juego no existente")  
                return  
        else:
            print("No tenemos juegos de ese genero")    
            return

    elif consola=="4":
        consola="xbox one"
        genero = input("\nGenero del juego:\n1.rpg\n : ")
        if genero=="1":
            genero="rpg"
            juego = input("\nSeleccione Juego :\n1.Karos: Cronicas de Rosh\n2.Crash bandicoot\n : ")
            if juego=="1":
                juego="Karos: Cronicas de Rosh"
            elif juego=="2":
                juego="Crash bandicoot"  
            else:
                print("Tipo de juego no existente")  
                return  
        else:
            print("No tenemos juegos de ese genero")    
            return      
    else:
        print("Tipo de consola no existente")  
        return   
        

    if empresa in catalogo_juegos and consola in catalogo_juegos[empresa]:
        precio = catalogo_juegos[empresa][consola][genero][juego]
    else:
        print("Compañia o consola no válido.")
        return
    
    tipo_usuario = input("\nIngrese el tipo de usuario (Estudiante/Trabajador,Socio): ").lower()
    descuento = 0.0

    if tipo_usuario == "estudiante":
        descuento = 0.15
    elif tipo_usuario == "trabajador":
        descuento = 0.10
    elif tipo_usuario == "socio":
        descuento = 0.20
    else:
        print("Tipo de usuario no válido.")
        return
    
    total_descuento = precio * descuento
    precio_final = precio - total_descuento

    venta = {
        "cliente": cliente,
        "empresa": empresa,
        "consola": consola,
        "genero":genero,
        "juego":juego,
        "precio_final": precio_final,
        "fecha_hora": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    ventas.append(venta)
    print("Venta registrada satisfactoriamente.")
    
def mostrar_ventas():
    if ventas:
        for idx, venta in enumerate(ventas, start=1):
            print(f"\nVenta {idx}:")
            print(f"Cliente: {venta['cliente']}")
            print(f"Compañia: {venta['empresa']}")
            print(f"Consola: {venta['consola']}")
            print(f"Genero: {venta['genero']}")
            print(f"Juego: {venta['juego']}")
            print(f"Precio final: ${venta['precio_final']:.2f}")
            print(f"Fecha y hora: {venta['fecha_hora']}")
    else:
        print("No hay ventas registradas.")

def buscar_clientes():
    buscar=input("\nIngrese el nombre del Cliente: ")
    cliente_encontrado=False
    for venta in ventas:
        if venta["cliente"].lower()==buscar.lower():    
            print(f"\nCliente: {venta['cliente']}")
            print("-------------------------------------------")
            print(f"Compañia    : {venta['empresa']}")
            print(f"Consola     : {venta['consola']}")
            print(f"Genero      : {venta['genero']}")
            print(f"Juego       : {venta['juego']}")
            print("-------------------------------------------")
            cliente_encontrado=True
            break
    if not cliente_encontrado:
            print(f"Cliente {buscar} no tiene ningun pedido realizado.")

def guardar_datos():

    with open('ventas.json', 'w') as file:
        json.dump(ventas, file, indent=4)
    print(f"Ventas guardadas en ventas.json. ")

def cargar_datos():
    
    try:
        with open('ventas.json', 'r') as file:
            global ventas
            ventas = json.load(file)
        print(f"ventas cargadas desde ventas.json. ")
    except FileNotFoundError:
        print(f"El archivo ventas.json no existe.")

def generar_boleta():
    boleta=input("\nIngrese el nombre del Cliente: ")
    cliente_encontrado=False
    for venta in ventas:
        if venta["cliente"].lower()==boleta.lower():    
            print("\n------------ Boleta de Venta -----------")
            print(f"Fecha y hora: {venta['fecha_hora']}")
            print(f"Cliente: {venta['cliente']}")
            print("----------------------------------------")
            print(f"Compañia    : {venta['empresa']}")
            print(f"Consola     : {venta['consola']}")
            print(f"Genero      : {venta['genero']}")
            print(f"Juego       : {venta['juego']}")
            print(f"Precio final: ${venta['precio_final']:.2f}")
            print("----------------------------------------")
            cliente_encontrado=True
            break
    if not cliente_encontrado:
            print(f"Cliente {boleta} no tiene ningun pedido realizado.")

while True:
        mostrar_menu()
        opcion = input("\tOPC: ")

        if opcion == '1':
            registrar_venta()

        elif opcion == '2':
            mostrar_ventas()

        elif opcion == '3':
            buscar_clientes()  

        elif opcion == '4':
            guardar_datos()

        elif opcion == '5':
            cargar_datos()

        elif opcion == '6':
            generar_boleta()

        elif opcion == '7':
            print("Saliendo del Programa.....") 
            break          
        else:
            print("Seleccione una opcion valida")