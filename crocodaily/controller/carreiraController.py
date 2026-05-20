from flask import render_template, request

from model.carreiraModel import CarreiraModel

from dao.carreiraDao import CarreiraDao

class CarreiraController:
    def __init__(self):
        self.carreiraDao = CarreiraDao()


    def list(self):
        areacarreira = self.carreiraDao.list()
        return render_template(
            "carreira.html",
            areacarreira=areacarreira
        )

      
