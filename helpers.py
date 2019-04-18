#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import random

@app.route('/vocabulary')
class Vocabulary:
    """
    Handle loading in a JSON file with proper unfinished swears in it!

    Usage:
        data = Vocabulary.read_json("/path/to/data.json")
    """

    def read_json(path, mode='r'):
        with open(path, mode=mode) as handle:
            return json.load(handle)



@app.route('/')
class EpithetGenerator:
    """select one random word from each column of the list and generate a 
       quantity of epithets from a vocabulary file loaded from a path."""

    def generate_words(self):

    # print("Thou %s %s %s!"((random.choice(Column_1),
    #                         random.choice(Column_2),
    #                         random.choice(Column_3)))






    

    