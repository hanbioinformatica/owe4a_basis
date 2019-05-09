"""
Basis voor een te ontwikkelen Flask applicatie
Creation: may 9, 2019
(c) HAN University of Applied Science
Author: Martijn van der Bruggen

Voor deployment op Azure WebApps is het noodzakelijk het bestand
de naam application.py te geven.
"""
import mysql.connector
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index_fun():
    return 'Dit is de routing naar de root'


"""
Mogelijkheid om te zoeken naar een woord in de ensembl database
Parameteroverdracht middels de get methode (default)
"""


@app.route("/sql")
def sqldemo():
    woord = request.args.get('woord')
    if woord == None: woord = "koe"
    verbinding = mysql.connector.connect(host="ensembldb.ensembl.org",
                                         user="anonymous",
                                         db="homo_sapiens_core_95_38")
    cursor = verbinding.cursor()
    cursor.execute("select * from gene where description like '%{}%' limit 10".format(woord))
    regel = ""
    tekst = """<form method="get">
                <input type="text" name="woord">
                <input type="submit" value="Submit">
                </form>
                <hr>"""
    while regel != None:
        if len(regel) > 9:
            tekst += str(regel[9]).replace(woord, "<b>" + woord + "</b>") + "<br>"
        regel = cursor.fetchone()
    cursor.close()
    verbinding.close()
    return tekst


if __name__ == '__main__':
    app.run()
