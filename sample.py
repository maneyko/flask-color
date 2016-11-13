#!/usr/bin/env python

from flask import Flask, jsonify, request, redirect
import flask_color

app = Flask(__name__)
app.config['DEBUG'] = True
flask_color.init_app(app)
names = {'John': 'Smith',
         'Marry': 'Peterson'}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first = request.form['first']
        last = request.form['last']
        names[first] = last
        return redirect('/names', code=302)
    else:
        return """
            <html style="padding-left: 2%;">
                <br>
                <a href="/names">All Names</a>
                <br><br>
                <form method="POST">
                    <input type="text" name="first" placeholder="First Name"/>
                    <input type="text" name="last" placeholder="Last Name"/>
                    <input type="submit">
                </form>
            </html>
            """

@app.route('/names')
def data():
    return jsonify(names)

if __name__ == '__main__':
    app.run()
