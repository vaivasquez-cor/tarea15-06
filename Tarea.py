reservas = []
valor="G"

def menu():
    menu="""
=== MENÚ PRINCIPAL ===

1. Registrar reserva
2. Buscar reserva
3. Eliminar reserva
4. Actualizar confirmaciones
5. Mostrar reservas
6. Mostar reservas confirmadas
7. Salir
"""
    print(menu)


def validar_codigo_reserva(valor):
    if "R" in valor[0]:
        
        if len(valor)== 7:
            if " " not in valor:
                if valor not in reservas:
                    print("Codigo de reserva ingresado")
                    return valor

                else:
                    print("Codigo ya se encuentra en uso")
            else:
                print("Codigo no debe contener espacios")
        else:
            print("El codigo debe tener exactamente 7 caracteres")
    else:
        print("Codigo reserva debe inciar con la letra r")


def validar_nombre_solicitante(valor):
    if len(valor) > 5:
        if valor.isalpha():
            return valor
        else:
            print("Nombre no puede contener numeros")
    else:
        print("Necesita minimo 5 caracteres")

def validar_tipo_sala(valor):
    if valor.upper() in ["P","M","G"]:
        return True
    else:
        return False


def validar_cantidad_personas(valor):
    try:
        cantidad = int(valor)
        if cantidad >= 2 and cantidad <= 20:
            return True
        return False
    except:
        return False

def validar_horas_reserva(valor):
    try:
        horas = int(valor)
        if horas >= 1 and horas <= 8:
            return True
        return False
    except:
        return False
    
#-------------------------------------------------------------------------------------------------------

def actualizar_estado(reservas):#busca la prioridad, si es <= a 4 cambia el estado a True
    for reserva in reservas:
        if reserva["cantidad_personas"] >=10:
            reserva["confirmada"] =True
        else:
            reserva ["confirmada"] =False
    print("Estados actualizados correctamente")

def buscar_reserva(reservas,codigo_reserva):#recorre la lista, retorna la posicion del id/ registros es la lista
    for posicion in range(len(reservas)):#posicion es un numero como x, desde el 0 que cuenta hasta terminar el rango de registros, que se saca el rango con len
        if reservas[posicion]["codigo_reserva"] == codigo_reserva:#
            return posicion#en que posicion de la lista esta
        return -1
def eliminar_reserva(reservas, codigo_reserva):
    posicion = buscar_reserva(reservas, codigo_reserva)
    if posicion == -1:
        print("Solicitud no encontrada")
    else:
        reservas.pop(posicion)
        print("Solicitud eliminada correctamente")

def mostrar_reservas(reservas):#recorre toda la lista y muestra cada diccionario
    if len(reservas) == 0:
        print("No existen reservas registradas")
        return
    for registro in reservas:
        print("\n------------------------------")
        print("Codigo de reserva:", registro["codigo_reserva"])
        print("Nombre del solicitante:", registro["nombre_solicitante"])
        print("Tipo de sala", registro["tipo_sala"])
        print("Cantidad de personas:", registro["cantidad_personas"])
        print("Horas reservadas:", registro["horas_reserva"])
        print("Confirmada:", registro["confirmada"])

def buscar_confirmadas(registros,confirmada):
    for posicion in range(len(registros)):
        if registros[posicion]["confirmada"] == confirmada:
            mostrar_reservas(registros)
        else:
            print("No hay reservas confirmadas")
#-----------------------------------------------------------------------------------------------
#Agregar reserva
def agregar_reserva(reservas):
    while True:
        codigo_reserva = input("Ingrese codigo reserva: ").upper()
        if not validar_codigo_reserva(codigo_reserva):
            print("Error: codigo inválido")
            continue
        break
    #pide los demas datos
    while True:
        nombre_solicitante = input("Ingrese nombre solicitante: ")
        if validar_nombre_solicitante(nombre_solicitante):
            break
        print("Error: nombre inválido")

    while True:
        tipo_sala = input("Ingrese área (P,M,G): ")
        if validar_tipo_sala(tipo_sala):
            tipo_sala= tipo_sala.upper()
            break
        print("Error: Ingrese una de las 3 tipos de sala(P,M,G)")

    while True:
        cantidad_personas = input("Ingrese cantidad de personas (2-20): ")
        if validar_cantidad_personas(cantidad_personas):
            cantidad_personas= int(cantidad_personas)
            break
        print("Error: cantidad de personas inválida")

    while True:
        horas_reserva = input("Ingrese horas de reserva: ")
        if validar_horas_reserva(horas_reserva):
            horas_reserva= int(horas_reserva)
            break
        print("Error: horas de reserva inválidas")

    reserva= {#se tiene que crear el diccionario dentro de la funcion con sus valores
        "codigo_reserva" : codigo_reserva,
        "nombre_solicitante" : nombre_solicitante,
            "tipo_sala" : tipo_sala,
            "cantidad_personas" : cantidad_personas,
            "horas_reserva" : horas_reserva,
            "confirmada" : False
    }

    #agregar a la lista
    reservas.append(reserva)
    print("Reserva agregada correctamente")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion >=1 and opcion <= 7:
                return opcion
            print("Error: debe ingresar una opción entre 1 y 6")
        except:
            print("Error: debe ingresar un número")


while True:
    
    menu()
    opcion = leer_opcion()
    if opcion == 1:
        agregar_reserva(reservas)
    elif opcion == 2:
        codigo_reserva = input("Ingrese reserva a buscar: ").upper()
        posicion = buscar_reserva(reservas, codigo_reserva)
        if posicion == -1:
            print("Reserva no encontrada")
        else:
            print("Reserva encontrada en la posición:", posicion)
    elif opcion == 3:
        codigo_reserva = input("Ingrese reserva a eliminar: ").upper()
        eliminar_reserva(reservas, codigo_reserva)
    elif opcion == 4:
        actualizar_estado(reservas)
    elif opcion == 5:
        mostrar_reservas(reservas)
    elif opcion == 6:
        confirmada = True
        buscar_confirmadas(reservas, confirmada)
    elif opcion == 7:
        print("Programa finalizado")
        break
        