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
6. Salir
"""
    print(menu)


def validar_codigo_reserva(valor):
    if "R" in valor[0]:
        print("si")
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
            print("ola")
        else:
            print("Nombre no puede contener numeros")
    else:
        print("Necesita minimo 5 caracteres")

def validar_tipo_sala(valor):
    if valor.upper() in ["P","M","G"]:
        return True
    else:
        print("Ingrese una de las 3 tipos de sala(P,M,G)")


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
        if horas >= 2 and horas <= 20:
            return True
        return False
    except:
        return False

def actualizar_estado(reservas):#busca la prioridad, si es <= a 4 cambia el estado a True
    for reserva in reservas:
        if reserva["cantidad_personas"] >=10:
            reserva["estado"] =True
        else:
            reserva ["estado"] =False
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

#Agregar reserva
def agregar_reserva(reservas):
    while True:
        codigo_reserva = input("Ingrese codigo reserva: ")
        if not validar_codigo_reserva(codigo_reserva):
            print("Error: codigo inválido")
            continue
        break
    #pide los demas datos
    while True:
        nombre_solicitante = input("Ingrese nombre equipo: ")
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
        cantidad_personas = input("Ingrese prioridad (1-5): ")
        if validar_cantidad_personas(cantidad_personas):
            prioridad= int(prioridad)
            break
        print("Error: cantidad de personas inválida")

    while True:
        horas_reserva = input("Ingrese horas de reserva: ")
        if validar_horas_reserva(horas_reserva):
            horas_reserva= int(horas_reserva)
            break
        print("Error: horas de reserva inválidas")

    solicitud= {#se tiene que crear el diccionario dentro de la funcion con sus valores
        "id_solicitud" : id_solicitud,
        "nombre_equipo" : nombre_equipo,
            "area" : area,
            "prioridad" : prioridad,
            "costo_estimado" : costo_estimado,
            "estado" : False
    }

    #agregar a la lista
    registros.append(solicitud)
    print("Solicitud agregada correctamente")

agregar_reserva()
#validar_nombre_solicitante(valor)
#validar_codigo_reserva(valor)
#validar_tipo_sala(valor)
