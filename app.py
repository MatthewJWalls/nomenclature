#!/usr/bin/env python

import random, os
from flask import *
import names

# set up flask constants

DEBUG      = False
SECRET_KEY = "donotcare"
USERNAME   = "donotcare"
PASSWORD   = "donotcare"
INDEX_NAME = "nameindex.txt"
INDEX_SIZE = 1000

# create app

app = Flask(__name__)
app.config.from_object(__name__)

minAdj = len(names.adjectives)-1
minAni = len(names.animals)-1

index = []
pos = 0

def generateNameList():

    def generateName():
        return "%s%s" % (
            names.adjectives[random.randint(0, minAdj)],
            names.animals[random.randint(0, minAni)]
        )

    index = []

    while len(index) < INDEX_SIZE:
        name = generateName()
        if name not in index:
            index.append(name)

    if os.path.exists(INDEX_NAME):
        os.remove(INDEX_NAME)

    f = open(INDEX_NAME, "w")
    f.write("\n".join(index))
    f.close()

def loadIndex():
    global index
    f = open(INDEX_NAME, "r")
    data = f.read()
    f.close()
    index = data.split("\n")    

@app.route('/')
def index():
    global pos
    global INDEX_SIZE

    pos += 1

    if pos-1 < len(index):
        return index[pos-1]
    else:
        # names exhausted, generate new index, keep pos counter the same
        app.logger.warning("Names exhaused. From this point, duplicates are possible.")
        INDEX_SIZE = INDEX_SIZE*2
        pos = 0
        generateNameList()
        loadIndex()
        return index[pos-1]

if __name__ == '__main__':

    if os.path.exists(INDEX_NAME):
        loadIndex()
    else:
        generateNameList()

    loadIndex()

    app.run(host='0.0.0.0')

