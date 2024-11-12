class Asiento:
    def _init_(self,color,precio,registro) :
        self.color=color
        self.precio=precio
        self.registro=registro

    def cambiarColor(self,Piel):
        if Piel=="rojo" or  Piel=="verde" or Piel=="amarillo" or Piel=="negro" or Piel=="blanco":
            self.color=Piel


class Motor:
    def _init_(self,numeroCilindros,tipo,registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro

    def cambiarRegistro (self,a):
        self.registro=a

    def asignarTipo(self,newtipo):
        if newtipo in ["gasolina","electrico"]:
            self.tipo=newtipo


class Auto:
    cantidadCreados=0
    def _init_(self,modelo,precio,asientos,marca,motor,registro) :
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro
    
    def cantidadAsientos(self):
        c=0
        for h in self.asientos:
            if type(h)==Asiento:
                c+=1
        return c
    
    def verificarIntegridad(self):
       for asiento in self.asientos:
         if asiento is None:
            continue
         if (self.registro is None) or (asiento.registro is None) or (self.motor.registro is None):
            continue
         if self.registro != asiento.registro or asiento.registro != self.motor.registro:
            return "Las piezas no son originales"
       return "Auto original"
