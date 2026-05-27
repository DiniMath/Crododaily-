from dao.conexao import Conexao
from model.agendaModel import AgendaModel

class AgendaDao:

    def list(self):

        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT idAgenda FROM agenda"
        )

        dados = cursor.fetchall()

        areaAgenda = []

        for linha in dados:

            agenda = AgendaModel(linha[0])

            areaAgenda.append(agenda)

        cursor.close()
        conexao.close()

        return areaAgenda