from abc import abstractmethod
from abc import ABC
from negocio.bateria import  BateriaClasica, BateriaElectrica


class Builder(ABC):
    @abstractmethod
    def set_bombo(self, bombo):
        pass

    @abstractmethod
    def set_caja(self, caja):
        pass

    @abstractmethod
    def set_pedal(self, pedal):
        pass

    @abstractmethod
    def set_ride(self, ride):
        pass

    @abstractmethod
    def set_crash(self, crash):
        pass

    @abstractmethod
    def set_hi_hat(self, hi_hat):
        pass

    @abstractmethod
    def set_tom1(self, tom1):
        pass

    @abstractmethod
    def set_tom2(self, tom2):
        pass

    @abstractmethod
    def set_asiento(self, asiento):
        pass

    @abstractmethod
    def set_precio(self, precio):
        pass

    @abstractmethod
    def build(self):
        pass


class BateriaClasicaBuilder(Builder):
    def __init__(self):
        self.bombo = None
        self.caja = None
        self.pedal = None
        self.ride = None
        self.crash = None
        self.hi_hat = None
        self.tom1 = None
        self.tom2 = None
        self.asiento = None
        self.precio = None

    def set_bombo(self, bombo):
        self.bombo = bombo
        return self

    def set_caja(self, caja):
        self.caja = caja
        return self

    def set_pedal(self, pedal):
        self.pedal = pedal
        return self

    def set_ride(self, ride):
        self.ride = ride
        return self

    def set_crash(self, crash):
        self.crash = crash
        return self

    def set_hi_hat(self, hi_hat):
        self.hi_hat = hi_hat
        return self

    def set_tom1(self, tom1):
        self.tom1 = tom1
        return self

    def set_tom2(self, tom2):
        self.tom2 = tom2
        return self

    def set_asiento(self, asiento):
        self.asiento = asiento
        return self

    def set_precio(self, precio):
        self.precio = precio
        return self

    def build(self):
        return BateriaClasica(self.bombo, self.caja, self.pedal, self.ride, self.crash, self.hi_hat, self.tom1,
                           self.tom2, self.asiento, self.precio)


class BateriaElectricaBuilder(Builder):
    def __init__(self):
        self.bombo = None
        self.caja = None
        self.pedal = None
        self.ride = None
        self.crash = None
        self.hi_hat = None
        self.tom1 = None
        self.tom2 = None
        self.asiento = None
        self.precio = None
        self.modulo = None

    def set_bombo(self, bombo):
        self.bombo = bombo
        return self

    def set_caja(self, caja):
        self.caja = caja
        return self

    def set_pedal(self, pedal):
        self.pedal = pedal
        return self

    def set_ride(self, ride):
        self.ride = ride
        return self

    def set_crash(self, crash):
        self.crash = crash
        return self

    def set_hi_hat(self, hi_hat):
        self.hi_hat = hi_hat
        return self

    def set_tom1(self, tom1):
        self.tom1 = tom1
        return self

    def set_tom2(self, tom2):
        self.tom2 = tom2
        return self

    def set_asiento(self, asiento):
        self.asiento = asiento
        return self

    def set_precio(self, precio):
        self.precio = precio
        return self

    def set_modulo(self, modulo):
        self.modulo = modulo
        return self

    def build(self):
        return BateriaElectrica(self.bombo, self.caja, self.pedal, self.ride, self.crash, self.hi_hat, self.tom1,
                           self.tom2, self.asiento, self.precio, self.modulo)





