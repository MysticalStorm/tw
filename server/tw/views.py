
import os
import time
import cookielib
import json
import urllib
import urllib2
from ghost import Ghost
from flask import Blueprint, render_template, url_for
from tw import login, password

bp = Blueprint('tw', __name__)

@bp.route('/')
def index():
    ts = time.time()
    return render_template('index.html', time=ts)

@bp.route('/try')
def hello_world():
    ghost = Ghost(log_level=40)

    cookie_jar = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))

    with ghost.start(download_images=False) as session:
        page, extra_resources = session.open("https://www.the-west.ru/")

        url = 'https://www.the-west.ru/index.php?ajax=check_login'
        values = {'name': login, 'password': password}
        data = urllib.urlencode(values)
        response = opener.open(url, data)
        data = json.load(response)
        print data
        for cookie in cookie_jar:
            print cookie.name, cookie.value

        session.show()
        url = 'https://www.the-west.ru/?action=login'
        values = 'world_id=16&player_id=' + str(data['player_id']) + '&password=' + str(
            data['password']) + '&set_cookie=0';
        page, extra_resources = session.open(url, method='post', body=values)

        cookies = ''
        for cookie in session.cookies:
            cookies += cookie.name() + '=' + cookie.value() + ';'
        opener.addheaders.append(('Cookie', cookies))

        for header in opener.addheaders:
            print header

        playerh, extra_resources = session.evaluate('Player.h')

        # https://ru16.the-west.ru/game.php?window=task&action=add&h=f5a032

        print 'Player H'
        print playerh

        url = 'https://ru16.the-west.ru/game.php?window=task&action=add&h=' + str(playerh)
        value = {'tasks[0][jobId]': '130', 'tasks[0][x]': '44169', 'tasks[0][y]': '17887', 'tasks[0][duration]': '15',
                 'tasks[0][taskType]': 'job'}
        data = urllib.urlencode(value)
        response = opener.open(url, data)

        page, extra_resources = session.open(url, method='post', body=data)
        print page
        print extra_resources

        # response = urllib2.urlopen(req)
        # data = json.load(response)
        # print data
        for cookie in cookie_jar:
            print cookie.name, cookie.value

        session.capture_to('new1.png')
    return 'Hello World!'