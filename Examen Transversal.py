planes = {
    "F001" : ["Plan Basico", "mensual", 1, False, "libre"],
    "F002" : ["Plan Full", "mensual", 1, True, True, "libre"],
    "F003" : ["Plan Estudiante", "trimestral", 3, False, True, "tarde"],
    "F004" : ["Plan Senior", "trimestral", 3, True, False, "mañana"],
    "F005" : ["Plan Anual Pro", "anual", 12, True, True, "libre"],
    "F006" : ["Plan Nocturno", "mensual", 1, False, True, "noche"],
}
inscripciones = {
    "F001" : [14990, 30],
    "F002" : [22990, 10],
    "F003" : [39990, 0],
    "F004" : [35990, 6],
    "F005" : [159990, 2],
    "F006" : [18990, 15],
}
def cupos_tipo(plan):
    total = 0
    plan = plan.lower()
    for tipo in inscripciones:
        nombre_plan = planes [tipo] [1].lower()
        if nombre_plan == planes:
            total += inscripciones [tipo] [1]
    print(f"El total de cupos disponibles es de:{total}")
def busqueda_precio(p_min,p_max):
    resultado = []
    for cupos in inscripciones:
         plan = inscripciones [cupos] [0]
         cupos = inscripciones [cupos] [1]
         if p_min <= plan <= p_max and cupos != 0:
             cupos = planes [cupos][0]
             resultado.append(f"{plan}--{cupos}")
             if len(resultado) == 0:
                 print("No hay planes en ese rango de precio.")
             else:
                 print(f"resultado:{resultado}")
def buscar_codigo(codigo):
    if codigo in inscripciones:
        return True
    else:
        return False
def actualizar_precio(cupos, p):
    if cupos in inscripciones:
        inscripciones [cupos][0] = p
        return True
    else:
        return False
def eliminar_plan(ecodigo):
    buscar_codigo()

def main():
    while True:
        print("============== MENÚ PRINCIPAL ==============")
        print("1. Cupos por tipo de plan.")
        print("2. Busqueda de planes por rango de precio.")
        print("3. Actualizar precio de plan.")
        print("4. Agregar Plan")
        print("5. Eliminar plan.")
        print("6. Salir.")
        opc = input ("ingrese una opcion del menu:")
        if opc == "1":
            plan = input ("plan que desea consultar:")
            cupos_tipo(plan)
        elif opc == "2":
            while True:
                try:
                    p_min = int(input("Ingrese el precio minimo a buscar:"))
                    p_max = int(input("ingrese el precio maximo a buscar:"))
                    break
                except ValueError:
                    print("ingrese valores enteros!")
                    busqueda_precio(p_min, p_max)
        elif opc == "3":
            while True:
                cupos = input("plan que desea actualizar:")
                nuevo_precio = input("Ingrese el nuevo precio:")
                actualizado = actualizar_precio(cupos, nuevo_precio)
                if actualizado:
                    print("Precio actualizado.")
                    break
                else:
                    print("No existe.")
                    respuesta = input("Desea actualizar otro precio?(s/n):")
                    if respuesta.lower() == "no" or respuesta.lower() == "n":
                        break
        elif opc == "4":
            pass
        elif opc == "5":
            pass
        elif opc == "6":
            print("programa finalizado.")
        else:
            print("ingrese una opcion valida.")
main()