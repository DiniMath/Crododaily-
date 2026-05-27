from dao.conexao import Conexao
from model.agendaModel import AgendaModel

class AgendaDao:

    def insert(self, agenda):

        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = """
            INSERT INTO agenda (dataAgenda, tarefa)
            VALUES (%s, %s)
        """

        valores = (
            agenda.getDataAgenda(),
            agenda.getTarefa()
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
            "SELECT idAgenda, dataAgenda, tarefa FROM agenda"
        )

        dados = cursor.fetchall()

        areaAgenda = []

        for linha in dados:

            agenda = AgendaModel(
                linha[0],
                linha[1],
                linha[2]
            )

            areaAgenda.append(agenda)

        cursor.close()
        conexao.close()

        return areaAgenda