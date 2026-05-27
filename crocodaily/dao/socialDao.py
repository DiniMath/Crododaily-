from dao.conexao import Conexao
from model.socialModel import SocialModel

class SocialDao:

<<<<<<< HEAD
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
=======
    def list(self):

        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT idSocial FROM social"
        )

        dados = cursor.fetchall()

        areaSocial = []

        for linha in dados:

            social = SocialModel(linha[0])

            areaSocial.append(social)

        cursor.close()
        conexao.close()

        return areaSocial
>>>>>>> dfd0a84cfaa4e2e8577e5fda6766e64fde59d0e7
