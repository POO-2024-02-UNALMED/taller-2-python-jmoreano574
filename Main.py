class Asiento():
    colores: list[str] = ["rojo", "verde", "amarillo", "negro", "blanco"]

    def __init__(self, color: str, precio: int, registro: int) -> None:
        self.color: str = color
        self.precio: int = precio
        self.registro: int = registro

    def cambiarColor(self, color: str) -> None:
        if color in Asiento.colores:
            self.color: str = color

class Motor():
    tiposPosibles: list[str] = ["electrico", "gasolina"]

    def __init__(self, numeroCilindros: int, tipo: str, registro: int) -> None:
        self.numeroCilindros: int = numeroCilindros
        self.tipo: str = tipo
        self.registro: int = registro

    def cambiarRegistro(self, registro: int) -> None:
        self.registro: int = registro

    def asignarTipo(self, tipo: str) -> None:
    if tipo in Motor.tiposPosibles:
        self.tipo: str = tipo

class Auto():
    cantidadCreados: int = 0
    def __init__(self, modelo: str, precio: int, asientos: list[Asiento], marca: str, motor: Motor, registro: int) -> None:
        self.modelo: str = modelo
        self.precio: int = precio
        self.asientos: list[Asiento] = asientos
        self.marca: str = marca
        self.motor: Motor = motor
        self.registro: int = registro

    def cantidadAsientos(self) -> int:
        contador = 0
        for i in self.asientos:
            if isinstance(i, Asiento):
                contador += 1
        return contador
        
    def verificarIntegridad(self) -> str:
    for asiento in self.asientos:
        if isinstance(asiento, Asiento):
            if asiento.registro != self.motor.registro:
                return "Las piezas no son originales"
            elif asiento.registro != self.registro:
                return "Las piezas no son originales"
            elif self.registro != self.motor.registro:
                return "Las piezas no son originales"
    return "Auto original"







