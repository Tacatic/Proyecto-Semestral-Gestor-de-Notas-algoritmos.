# ===== FUNCIONES ===== #

## Esta funcion es para registrar un nuevo curso con su respectiva nota ##
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

## Esta funcion permite mostrar los cursos y notas que hemos registrado ##    
def mostrar_cursos(cursos):
    if not cursos:
        print("No hay cursos registrados.")
    else:
        print("\n Cursos registrados.")
        for i, (curso, nota) in enumerate(cursos, start=1):
            print(f"{i}. {curso} - Nota: {nota}")        

## Esta funcion permite realizar una suma de las notas para poder dar un promedio de ellas ##
def promedio_notas(cursos):
    if not cursos:
        print("No hay cursos registrados.")
    else:
        promedio = sum(nota for _, nota in cursos) / len(cursos)
        print(f"El promedio de notas es: {promedio:.2f}")

## Esta funcion hace sumatoria de los cursos aprobados que son mayaores a 60 y reprobados que son menores a 60 ##        
def contar_aprobados_reprobados(cursos):
    if not cursos:
        print("No hay cursos registrados.")
    else:
        aprobados = sum(1 for _, nota in cursos if nota >= 60)
        reprobados = len(cursos) - aprobados
        print(f"Cursos aprobados: {aprobados}")
        print(f"Cursos reprobados: {reprobados}") 

## Esta funcion permite realizar una busqueda de forma lineal ##
## lo que quiere decir que no importa si lo buscamos con mayusculas o minusculas ##        
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

## En esta funcion podemos realizar cambios ##
## Es decir si necesitamos cambiarle nombre o nota a nuestro curso ##        
def actualizar_curso(cursos, historial):
    if not cursos:
        print("No hay cursos registrados.")
        return
    
    mostrar_cursos(cursos)
    indice = input("Seleccione el numero del curso a actualizar:") 
    
    if indice.isdigit() and 1 <= int(indice) <= len(cursos):  
        indice = int(indice) - 1     
        old_nombre, old_nota = cursos[indice]
        
        nueva_nota = input("Ingrese la nueva nota (0-100, deje vacio para mantener la nota) ")
        if nueva_nota.isdigit() and 0 <= int(nueva_nota) <= 100:
            nota = int(nueva_nota)
            cursos[indice] = (old_nombre, nota)
            print("Curso actualizado con exito.")
            historial.append(f"Se Acualizo la nota {old_nombre}: de ({old_nota}) a  Nueva nota: ({nota})")
        else:
            print("Nota invalida, la nota debe estar entre 0 y 100")
    else:
        print("Opcion invalida.")

## Esta funcion nos permite eliminar una nota registrada con su respectiva nota ##
## Pero no sin antes preguntarle al usuario si en realidad debe eliminar el curso ##
def eliminar_curso(cursos, historial):
    if not cursos:
        print("No hay cursos registrados.")
        return
    
    mostrar_cursos(cursos)
    indice = input("Seleccione el numero del curso a eliminar:")
    
    if indice.isdigit() and 1 <= int(indice) <= len(cursos):
        indice = int(indice) - 1
        curso_eliminar = cursos [indice]
        
        confirmacion = input (f"¿Estas segura(o) de eliminar '{curso_eliminar[0]}'? (Si/No): ").strip().lower()
        if confirmacion == "si":
            eliminado = cursos.pop(indice)
            print(f"Curso '{eliminado[0]}' eliminado.")
            
            historial.append(f"Se Elimino: {eliminado[0]} - Nota: {eliminado[1]}")
        else:
            print("Operacion Cancelada, no se elimino el curso.")
    else:
        print("Opcion invalida.")
        
