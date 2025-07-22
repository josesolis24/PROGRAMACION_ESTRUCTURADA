
#listas= [
    #["Ruben", 10, 0, 10, 0, 10, 0],
    #["Diana", 10, 0, 9, 8, 8, 0],
    #["Jose", 5, 0, 6, 0, 7, 0],
   
#]

def borra_pantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t... Oprime  una tecla para continuar...")

def menu_pricpal():
    print("\n\t..::: 📊Sistema de Gestión de Calificacones📊  :::...\n\n 1️⃣ Agregar  \n 2️⃣ Mostrar \n 3️⃣ Calcular Promedio  \n 4️⃣ SALIR ")
    opcion=input("\t Elige una opción (1-4):  ").upper()
    return opcion  

def Agregar_Calificaciones(lista):
    borra_pantalla()
    print("\n\t ..::: 📂Agregar Calificaciones📂 :::...\n")
    nombre = input("\n\t Ingresa el nombre del alumno: ")
    calificaciones = []
    for i in range(1,4):
        
        calificacion = float(input(f"\t Ingresa la calificación {i+1} de {nombre}: "))
        calificaciones.append(calificacion)
    lista.append([nombre] + calificaciones)
    print(f"\n\t ✅Calificaciones de {nombre} agregadas exitosamente.✅")
    esperarTecla()
    return lista
    
def Mostrar_Calificaciones(lista):

    if not lista:
        print("\n\t ❌No hay calificaciones registradas.❌")
    else:
        print("\n\t Calificaciones Registradas:")
        for alumno in lista:
            print(f"\t {alumno[0]}: {alumno[1:]}")
    esperarTecla()


def Calcular_Promedios(lista):
    
    if not lista:
        print("\n\t ❌No hay calificaciones registradas.❌")
    else:
        print("\n\t Promedios de Calificaciones:")
        for alumno in lista:
            nombre = alumno[0]
            calificaciones = alumno[1:]
            promedio = sum(calificaciones) / len(calificaciones)
            print(f"\t {nombre}: {promedio:.2f}")
    esperarTecla()

