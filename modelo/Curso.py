class Curso:
    def __init__(self, Siglas, Nombre):
        self.Siglas = Siglas
        self.Nombre = Nombre


    def __str__(self):
        return f"Curso: Siglas={self.__siglas}, Nombre={self.__nombre}"
