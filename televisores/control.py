class Control:
    _tv = None

    def turnOn(self):
        self._tv.turnOn()

    def turnOff(self) :
        self._tv.turnOff()

    def canalUp(self):
        canalNuevo = self._tv.getCanal() + 1
        self._tv.setCanal(canalNuevo)

    def canalDown(self):
        canalNuevo = self._tv.getCanal() - 1
        self._tv.setCanal(canalNuevo)

    def volumenUp(self):
        volumenNuevo = self._tv.getVolumen() + 1
        self._tv.setVolumen(volumenNuevo)

    def volumenDown(self):
        volumenNuevo = self._tv.getVolumen() - 1
        self._tv.setVolumen(volumenNuevo)

    def setCanal(self, canal):
        self._tv.setCanal(canal)

    def enlazar(self,tv):
        self._tv = tv
        self._tv.setControl(self)

    def getTv(self):
        return self._tv

    def setTv(self, tv):
        self._tv = tv