def curso_nota(cursos):
    n = len(cursos)
    comps = swaps = 0
    changed = True
    while changed:
        changed = False
        for i in range (n - 1):
            comps += 1
            if cursos [i][1] < cursos [i+1][1]:  #solo cambiamos el signo mayo para hacerlo de forma ascendente
                cursos [i], cursos[i+1] = cursos[i+1], cursos [i]
                swaps += 1
                changed = True
        n -= 1

    print("\nCursos ordenados por nota")
    for i, (curso, nota) in enumerate(cursos, start=1):
        print(f"{i}. {curso} - Nota: {nota}") 
    
def curso_nombre(cursos):
    comps = moves = 0
    for i in range(1, len(cursos)):
        clave = cursos[i]
        j = i - 1
        while j >= 0:
            comps += 1
            if cursos [j][0].lower() > clave[0].lower():
                cursos[j+1] = cursos[j]
                moves += 1
                j -= 1
            else:
                break
        cursos[j+1] = clave
        
    print("\nCursos ordenados por nombre")
    for i, (curso, nota) in enumerate(cursos, start=1):
        print(f"{i}. {curso} - Nota: {nota}")  
        
        
def busqueda_binaria(cursos):
    if not cursos:
        print("No hay cursos registrados")
        return
    
    cursos.sort(key=lambda x: x[0].lower())
    
    nombre_buscar = input("Ingrese el nombre del curso: ").strip().lower()
    
    min = 0
    max = len(cursos) - 1
    encontrado = False
    while min <= max:
        medio = (min+max) // 2
        nombre_medio = cursos[medio][0].lower()
        if nombre_medio == nombre_buscar:
            print(f"Curso encontrado: {cursos[medio][0]} - Nota:{cursos[medio][1]}")
            encontrado = True
            break
        elif nombre_medio < nombre_buscar:
            min = medio + 1
        else:
            max = medio - 1
    if not encontrado:
        print(f"\nEl curso {nombre_buscar} no fue encontrado")

def revision_cola(cursos):
    if not cursos:
        print("No hay cursos registrados")
        return
    
    cola = []
    
    print("\nIngrese los cursos que desea enviar a revisión")
    print("Escriba fin para terminar\n")

    while True:
        curso = input("Curso a revisar: ").strip()
        if curso.lower() == "fin":
            break
        cola.append(curso)
    
    if not cola:
        print("\nNo se ingresaron solicitudes de revision")
    else:
        print("\nProcesando solicitudes de revision")
        for curso in cola:
            print(f"Revisando el curso {curso}")
    print("\nTodas las solicitudes fueron atendidas")
    
def mostrar_historial(historial):
    if not historial:
        print("\nNo hay cambios registrados en el historial")
    else:
        print("\nHistorial de cambios")      
        for i, cambio in enumerate(reversed(historial), start=1):
            print(f"{i}. {cambio}")                                                            
# ========== Menu Principal ========== #                     

def menu_principal():
    cursos = []
    historial = []
    
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Registrar nuevo curso")
        print("2. Mostrar todos los cursos y notas")
        print("3. Calcular Promedio General")
        print("4. Contar cursos aprobados y reprobados")
        print("5. Buscar Curso por nombre (Busqueda Lineal)")
        print("6. Actualizar nota del Curso")
        print("7. Eliminar curso")
        print("8. Ordenar cursos por nota (ordenamiento burbuja)")
        print("9. Ordenar cursos por nombre (Ordenamiento insercion)")
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
            actualizar_curso(cursos, historial)
        elif opcion == "7":
            eliminar_curso(cursos, historial)
        elif opcion == "8":
            curso_nota(cursos)
        elif opcion == "9":
            curso_nombre(cursos)
        elif opcion == "10":
            busqueda_binaria(cursos)
        elif opcion == "11":
            revision_cola(cursos)
        elif opcion == "12":
            mostrar_historial(historial)   
        elif opcion == "13":
            print("Gracias por usar el Gestor de Notas Académicas. ¡Hasta pronto!")
            break
        else:
            print("Opcion invalida, intente nuevamente,")
            
menu_principal()                        
                