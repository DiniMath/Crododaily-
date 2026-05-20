from dao.conexao import Conexao
from model.carreiraModel import CarreiraModel

class CarreiraDao:
    def list(self):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT idCarreira, avaliacao FROM carreira"
        )
        dados = cursor.fetchall()
        areacarreira = []
        for linha in dados:
            carreira = CarreiraModel(linha[0], linha[1])
            areacarreira.append(carreira)
        cursor.close()
        conexao.close()
        return areacarreira
