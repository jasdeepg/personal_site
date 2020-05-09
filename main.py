import os
from flask import Flask, render_template
from blog.blog_blueprint import blog_app
from projects.projects_blueprint import projects_app
import config

app = Flask(__name__)

app.register_blueprint(blog_app, url_prefix='/blog')
app.register_blueprint(projects_app, url_prefix='/projects')

@app.route('/')
def main():
    return render_template('about.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/aboutex')
def about_ex():
    return render_template('about_ex.html')

@app.route('/fb_test')
def fb_test():
    return render_template('fb_test.html')

@app.route('/channel')
def channel():
    return render_template('channel.html')

#CSV files
@app.route('/distance.csv')
def distance():
    return render_template('distance.csv')

@app.route('/distance_ex.csv')
def distance_ex():
    return render_template('distance_ex.csv')

# projects that could not be built in CMS - below are direct routes
@app.route('/bounce')
def bounce():
    return render_template('bounce.html')

@app.route('/image')
def image():
    return render_template('image_pixels.html')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)