from negocio.builder import BateriaElectricaBuilder
from negocio.builder import BateriaClasicaBuilder
from negocio.observer import NotificadorTienda
from datos.bateriaDAO import bateriaClasicaDAO


class TiendaBaterias:
    def __init__(self):
        self.builder_electrico = BateriaElectricaBuilder()
        self.builder_clasico = BateriaClasicaBuilder()
        self.notificador = NotificadorTienda()
        self.baterias = []
        self.bateriaClasidaDAO = bateriaClasicaDAO()

    def añadir_computadora(self, bateria):
        self.baterias.append(bateria)
        self.notificador.notificar_observadores(self.baterias)

    def __str__(self):
        return f"Baterias: {self.baterias}"

    def get_builder_clasico(self):
        return self.builder_clasico

    def get_builder_electrico(self):
        return self.builder_electrico

    def get_baterias(self):
        return self.baterias

    def get_bateria(self, posicion):
        return self.baterias[posicion]

    def get_bateria_clasida_DAO(self):
        return self.bateriaClasidaDAO

    def imprimir_baterias(self):
        for bateria in self.baterias:
            print(bateria)