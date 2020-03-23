from butter_cms import ButterCMS
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config
import datetime

blog_app = Blueprint('blog', __name__, template_folder='templates/blog')

client = ButterCMS(config.BUTTERCMS_KEY)

#blog_app.jinja_env.globals.update(convert_unicode_datetime=convert_unicode_datetime)

@blog_app.route('/')

@blog_app.route('/page/<int:page>')
def home(page=1):
    response = client.posts.all({'page': 1, 'page_size': 10})
    posts = response['data'] 
    next_page = response['meta']['next_page']
    previous_page = response['meta']['previous_page']
    return render_template('blog.html', posts=posts, next_page=next_page, previous_page=previous_page, convert_unicode_datetime=convert_unicode_datetime)


@blog_app.route('/<slug>')
def show_post(slug):
    response = client.posts.get(slug)
    published_date = convert_unicode_datetime(response['data']['published'])
    try:
        post = response['data']
    except:
        # Post was not found
        abort(404)
    return render_template('post.html', post=post, published_date=published_date)

@blog_app.route('/category/<category_slug>')
def show_category(category_slug):
    response = client.categories.get(category_slug, {'include':'recent_posts'})
    try:
        category = response['data']
    except:
        # category was not found
        abort(404)
    return render_template('category.html', category=category)

# convert unicode to datetime object
def convert_unicode_datetime(date):
    formatted_date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ");
    return formatted_date;





