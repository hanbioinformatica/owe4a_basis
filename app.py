"""
Basis voor een te ontwikkelen Flask applicatie
Creation: may 9, 2019
(c) HAN University of Applied Science
Author: Martijn van der Bruggen
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index_fun():
    return 'Dit is de routing naar de root'

if __name__ == '__main__':
    app.run()
