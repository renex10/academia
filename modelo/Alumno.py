class Alumno:
    def __init__(self, Rut, Nombre, Apellido, Fecha_nacimiento):
        self.Rut = Rut
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Fecha_nacimiento = Fecha_nacimiento

    def __str__(self):
        return f"Alumno: Rut={self.Rut}, Nombre={self.Nombre}, Apellido={self.Apellido}, Fecha_nacimiento={self.Fecha_nacimiento}"



   