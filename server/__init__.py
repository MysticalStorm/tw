from flask import Flask, render_template
from flask_assets import Bundle, Environment

app = Flask(__name__)
app.config.from_object('config')

# Assets
assets = Environment(app)
assets.url = '/static'
assets.directory = app.config['ASSETS_DEST']

less = Bundle('less/style.less', filters='less', output='gen/style.css')
assets.register('all-css', less)

# Endpoints
@app.route('/')
def index():
    return render_template('index.html')

from server.tw.views import bp
app.register_blueprint(bp)
