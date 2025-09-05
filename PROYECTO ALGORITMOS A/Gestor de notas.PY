#FUNCIONES

def registrar_curso(cursos):
    nombre = input("Ingrese el nombre del curso: ")
    while nombre.strip() == "":
        print("El nombre no puede estar vacio")
        nombre = input("Ingrese el nombre del curso: ")
        
    nota = input ("Ingrese la nota (0-100): ")
    while not nota.isdigit() or not (0 <= int(nota) <= 100):
        print("La nota debe ser un numero ente 0 y 100.")
        nota = input("Ingrese la nota (0-100): ")   
    
    cursos.append((nombre, int(nota)))
    print("Curso registrado con exito")
    
def mostrar_cursos(cursos):
    if not cursos:
        print("No hay cursos registrados.")
    else:
        print("\n Cursos registrados.")
        for i, (curso, nota) in enumerate(cursos, start=1):
            print(f"{i}. {curso} - Nota: {nota}")        

def promedio_notas(cursos):
    if not cursos:
        print("No hay cursos registrados.")
    else:
        promedio = sum(nota for _, nota in cursos) / len(cursos)
        print(f"El promedio de notas es: {promedio:.2f}")
        
def contar_aprobados_reprobados(cursos):
    if not cursos:
        print("No hay cursos registrados.")
    else:
        aprobados = sum(1 for _, nota in cursos if nota >= 60)
        reprobados = len(cursos) - aprobados
        print(f"Cursos aprobados: {aprobados}")
        print(f"Cursos reprobados: {reprobados}") 
        
def buscar_curso(cursos):
    if not cursos:
        print("No hay cursos registrados.")
        return
    
    nombre_buscar = input("Ingrese el nombre de curso a buscar:").strip().lower()
    
    encontrado = False
    for i, (nombre, nota) in enumerate(cursos, start=1):
        if nombre.lower() == nombre_buscar:
            print (f"Encontrado{1}. {nombre} - Nota: {nota}")
            encontrado = True
            break
    if not encontrado:
        print(f"El curso no fue encontrado.")         
        
def actualizar_curso(cursos):
    if not cursos:
        print("No hay cursos registrados.")
        return
    
    mostrar_cursos(cursos)
    indice = input("Seleccione el numero del curso a actualizar:") 
    
    if indice.isdigit() and 1 <= int(indice) <= len(cursos):  
        indice = int(indice) - 1
        nuevo_nombre = input("Ingrese el nuevo nombre (Deje vacio si necesita mantener el nombre): ")
        nueva_nota = input("Ingrese la nueva nota (0-100, deje vacio para mantener la nota) ")
    
        nombre, nota = cursos[indice]
        if nuevo_nombre.strip():
            nombre = nuevo_nombre
        if nueva_nota.isdigit() and 0 <= int(nueva_nota) <= 100:
            nota = int(nueva_nota)
        
        cursos[indice] = (nombre, nota)  
        print("Curso actualizado con exito.")
    else:
        print("Opcion invalida.")

def eliminar_curso(cursos):
    if not cursos:
        print("No hay cursos registrados.")
        return
    
    mostrar_cursos(cursos)
    indice = input("Seleccione el numero del curso a eliminar:")
    
    if indice.isdigit() and 1 <= int(indice) <= len(cursos):
        indice = int(indice) - 1
        curso_eliminar = cursos [indice]
        
        confirmacion = input (f"¿Estas segura(o) de eliminar '{curso_eliminar[0]}'? (S/N): ").strip().lower()
        if confirmacion == "s":
            eliminado = cursos.pop(indice)
            print(f"Curso '{eliminado[0]}' eliminado.")
        else:
            print("Operacion Cancelada, no se elimino el curso.")
    else:
        print("Opcion invalida.")            

def menu_principal():
    cursos = []
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Registrar nuevo curso")
        print("2. Mostrar todos los cursos y notas")
        print("3. Calcular Promedio General")
        print("4. Contar cursos aprobados y reprobados")
        print("5. Buscar Curso por nombre (Busqueda Lineal)")
        print("6. Actualizar nota del Curso")
        print("7. Eliminar curso")
        print("8. Ordenar cursos por nota")
        print("9. Ordenar cursos por nombre")
        print("10. Buscar curso por nombre (Busqueda binaria)")
        print("11. Simular cola de solicitudes de revision")
        print("12. Mostrar historial de cambios")
        print("13. Salir")
        
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            registrar_curso(cursos)
        elif opcion == "2":
            mostrar_cursos(cursos)
        elif opcion == "3":
            promedio_notas(cursos)
        elif opcion == "4":
            contar_aprobados_reprobados(cursos)    
        elif opcion == "5":
            buscar_curso(cursos)
        elif opcion == "6":
            actualizar_curso(cursos)
        elif opcion == "7":
            eliminar_curso(cursos)
        elif opcion == "13":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida, intente nuevamente,")
            
menu_principal()                        
                