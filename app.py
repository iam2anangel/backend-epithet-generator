#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import jsonify
from backend_epithet_generator.helpers import EpithetGenerator, Vocabulary
app = Flask(__name__)

@app.route('/')
def generate_epithets():
    result = EpithetGenerator().generate_word()
    d = {"epithets": result}
    return jsonify(d)

@app.route('/vocabulary')
def vocabulary():
    result = Vocabulary.read_json('resources/data.json')
    d = {"vocabulary": result}
    return jsonify(d)

@app.route('/epithets/<int:quantity>')
def generate_multiple_epithets():
    result = EpithetGenerator().generate_words(quantity)
    d = {"epithets": result}
    return jsonify(d)

@app.route('/randomize')
def generate_random():
    random_time = random.randint(1, 500)
    result = EpithetGenerator().generate_words(random_time)
    return jsonify({"epithets": result})