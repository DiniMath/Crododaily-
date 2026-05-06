from flask import render_template, request

from model.carreiraModel import CarreiraModel

class CarreiraController:
    def __init__(self):
        pass

    def mostrarDados(self):
        x = request.args.get("avaliacao")

        oCarreiraModel = CarreiraModel(x)

        return render_template("carreira.html", msg=oCarreiraModel.mostrarDados())