# database/database.py
import sqlite3

class Database:
    def __init__(self, db_name='academia.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.crear_tablas()

    def crear_tablas(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS personas (
                Rut TEXT PRIMARY KEY,
                Nombre TEXT NOT NULL,
                Apellido TEXT NOT NULL,
                Fecha_nacimiento TEXT NOT NULL,
                Tipo TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS cursos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Siglas TEXT NOT NULL,
                Nombre TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS docentes_cursos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Docente_rut TEXT,
                Curso_id INTEGER,
                FOREIGN KEY(Docente_rut) REFERENCES personas(Rut),
                FOREIGN KEY(Curso_id) REFERENCES cursos(id)
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS matriculas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Alumno_rut TEXT,
                Curso_id INTEGER,
                FOREIGN KEY(Alumno_rut) REFERENCES personas(Rut),
                FOREIGN KEY(Curso_id) REFERENCES cursos(id)
            )
        ''')
        self.connection.commit()

    def registrar_persona(self, persona, tipo_persona):
        self.cursor.execute("INSERT INTO personas (Rut, Nombre, Apellido, Fecha_nacimiento, Tipo) VALUES (?, ?, ?, ?, ?)", (persona.Rut, persona.Nombre, persona.Apellido, persona.Fecha_nacimiento, tipo_persona))
        self.connection.commit()

    def registrar_curso(self, curso):
        self.cursor.execute("INSERT INTO cursos (Siglas, Nombre) VALUES (?, ?)", (curso.Siglas, curso.Nombre))
        self.connection.commit()

    def asignar_docente(self, curso_id, docente_id):
        self.cursor.execute("INSERT INTO docentes_cursos (Docente_rut, Curso_id) VALUES (?, ?)", (docente_id, curso_id))
        self.connection.commit()

    def matricular_alumno(self, alumno_id, curso_id):
        self.cursor.execute("INSERT INTO matriculas (Alumno_rut, Curso_id) VALUES (?, ?)", (alumno_id, curso_id))
        self.connection.commit()

    def listar_alumnos(self):
        self.cursor.execute("SELECT * FROM personas WHERE Tipo = 'alumno'")
        return self.cursor.fetchall()

    def listar_docentes(self):
        self.cursor.execute("SELECT * FROM personas WHERE Tipo = 'docente'")
        return self.cursor.fetchall()

    def listar_cursos(self):
        self.cursor.execute("SELECT * FROM cursos")
        return self.cursor.fetchall()

    def cerrar_conexion(self):
        self.connection.close()