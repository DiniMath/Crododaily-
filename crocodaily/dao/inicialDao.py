from dao.conexao import Conexao
from model.inicialModel import InicialModel

class InicialDao:

    def insert(self, inicial):

        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = """
            INSERT INTO inicial (descricao)
            VALUES (%s)
        """

        valores = (
            inicial.getInicial(),
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
            "SELECT idInicial, descricao FROM inicial"
        )

        dados = cursor.fetchall()

        areaInicial = []

        for linha in dados:

            inicial = InicialModel(
                linha[0],
                linha[1]
            )

            areaInicial.append(inicial)

        cursor.close()
        conexao.close()

        return areaInicial