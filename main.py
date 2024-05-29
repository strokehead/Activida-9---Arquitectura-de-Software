from negocio.adaptador import AdaptadorPrecio
from negocio.observer import ObservadorBateriasNuevas
from presentacion.UserUI import UserUI
from negocio.tienda import TiendaBaterias

tienda = TiendaBaterias()
tiendaDAO = tienda.get_bateria_clasida_DAO()

bateria1 = tienda.get_builder_clasico().set_bombo("Pearl 16x10").set_caja("Pearl 12x4").set_pedal("Tama").set_precio(
    200).build()

tiendaDAO.add_bateria(bateria1)
tienda.añadir_computadora(bateria1)

bateria2 = tienda.get_builder_electrico().set_caja("Pearl 12x4").set_tom1("Pearl 8x5").set_tom2("10x5.5").set_hi_hat(
    "Zildjian 15''").set_precio(300).build()

tiendaDAO.add_bateria(bateria2)
tienda.añadir_computadora(bateria2)

#tienda.imprimir_baterias()

interfaz = UserUI(tienda)
interfaz.mostrarOpciones()

print()
catalogo_actualizado = tienda.get_baterias()
# Observer

cliente1 = ObservadorBateriasNuevas()
cliente2 = ObservadorBateriasNuevas()
# Agregar observadores
tienda.notificador.add_observador(cliente1)
tienda.notificador.add_observador(cliente2)

tienda.notificador.notificar_observadores(catalogo_actualizado)
