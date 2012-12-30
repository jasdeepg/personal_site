import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

#projects

@app.route('/bounce')
def bounce():
    return render_template('bounce.html')

@app.route('/image')
def image():
    return render_template('image_pixels.html')

@app.route('/holdhands')
def hold_hands():
    return render_template('hold_hands.html')

@app.route('/superconductor')
def superconductor():
    return render_template('superconductor.html')

@app.route('/boe')
def boe():
    return render_template('boe.html')

@app.route('/gravis')
def gravis():
    return render_template('gravis.html')

@app.route('/water')
def water():
    return render_template('water.html')

@app.route('/voice')
def voice():
    return render_template('voice.html')

@app.route('/duron')
def duron():
    return render_template('duron.html')

@app.route('/metoo')
def metoo():
    return render_template('metoo.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/distance.csv')
def distance():
    return render_template('distance.csv')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)