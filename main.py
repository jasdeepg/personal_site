import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('about.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/aboutex')
def about_ex():
    return render_template('about_ex.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/fb_test')
def fb_test():
    return render_template('fb_test.html')

@app.route('/channel')
def channel():
    return render_template('channel.html')

#projects

#2014
@app.route('/lolliandpops')
def lolliandpops():
    return render_template('target_accrual.html')


#2013
@app.route('/target')
def target():
    return render_template('target_accrual.html')

@app.route('/pov')
def pov():
    return render_template('pov.html')

@app.route('/chocolatetasting')
def chocolatetasting():
    return render_template('chocolatetasting.html')

@app.route('/chocolateis')
def chocolateis():
    return render_template('chocolateis.html')


#2012
@app.route('/bounce')
def bounce():
    return render_template('bounce.html')

@app.route('/image')
def image():
    return render_template('image_pixels.html')

@app.route('/holdhands')
def hold_hands():
    return render_template('hold_hands.html')

@app.route('/98lumens')
def lumens():
    return render_template('98lumens.html')

@app.route('/doubleyou')
def doubleyou():
    return render_template('doubleyou.html')

#2011
@app.route('/ms')
def microsoft():
    return render_template('microsoft.html')

@app.route('/msni')
def msni():
    return render_template('msni.html')

#2010
@app.route('/lenses')
def lenses():
    return render_template('lenses.html')

#2009
@app.route('/voice')
def voice():
    return render_template('voice.html')

@app.route('/duron')
def duron():
    return render_template('duron.html')

@app.route('/metoo')
def metoo():
    return render_template('metoo.html')

@app.route('/teched')
def teched():
    return render_template('teched.html')

#2008
@app.route('/gravis')
def gravis():
    return render_template('gravis.html')

@app.route('/water')
def water():
    return render_template('water.html')

@app.route('/traffic')
def traffic():
    return render_template('traffic.html')

#2007
@app.route('/boe')
def boe():
    return render_template('boe.html')

#2006

#2005
@app.route('/superconductor')
def superconductor():
    return render_template('superconductor.html')

#CSV files
@app.route('/distance.csv')
def distance():
    return render_template('distance.csv')

@app.route('/distance_ex.csv')
def distance_ex():
    return render_template('distance_ex.csv')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)