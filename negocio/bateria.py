from abc import ABC


class Bateria(ABC):

    def __init__(self, bombo, caja, pedal, ride, crash, hi_hat, tom1, tom2, asiento, precio):
        self.bombo = bombo
        self.caja = caja
        self.pedal = pedal
        self.ride = ride
        self.crash = crash
        self.hi_hat = hi_hat
        self.tom1 = tom1
        self.tom2 = tom2
        self.asiento = asiento
        self.precio = precio


class BateriaClasica(Bateria):
    def __init__(self, bombo, caja, pedal, ride, crash, hi_hat, tom1, tom2, asiento, precio):
        super().__init__(bombo, caja, pedal, ride, crash, hi_hat, tom1, tom2, asiento, precio)

    def __str__(self):
        return (f"Bombo: {self.bombo}, Caja: {self.caja},Pedal: {self.pedal}, Ride: {self.ride}, "
                f"Crash {self.crash}$ , Hi-Hat: {self.hi_hat}, "
                f"Tom 1 {self.tom1}, Tom 2 {self.tom2}, Asiento {self.asiento}, Precio {self.precio},")

    def get_bombo(self):
        return self.bombo

    def get_caja(self):
        return self.caja

    def get_pedal(self):
        return self.pedal

    def get_ride(self):
        return self.ride

    def get_crash(self):
        return self.crash

    def get_hi_hat(self):
        return self.hi_hat

    def get_tom1(self):
        return self.tom1

    def get_tom2(self):
        return self.tom2

    def get_asiento(self):
        return self.asiento

    def get_precio(self):
        return self.precio


class BateriaElectrica(Bateria):
    def __init__(self, bombo, caja, pedal, ride, crash, hi_hat, tom1, tom2, asiento, precio, modulo):
        super().__init__(bombo, caja, pedal, ride, crash, hi_hat, tom1, tom2, asiento, precio)
        self.modulo = modulo

    def __str__(self):
        return (f"Bombo: {self.bombo}, Caja: {self.caja},Pedal: {self.pedal}, Ride: {self.ride}, "
                f"Crash {self.crash}$ , Hi-Hat: {self.hi_hat}, "
                f"Tom 1 {self.tom1}, Tom 2 {self.tom2}, Asiento {self.asiento}, Precio {self.precio},"
                f"Modulo: {self.modulo}")

    def get_bombo(self):
        return self.bombo

    def get_caja(self):
        return self.caja

    def get_pedal(self):
        return self.pedal

    def get_ride(self):
        return self.ride

    def get_crash(self):
        return self.crash

    def get_hi_hat(self):
        return self.hi_hat

    def get_tom1(self):
        return self.tom1

    def get_tom2(self):
        return self.tom2

    def get_asiento(self):
        return self.asiento

    def get_precio(self):
        return self.precio
