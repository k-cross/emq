import csv
from flask import Flask


def app_setup():
    app = Flask(__name__)

    # For all key/value pairs, look in the secret/keys file for edits
    with open('secret/keys.csv', 'rt') as f:
        f_csv = csv.reader(f)
        for line in f_csv:
            app.config[line[0]] = line[1]

    return app
