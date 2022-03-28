class TV:
    numTV = 0
    def __init__(self, marca, estado):
        self.marca = marca
        self.canal = 1
        self.precio = 500
        self.estado = estado
        self.volumen = 1
        self.control = None
        TV.numTV += 1

    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca
    

    def getControl(self):
        return self.control
    

    def setControl(self, control):
        self.control = control
    

    def getPrecio(self):
        return self.precio
    

    def setPrecio(self, precio):
        self.precio = precio
    

    def getVolumen(self):
        return self.volumen
    

    def setVolumen(self, volumen):
        if (not self.estado): return
        if (volumen < 0 or volumen > 7):
            return
        self.volumen = volumen
    

    def getCanal(self):
        return self.canal
    

    def setCanal(self, canal):
        if (not self.estado):return
        if (canal < 1 or canal > 120):
            return
        self.canal = canal
    
    
    @classmethod
    def getNumTV(self):
        return TV.numTV

    @classmethod
    def setNumTV(cls, numTV):
        TV.numTV = numTV
    
    def turnOn(self):
        self.estado = True
    
    def turnOff(self):
        self.estado = False
    
    def getEstado(self):
        return self.estado

    def canalUp(self):
        canalNuevo = self.canal + 1
        self.setCanal(canalNuevo)
    
    def canalDown(self):
        canalNuevo = self.canal - 1
        self.setCanal(canalNuevo)
    
    def volumenUp(self):
        volumenNuevo = self.volumen + 1
        self.setVolumen(volumenNuevo)

    def volumenDown(self):
        volumenNuevo = self.volumen - 1
        self.setVolumen(volumenNuevo)
