from negocio.bateria import Bateria


class AdaptadorPrecio(Bateria):
    def __init__(self, bateria):
        self.bateria = bateria

    def get_precio(self):
        dolares = self.bateria.get_precio()
        tasa_cambio = 6.96
        bolivianos = self.dolares_a_bolivianos(dolares, tasa_cambio)
        return bolivianos

    def dolares_a_bolivianos(self, dolares, tasa_cambio):
        bolivianos = dolares * tasa_cambio
        return bolivianos
