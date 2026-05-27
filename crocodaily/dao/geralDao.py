from dao.conexao import Conexao
from model.geralModel import GeralModel

class GeralDao:

    def insert(self, geral):

        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = """
            INSERT INTO geral (descricao)
            VALUES (%s)
        """

        valores = (
            geral.getGeral(),
        )

        cursor.execute(sql, valores)

        conexao.commit()

        print("Dados inseridos com sucesso!")

        cursor.close()
        conexao.close()

    def list(self):

        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT idGeral, descricao FROM geral"
        )

        dados = cursor.fetchall()

        areaGeral = []

        for linha in dados:

            geral = GeralModel(
                linha[0],
                linha[1]
            )

            areaGeral.append(geral)

        cursor.close()
        conexao.close()

        return areaGeral