import mysql.connector

class Conexao:

    @staticmethod
    def conectar():
        return mysql.connector.connect(
            host= "loacalhost",
            user = "root",
            password = "ifsp",
            database = "crocodaily"
        )