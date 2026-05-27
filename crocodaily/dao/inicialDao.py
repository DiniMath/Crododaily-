from dao.conexao import Conexao
from model.inicialModel import InicialModel

class InicialDao:

    def list(self):

        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT idInicial FROM inicial"
        )

        dados = cursor.fetchall()

        areaInicial = []

        for linha in dados:

            inicial = InicialModel(linha[0])

            areaInicial.append(inicial)

        cursor.close()
        conexao.close()

        return areaInicial