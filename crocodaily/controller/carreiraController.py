from flask import render_template, request, redirect, url_for

from model.carreiraModel import CarreiraModel

from dao.carreiraDao import CarreiraDao

class CarreiraController:
    def __init__(self):
        self.carreiraDao = CarreiraDao()


    def insert(self):
        avaliacao = request.form['avaliacao']
        carreira = CarreiraModel(
            None,
            avaliacao
        )
        self.carreiraDao.insert(carreira)

        return redirect(url_for('carreira'))

      
