
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import jsonify
app = Flask(__name__)
@app.route('/')
def generate_epithets():
    d = {"epithets": []}
    return jsonify(d)




@app.route('/vocabulary')
def vocabulary():
    d = {"vocabulary": {}}
    return jsonify(d)