import cookielib
import json
import urllib
import urllib2
import os
from ghost import Ghost
from pathlib import Path


class BOT:
    ghost = Ghost(log_level=40)
    cookie_jar = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.121 Safari/535.2'

    def start(self, login, password):
        print 'ENTER'

        with self.ghost.start(download_images=False, user_agent = user_agent) as session:
            page, extra_resources = session.open("https://www.the-west.ru/")
            print 'ENTER TO WEST'

            url = 'https://www.the-west.ru/index.php?ajax=check_login'
            values = {'name': login, 'password': password}
            data = urllib.urlencode(values)
            response = self.opener.open(url, data)
            data = json.load(response)
            print data
            for cookie in self.cookie_jar:
                print cookie.name, cookie.value

            # session.show()
            url = 'https://www.the-west.ru/?action=login'
            values = 'world_id=16&player_id=' + str(data['player_id']) + '&password=' + str(
                data['password']) + '&set_cookie=0';
            page, extra_resources = session.open(url, method='post', body=values)

            cookies='User-Agent=' + user_agent +  ';'
            for cookie in session.cookies:
                cookies += cookie.name() + '=' + cookie.value() + ';'
            self.opener.addheaders.append(('Cookie', cookies))

            for header in self.opener.addheaders:
                print header

            playerh, extra_resources = session.evaluate('Player.h')

            # https://ru16.the-west.ru/game.php?window=task&action=add&h=f5a032

            print 'Player H'
            print playerh

            url = 'https://ru16.the-west.ru/game.php?window=task&action=add&h=' + str(playerh)
            value = {'tasks[0][jobId]': '130', 'tasks[0][x]': '44169', 'tasks[0][y]': '17887',
                     'tasks[0][duration]': '15',
                     'tasks[0][taskType]': 'job'}
            data = urllib.urlencode(value)
            response = self.opener.open(url, data)

            #page, extra_resources = session.open(url, method='post', body=data)
            #print page
            #print extra_resources

            # response = urllib2.urlopen(req)
            # data = json.load(response)
            # print data
            for cookie in self.cookie_jar:
                print cookie.name, cookie.value

            from server import app
            logo_path=os.path.join(app.root_path, 'static/logo.png')
            my_file = Path(logo_path)
            if my_file.is_file():
                os.remove(logo_path)
            session.capture_to(logo_path)
