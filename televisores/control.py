class Control:
    tv = None

    def turnOn(self):
        self.tv.turnOn()

    def turnOff(self) :
        self.tv.turnOff()

    def canalUp(self):
        canalNuevo = self.tv.getCanal() + 1
        self.tv.setCanal(canalNuevo)

    def canalDown(self):
        canalNuevo = self.tv.getCanal() - 1
        self.tv.setCanal(canalNuevo)

    def volumenUp(self):
        volumenNuevo = self.tv.getVolumen() + 1
        self.tv.setVolumen(volumenNuevo)

    def volumenDown(self):
        volumenNuevo = self.tv.getVolumen() - 1
        self.tv.setVolumen(volumenNuevo)

    def setCanal(self, canal):
        self.tv.setCanal(canal)

    def enlazar(self,tv):
        self.tv = tv
        self.tv.setControl(self)

    def getTv(self):
        return self.tv

    def setTv(self, tv):
        self.tv = tv
