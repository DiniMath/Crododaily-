class SocialModel:
    # IMPORTANTE: Ele precisa ter o 'idSocial' aqui nos parênteses!
    def __init__(self, idSocial, avaliacao):
        self.__idSocial = idSocial
        self.__avaliacao = avaliacao

    def getIdSocial(self):
        return self.__idSocial
    
    def setIdSocial(self, idSocial):
        self.__idSocial = idSocial

    def getAvaliacao(self):
        return self.__avaliacao
    
    def setAvaliacao(self, avaliacao):
        self.__avaliacao = avaliacao