from flask import Flask, render_template, request, redirect, url_for
from controller.carreiraController import CarreiraController
from controller.socialController import SocialController

app = Flask(__name__)

carreiracontroler = CarreiraController()
socialcontroller = SocialController()

@app.route('/')
def inicial():
    return render_template('inicial.html')

@app.route('/carreira', methods=['GET', 'POST'])
def carreira():
    if request.method == 'POST':
        controller = CarreiraController()
        return controller.insert()
    
    return render_template('carreira.html')



@app.route('/social', methods= ['GET', 'POST'])
def social():
    if request.method == 'POST':
        controller = SocialController()
        return controller.insert()
    
    return render_template('social.html')

@app.route('/geral')
def geral():
    return render_template('geral.html')

@app.route('/agenda')
def agenda():
    return render_template('agenda.html')

app.run(debug=True)