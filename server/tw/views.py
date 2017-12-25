from flask import Blueprint, render_template, request
from server import bot

bp = Blueprint('tw', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@bp.route('/try', methods=['GET', 'POST'])
def west_run():

    login = request.args.get('login', type=str)
    password = request.args.get('password', type=str)

    print 'BEFORE'
    bot.start(login, password)
    print 'AFTER'

    return render_template('tw/index.html')