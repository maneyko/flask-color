# coding: utf-8
"""
    flaskext.colors
    ~~~~~~~~~~~~~~
    Provides colorful output in debugging mode.
"""

import re
from time import strftime
import werkzeug.serving

def color(n, text):
    'If terminal supports 256 colors `n` may be a number'
    colors = {'RED': 1, 'GREEN': 2, 'YELLOW': 3, 'BLUE': 4,
              'PURPLE': 5, 'CYAN': 6, 'WHITE': 7, 'GRAY': 8}
    if type(n) is str and n in colors.keys():
        n = colors[n]
    return '{esc}[38;5;{:d}m{}{esc}[0m'.format(n, text, esc='\033')

def init_app(app):
    if not (
        app.config['DEBUG'] or
        app.config.get('COLOR_ALWAYS_ON')
    ):
        return

    static_pat = app.config.get(
        'COLOR_PATTERN_GRAY',
        r'^/(static|assets|img|js|css)/(.*)'
        + r'|favicon\.ico'
        + r'|(.*)\.(png|jpeg|jpg|gif|css)$'
    )
    hide_pat = app.config.get('COLOR_PATTERN_HIDE', r'/^$/')

    def log_request(self, code='-', size='-'):
        method, url, procotol = self.requestline.split()[:3]

        if re.search(hide_pat, url):
            return

        def status_text(code):
            if type(code) is not int or code // 100 not in [2, 3, 4, 5]:
                return color('GRAY', code)
            hcode = code // 100
            if hcode == 2:
                return color('GREEN', code)
            elif hcode == 3:
                return color('CYAN', code)
            elif hcode in [4, 5]:
                return color('RED', code)

        def method_text(method):
            if method == 'GET':
                return color('PURPLE', method)
            elif method == 'POST':
                return color('YELLOW', method)
            else:
                return color('WHITE', method)

        print('{date} {status} {method} {procotol} {url}'.format(
            date     = color('GRAY', strftime('%H.%M.%S')),
            status   = status_text(code),
            method   = method_text(method),
            procotol = color('GRAY', procotol),
            url      = color('GRAY', url) if re.search(static_pat, url)
                        else color('WHITE', url)
        ))
    werkzeug.serving.WSGIRequestHandler.log_request = log_request
