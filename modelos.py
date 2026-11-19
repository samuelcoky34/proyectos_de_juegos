from abc import ABC, abstractmethod

class Jugador(ABC):
    def __init__(self, nombre: str, nacionalidad: str, edad: int, grl: int):
        if not nombre.strip() or not nacionalidad.strip():
            raise ValueError("El nombre y la nacionalidad no pueden estar vacíos")
        if not (1 <= grl <= 99):
            raise ValueError("El GRL debe estar entre 1 al 99")
        if not (16 <= edad <= 45):
            raise ValueError("El jugador debe tener la edad entre 16 al 45")

        self.nombre = nombre.strip()
        self.nacionalidad = nacionalidad.strip()
        self.edad = edad
        self.__grl = grl

    def obtener_grl(self):
        return self.__grl

    def actualizar_grl(self, nuevo_grl: int):
        if not (1 <= nuevo_grl <= 99):
            raise ValueError("El GRL debe estar entre 1 al 99")
        self.__grl = nuevo_grl

    @abstractmethod
    def jugar_partido(self):
        pass

class Delantero(Jugador):
    def __init__(self, nombre: str, nacionalidad: str, edad: int, grl: int):
        super().__init__(nombre, nacionalidad, edad, grl)
        self.goles = 0

    def jugar_partido(self):
        self.goles += 1
        print(f"⚽ {self.nombre} (DEL - GRL{self.obtener_grl()}) anotó un gol. Goles totales: {self.goles}")

class Mediocampista(Jugador):
    def __init__(self, nombre: str, nacionalidad: str, edad: int, grl: int):
        super().__init__(nombre, nacionalidad, edad, grl)
        self.asistencias = 0

    def jugar_partido(self):
        self.asistencias += 1
        print(f"⚽ {self.nombre} (MC - GRL{self.obtener_grl()}) asistio un gol. Asistencias totales: {self.asistencias}")

class Defensor(Jugador):
    def __init__(self, nombre: str, nacionalidad: str, edad: int, grl: int):
        super().__init__(nombre, nacionalidad, edad, grl)
        self.quites = 0

    def jugar_partido(self):
        self.quites += 1
        print(f"⚽ {self.nombre} (DFC - GRL{self.obtener_grl()}) ha defendido un gol. Quites totales: {self.quites}")

class Arquero(Jugador):
    def __init__(self, nombre: str, nacionalidad: str, edad: int, grl: int):
        super().__init__(nombre, nacionalidad, edad, grl)
        self.atajadas = 0

    def jugar_partido(self):
        self.atajadas += 1
        print(f"⚽ {self.nombre} (POR - GRL{self.obtener_grl()}) ha atajado un gol. Atajadas totales: {self.atajadas}")

if __name__ == "__main__":
    equipo_prueba = [
        Delantero("Lamine Yamal", "España", 19, 89),
        Mediocampista("Pedri", "España", 23, 90),
        Defensor("Cubarsi", "España", 19, 86),
        Arquero("Courtois", "Belgica", 34, 90)
    ]
    for jugador in equipo_prueba:
        jugador.jugar_partido()