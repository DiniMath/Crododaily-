from flask import render_template

class AgendaController:

    def __init__(self):
        pass

    def mostrarDados(self):

        return render_template("agenda.html")