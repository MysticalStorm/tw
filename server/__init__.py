from flask import Flask, render_template
from flask_assets import Bundle, Environment
from flaskext.markdown import Markdown
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config.from_object('config')

bcrypt = Bcrypt(app)

# Assets
assets = Environment(app)
assets.url = '/static'
assets.directory = app.config['ASSETS_DEST']

less = Bundle('less/style.less', filters='less', output='gen/style.css')
assets.register('all-css', less)


# Database
db = SQLAlchemy(app)
import models


# Markdown
Markdown(app, safe_mode='escape')

# Debug toolbar
if app.config['DEBUG']:
    from flask_debugtoolbar import DebugToolbarExtension as DTE
    toolbar = DTE(app)


# Endpoints
@app.route('/')
def index():
    return render_template('index.html', User=models.User)

from server.auth.views import auth_blueprint
app.register_blueprint(auth_blueprint)
