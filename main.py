from controlador.controlador import Controlador

def mostrar_menu():
    print("============= Menu principal ================")
    print("1 - Registrar alumno")
    print("2 - Registrar docente")
    print("3 - Registrar curso")
    print("4 - Asignar docente")
    print("5 - Matricular alumno")
    print("6 - Listar alumnos")
    print("7 - Listar docentes")
    print("8 - Listar cursos")
    print("9 - Salir")
    print("=============================================")

def main():
    controlador = Controlador()

    while True:
        mostrar_menu()
        opcion = input("Ingrese una opcion: ")

        if opcion == '1':
            rut = input("Ingrese el Rut del alumno: ")
            nombre = input("Ingrese el nombre del alumno: ")
            apellido = input("Ingrese el apellido del alumno: ")
            fecha_nacimiento = input("Ingrese la fecha de nacimiento del alumno (YYYY-MM-DD): ")
            controlador.registrar_persona(rut, nombre, apellido, fecha_nacimiento, "alumno")

        elif opcion == '2':
            rut = input("Ingrese el Rut del docente: ")
            nombre = input("Ingrese el nombre del docente: ")
            apellido = input("Ingrese el apellido del docente: ")
            fecha_nacimiento = input("Ingrese la fecha de nacimiento del docente (YYYY-MM-DD): ")
            controlador.registrar_persona(rut, nombre, apellido, fecha_nacimiento, "docente")

        elif opcion == '3':
            siglas = input("Ingrese las siglas del curso: ")
            nombre = input("Ingrese el nombre del curso: ")
            controlador.registrar_curso(siglas, nombre)

        elif opcion == '4':
            curso_id = input("Ingrese el ID del curso: ")
            docente_rut = input("Ingrese el Rut del docente: ")
            controlador.asignar_docente(curso_id, docente_rut)

        elif opcion == '5':
            alumno_rut = input("Ingrese el Rut del alumno: ")
            curso_id = input("Ingrese el ID del curso: ")
            controlador.matricular_alumno(alumno_rut, curso_id)

        elif opcion == '6':
            controlador.listar_alumnos()

        elif opcion == '7':
            controlador.listar_docentes()

        elif opcion == '8':
            controlador.listar_cursos()

        elif opcion == '9':
            controlador.cerrar_conexion()
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
