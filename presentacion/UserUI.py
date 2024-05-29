from negocio.adaptador import AdaptadorPrecio


class UserUI:
    def __init__(self, tienda):
        self.tienda = tienda
        self.tiendaDAO = self.tienda.get_bateria_clasida_DAO()

    def mostrarOpciones(self):

        print("Bienvenido a 'Toca o muere'")

        while True:

            print("Puede escoger una de nuestras opciones:")
            print("Catalogo")
            print("Comprar")
            print("Precio")
            print("Salir")

            respuesta = input("")

            if respuesta == "Catalogo":
                print(self.tiendaDAO.get_all_baterias())

            if respuesta == "Comprar":
                id_bateria = input("Ingrese el numero de la bateria: ")
                self.tiendaDAO.delete_bateria(id_bateria)

            if respuesta == "Precio":
                id_bateria = input("Ingrese el numero de la bateria: ")
                adaptador = AdaptadorPrecio(self.tienda.get_bateria(int(id_bateria)-1))
                print(f"Precio en bolivianos de bateria {id_bateria}: {adaptador.get_precio()} ")
                print()

            if respuesta == "Salir":
                self.tiendaDAO.delete_all_baterias()
                print("Hasta luego, vuelva pronto!!!")
                break



