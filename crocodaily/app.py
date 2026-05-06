from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicial():
    return render_template('inicial.html')

@app.route('/carreira')
def carreira():
    return render_template('carreira.html')

@app.route('/social')
def social():
    return render_template('social.html')

@app.route('/geral')
def geral():
    return render_template('geral.html')

@app.route('/agenda')
def agenda():
    return render_template('agenda.html')

app.run(debug=True)