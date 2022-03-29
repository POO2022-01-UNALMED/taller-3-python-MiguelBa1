class TV:
    _numTV = 0
    def __init__(self, marca, estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self._control = None
        TV._numTV += 1

    def getMarca(self):
        return self._marca

    def setMarca(self, marca):
        self._marca = marca
    

    def getControl(self):
        return self._control
    

    def setControl(self, control):
        self._control = control
    

    def getPrecio(self):
        return self._precio
    

    def setPrecio(self, precio):
        self._precio = precio
    

    def getVolumen(self):
        return self._volumen
    

    def setVolumen(self, volumen):
        if (not self._estado): return
        if (volumen < 0 or volumen > 7):
            return
        self._volumen = volumen
    

    def getCanal(self):
        return self._canal
    

    def setCanal(self, canal):
        if (not self._estado):return
        if (canal < 1 or canal > 120):
            return
        self._canal = canal
    
    
    @classmethod
    def getNumTV(self):
        return TV._numTV

    @classmethod
    def setNumTV(cls, numTV):
        TV._numTV = numTV
    
    def turnOn(self):
        self._estado = True
    
    def turnOff(self):
        self._estado = False
    
    def getEstado(self):
        return self._estado

    def canalUp(self):
        canalNuevo = self._canal + 1
        self.setCanal(canalNuevo)
    
    def canalDown(self):
        canalNuevo = self._canal - 1
        self.setCanal(canalNuevo)
    
    def volumenUp(self):
        volumenNuevo = self._volumen + 1
        self.setVolumen(volumenNuevo)

    def volumenDown(self):
        volumenNuevo = self._volumen - 1
        self.setVolumen(volumenNuevo)
