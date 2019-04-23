#!/usr/bin/env python
# -*- coding: utf-8 -*-



import json
import random


class Vocabulary:
    """
    Handle loading in a JSON file with proper unfinished swears in it!
<<<<<<< HEAD
=======

>>>>>>> b67c3b42d3d4408adfa09f8bfc59ce4381ec4dca
    Usage:
        data = Vocabulary.read_json("/path/to/data.json")
    """

    def read_json(path, mode='r'):
        with open(path, mode=mode) as handle:
            return json.load(handle)




class EpithetGenerator:
    """select one random word from each column of the list and generate a 
       quantity of epithets from a vocabulary file loaded from a path."""

    def generate_word(self):
        data = Vocabulary.read_json("resources/data.json")
        return "{} {} {}!".format(random.choice(data["Column 1"]), 
        random.choice(data["Column 2"]), random.choice(data["Column 3"]))
    
    def generate_words(self, quantity):
        epithets_list = []

        for _ in range(quantity):
            epithets_list.append(self.generate_word() + "!")
<<<<<<< HEAD
            return epithets_list
=======
            return epithets_list

   






    

    
>>>>>>> b67c3b42d3d4408adfa09f8bfc59ce4381ec4dca
