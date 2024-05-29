class NotificadorTienda:
    def __init__(self):
        self.__observadores = []

    def add_observador(self, observador):
        self.__observadores.append(observador)

    def remove_observador(self, observador):
        self.__observadores.remove(observador)

    def notificar_observadores(self, baterias):
        for observer in self.__observadores:
            observer.update(baterias)


# Observer Pattern
class ObservadorBateriasNuevas:

    def __init__(self):
        self.catalogo_baterias = []

    def update(self, baterias):
        self.catalogo_baterias = baterias
        self.mostrar()

    def mostrar(self):
        print("Se agrego un nuevo modelo de bateria en nuestro catalogo: ", self.catalogo_baterias[-1])

    def mostrar_catalogo(self):
        print("Catalogo de cliente:")
        for bateria in self.catalogo_baterias:
            print(bateria)