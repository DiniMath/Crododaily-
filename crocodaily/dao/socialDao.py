from dao.conexao import Conexao
from model.socialModel import SocialModel

class SocialDao:

    def insert(self, social):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = """
            INSERT INTO social (avaliacao)
            VALUES (%s)
        """

        valores = (social.getAvaliacao(),)

        cursor.execute(sql, valores)

        conexao.commit()

        print("Dados inseridos com sucesso!")

        cursor.close()
        conexao.close()