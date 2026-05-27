class AgendaModel:

    def __init__(self, idAgenda):

        self.__idAgenda = idAgenda

    def getAgenda(self):
        return(self.__idAgenda)

    def setAgenda(self, idAgenda):
        self.__idAgenda = idAgenda