from flask import render_template, request

from model.socialModel import SocialModel

class SocialModel:
    def __init__(self):
        pass

    def mostrarDados(self):
        x = request.args.get("avaliacao")

        oSocialModel = SocialModel(x)

        return render_template("social.html", msg=oSocialModel.mostrarDados())