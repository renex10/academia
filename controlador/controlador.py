# controlador/controlador.py
from database.database import Database
from modelo.Alumno import Alumno
from modelo.Curso import Curso
from modelo.Docente import Docente

class Controlador:
    def __init__(self):
        self.db = Database()

    def registrar_persona(self, Rut, Nombre, Apellido, Fecha_nacimiento, tipo_persona):
        if tipo_persona.lower() == "alumno":
            persona = Alumno(Rut, Nombre, Apellido, Fecha_nacimiento)
        elif tipo_persona.lower() == "docente":
            persona = Docente(Rut, Nombre, Apellido, Fecha_nacimiento)
        else:
            print("Tipo de persona no válido.")
            return
        
        self.db.registrar_persona(persona, tipo_persona)
        print(f"{tipo_persona.capitalize()} registrado correctamente.")

    def registrar_curso(self, Siglas, Nombre):
        curso = Curso( Siglas, Nombre)  # None para Rut si no es necesario
        self.db.registrar_curso(curso)
        print("Curso registrado correctamente.")

    def asignar_docente(self, curso_id, docente_id):
        self.db.asignar_docente(curso_id, docente_id)
        print("Docente asignado al curso correctamente.")

    def matricular_alumno(self, curso_id, alumno_id):
        self.db.matricular_alumno(alumno_id, curso_id)
        print("Alumno matriculado en el curso correctamente.")

    def listar_alumnos(self):
        alumnos = self.db.listar_alumnos()
        for alumno in alumnos:
            print(alumno)

    def listar_docentes(self):
        docentes = self.db.listar_docentes()
        for docente in docentes:
            print(docente)

    def listar_cursos(self):
        cursos = self.db.listar_cursos()
        for curso in cursos:
            print(curso)

    def cerrar_conexion(self):
        self.db.cerrar_conexion()
