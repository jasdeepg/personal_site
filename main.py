import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/bounce')
def bounce():
    return render_template('bounce.html')

@app.route('/image')
def image():
    return render_template('image_pixels.html')

@app.route('/holdhands')
def hold_hands():
    return render_template('hold_hands.html')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)