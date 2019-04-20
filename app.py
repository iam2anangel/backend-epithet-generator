#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import jsonify
from .helpers import EpithetGenerator, Vocabulary
app = Flask(__name__)

@app.route('/')
def generate_epithets():
    # d = {"epithets": []}
    result = EpithetGenerator().generate_word()
    return jsonify({"epithets": result})




@app.route('/vocabulary')
def vocabulary():
    # d = {"vocabulary": {}}
    result = Vocabulary.read_json("resources/data.json")
    return jsonify({"vocabulary": result})


@app.route("/epithets/<int:quantity>")
def generate_multiple_words():
    return jsonify({"epithets": result})