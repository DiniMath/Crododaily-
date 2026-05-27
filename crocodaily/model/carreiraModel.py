class CarreiraModel:
    def __init__(self, idCarreira, avaliacao):
        
        self.__idCarreira = idCarreira
        self.__avaliacao = avaliacao

  
    def getIdCarreira(self):
        return self.__idCarreira
    
    def setIdCarreira(self, idCarreira):
        self.__idCarreira = idCarreira

    
    def getAvaliacao(self):
        return self.__avaliacao
    
    def setAvaliacao(self, avaliacao):
        self.__avaliacao = avaliacao