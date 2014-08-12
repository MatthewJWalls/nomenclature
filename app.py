#!/usr/bin/env python

import random
from flask import *
import names

# set up flask constants

DEBUG      = False
SECRET_KEY = "donotcare"
USERNAME   = "donotcare"
PASSWORD   = "donotcare"

# create app

app = Flask(__name__)
app.config.from_object(__name__)

minAdj = len(names.adjectives)-1
minAni = len(names.animals)-1

@app.route('/')
def index():
    try:
        return "%s%s" % (
            names.adjectives[random.randint(0, minAdj)],
            names.animals[random.randint(0, minAni)]
        )
    except:
        app.logger.debug("fuck")

if __name__ == '__main__':
    app.run(host='0.0.0.0')

