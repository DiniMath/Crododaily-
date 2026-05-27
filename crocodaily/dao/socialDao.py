from dao.conexao import Conexao
from model.socialModel import SocialModel

class SocialDao:

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