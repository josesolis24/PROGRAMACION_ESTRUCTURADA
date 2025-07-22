
def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
    input("Oprima cualquier tecla para continuar")

def menu_principal():
   print(".:: Sistema de Agenda ::.. "
         "\n1️⃣ Agregar contacto  "
         "\n2️⃣ Mostrar todos los contactos"
         "\n3️⃣ Buscar contactos por nombre "
         "\n4️⃣ Modificar Contacto "
         "\n5️⃣ Eliminar contacto "
         "\n6️⃣ SALIR ")
   opcion=input("Elige una opción (1️⃣➖6️⃣): ") 
   return opcion

def agregar_contacto(agenda):
   borrarPantalla()
   print("👤Agregar Contacto👤")
   nombre = input("Nombre: ") .upper() .strip()
   if nombre in agenda:
      print("✅El contacto existente✅")
   else:
      tel=input("Teléfono: ") .strip()
      email=input("Email: ") .strip() .strip()
      agenda[nombre]=[tel, email]
      print("✅Accion realizada con exito✅")

def mostrar_contactos(agenda):
   borrarPantalla()
   print("👤Mostrar Contactos👤")
   if not agenda:
      print("❌No hay contactos❌")
   else:
      print(f"{'Nombre':<15} {'Teléfono':<15} {'Email':<15}")
      print("-"*60)
      for nombre, datos in agenda.items():
         print(f"{nombre:<15} {datos[0]:<15} {datos[1]:<15}")
         print("-"*60)

def buscar_contacto(agenda):
    borrarPantalla()
    print("Buscar Contacto👤")
    if not agenda:
        print("❌No hay contactos❌") 
    else:
       print("❌No existe el contacto❌")
       
def modificar_contacto(agenda):
    borrarPantalla()
    print("Modificar Contacto👤")
    if not agenda:
        print("❌No hay contactos❌") 
    else:
        nombre = input("Nombre: ").upper().strip()
        if nombre in agenda:
           print(f'{"Nombre":<15} {"Teléfono":<15} {"Email":<15}')
           print("-"*60)
           print(f"{nombre:<15} {agenda[nombre][0]:<15} {agenda[nombre][1]:<15}")
           print("-"*60)
           resp= input("¿Desea modificar el contacto? (Si/No): ").upper().strip()
           if resp == "SI":
                tel = input("Teléfono: ").strip()
                email = input("Email: ").strip()
                agenda[nombre]=[tel, email]
                print("✅Accion realizada con éxito✅")
           else:
                print("❌No se modificó el contacto❌")
            
        else:
            print("El contacto no existe") 

def eliminar_contacto(agenda):
    borrarPantalla()
    print("Eliminar Contacto")
    if not agenda:
        print("❌No hay contactos❌") 
    else:
        nombre = input("Nombre del contacto a buscar: ").upper().strip()
        if nombre in agenda:
            print(f'{"Nombre":<15} {"Teléfono":<15} {"Email":<15}')
            print("-"*60)
            print(f"{nombre:<15} {agenda[nombre][0]:<15} {agenda[nombre][1]:<15}")
            print("-"*60)
            resp = input("¿Desea eliminar el contacto? (Si/No): ").upper().strip()
            if resp == "si":
                agenda.pop(nombre)
                print("✅Accion Realizada  con éxito✅")
            else:
                print("❌Este contacto no existe❌")
                        


   
  

