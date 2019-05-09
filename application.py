"""
Basis voor een te ontwikkelen Flask applicatie
Creation: may 9, 2019
(c) HAN University of Applied Science
Author: Martijn van der Bruggen

Voor deployment op Azure WebApps is het noodzakelijk het bestand
de naam application.py te geven.
"""
from flask import Flask, request, make_response, render_template

app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
def index_fun():
    param_kleur = request.form.get("kleur")
    resp = make_response(render_template('mijnTemplate.html', kleur=param_kleur))
    return resp


if __name__ == '__main__':
    app.run()
