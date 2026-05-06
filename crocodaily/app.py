from flask import Flask, render_template, request
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

app.run(debug=True)
