# -*- coding: utf-8 -*-

"""
    flaskext.colors
    ~~~~~~~~~~~~~~

    Provides colorful output in debugging mode.
    Meant to resemble lite-server from npm.

"""

import time
import re

RED    = 1
GREEN  = 2
YELLOW = 3
BLUE   = 4
PURPLE = 5
CYAN   = 6
WHITE  = 7
GRAY   = 8

def ctext(text, number):
    """Supports 256 colors if enabled in terminal."""
    return '\033[38;5;{number}m{text}\033[0m'.format(
            number=str(number), text=text
            )

def init_app(app):
    if not (
        app.config['DEBUG'] or
        app.config.get('COLOR_ALWAYS_ON', False)
    ):
        return
    import werkzeug.serving

    staticPattern = app.config.get(
        'COLOR_PATTERN_GRAY',
        r'^/(static|assets|img|js|css)/(.*)|favicon\.ico|(.*)\.(png|jpeg|jpg|gif|css)$'
    )
    hidePattern = app.config.get('COLOR_PATTERN_HIDE', r'/^$/')
    WSGIRequestHandler = werkzeug.serving.WSGIRequestHandler

    def log_request(self, code='-', size='-'):
        url = self.requestline.split(" ")[1]
        method = self.requestline.split(" ")[0]

        if re.search(hidePattern, url):
            return

        if code == 200:
            statusColor = GREEN
        elif code/100 in [3]:
            statusColor = CYAN
        elif code/100 in [4, 5]:
            statusColor = RED
        else:
            statusColor = GRAY

        if method == 'GET':
            methodColor = PURPLE
        elif method == 'POST':
            methodColor = YELLOW
        else:
            methodColor = WHITE

        print("{date} {status} {method} {url}".format(
            date   = ctext(time.strftime("%y.%m.%d %H.%M.%S"), GRAY),
            status = ctext(code, statusColor),
            method = ctext(method, methodColor),
            url    = ctext(url, GRAY)
        ))

    WSGIRequestHandler.log_request = log_request
    werkzeug.serving.WSGIRequestHandler = WSGIRequestHandler
