from butter_cms import ButterCMS
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config
import datetime

projects_app = Blueprint('projects', __name__, template_folder='templates/projects', static_folder='../static')

client = ButterCMS(config.BUTTERCMS_KEY)

#blog_app.jinja_env.globals.update(convert_unicode_datetime=convert_unicode_datetime)

@projects_app.route('/')

@projects_app.route('/page/<int:page>')
def home(page=1):
    response = client.content_fields.get(['projects'])
    projects = response['data']['projects']
    return render_template('projects.html', projects=projects, convert_unicode_datetime=convert_unicode_datetime)


@projects_app.route('/<slug>')
def show_post(slug):
    response = client.content_fields.get(['projects'], {'fields.slug':slug})
    date_start = convert_unicode_datetime(response['data']['projects'][0]['date_start'])
    date_end = convert_unicode_datetime(response['data']['projects'][0]['date_end'])
    try:
        project = response['data']['projects'][0]
    except:
        # Post was not found
        abort(404)
    return render_template('project.html', project=project, date_start=date_start, date_end=date_end)

# convert unicode to datetime object
def convert_unicode_datetime(date):
    formatted_date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S");
    return formatted_date;