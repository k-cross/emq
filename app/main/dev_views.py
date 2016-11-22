from flask import render_template
from . import main


@main.route('/listUser')
def list():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from orders group by transID")
    rows = cursor.fetchall()

    return render_template("list.html", rows=rows)


