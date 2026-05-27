from flask import render_template, request, redirect, url_for

from model.socialModel import SocialModel

from dao.socialDao import SocialDao

class SocialController:
    def __init__(self):
        self.socialDao = SocialDao()


    def insert(self):
        avaliacao = request.form['avaliacao']
        social = SocialModel(
            None,
            avaliacao
        )
        self.socialDao.insert(social)

        return redirect(url_for('social'))

      
