from flask import render_template, request

class InicialController:

    def __init__(self):
        pass

    def mostrarDados(self):

        return render_template("inicial.html")