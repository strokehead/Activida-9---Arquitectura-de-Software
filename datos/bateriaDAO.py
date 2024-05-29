import mariadb
from abc import abstractmethod
from abc import ABC


class bateriaDAO(ABC):
    @abstractmethod
    def add_bateria(self, bateria):
        pass

    @abstractmethod
    def get_all_baterias(self):
        pass

    @abstractmethod
    def delete_bateria(self, id_bateria):
        pass

    @abstractmethod
    def delete_all_baterias(self):
        pass


class bateriaClasicaDAO(bateriaDAO):

    def add_bateria(self, bateria):
        conexion = mariadb.connect(
            user = "root",
            password = "strokes2500",
            host = "127.0.0.1",
            database = "base_arquitectura")

        cur = conexion.cursor()
        try:
            cur.execute("INSERT INTO baterias (bombo, caja, pedal, ride, crash, hi_hat, tom1, tom2, asiento, precio) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (bateria.get_bombo(), bateria.get_caja(), bateria.get_pedal(), bateria.get_ride(), bateria.get_crash(), bateria.get_hi_hat(), bateria.get_tom1(), bateria.get_tom2(), bateria.get_asiento(), bateria.get_precio()))
        except mariadb.Error as e:
            print(f"Error: {e}")

        conexion.commit()

        conexion.close()

    def get_all_baterias(self):
        conexion = mariadb.connect(
            user="root",
            password="strokes2500",
            host="127.0.0.1",
            database="base_arquitectura")

        cur = conexion.cursor()
        baterias = []
        try:
            cur.execute("SELECT * FROM baterias ")
            baterias = cur.fetchall()
        except mariadb.Error as e:
            print(f"Error: {e}")

        conexion.close()

        return baterias

    def delete_bateria(self, id_bateria):
        conexion = mariadb.connect(
            user="root",
            password="strokes2500",
            host="127.0.0.1",
            database="base_arquitectura")

        cur = conexion.cursor()
        try:
            cur.execute("DELETE FROM baterias WHERE id = %s", (id_bateria,))
            print("Felicidades, compro su bateria!!!")
            print("")
            conexion.commit()
        except mariadb.Error as e:
            print(f"Error: {e}")

        conexion.close()

    def delete_all_baterias(self):
        conexion = mariadb.connect(
            user="root",
            password="strokes2500",
            host="127.0.0.1",
            database="base_arquitectura")
        
        cur = conexion.cursor()

        try:
            cur.execute("TRUNCATE TABLE baterias")
            conexion.commit()
        except mariadb.Error as e:
            print(f"Error: {e}")
        conexion.close()


