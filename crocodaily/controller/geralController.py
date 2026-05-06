from flask import render_template

class GeralController:

    def __init__(self):
        pass

    def mostrarDados(self):

        return render_template("geral.html")