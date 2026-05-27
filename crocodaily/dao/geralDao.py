from dao.conexao import Conexao
from model.geralModel import GeralModel

class GeralDao:

    def list(self):

        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT idGeral FROM geral"
        )

        dados = cursor.fetchall()

        areaGeral = []

        for linha in dados:

            geral = GeralModel(linha[0])

            areaGeral.append(geral)

        cursor.close()
        conexao.close()

        return areaGeral