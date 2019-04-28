#!/usr/bin/env python
# -*- coding: utf-8 -*-

from backend_epithet_generator.app import app
import json



def test_generate_word():
    with app.test_client as c:
        result = c.get("/")
        assert result.status_code == 200

def test_generate_words():
    result = app.test_client().get("/epithets/<int:quantity>")
    assert result.status_code == 200
    assert result.data.decode()

def test_vocab():
    result = app.test_client().get("/vocabulary")
    assert result.status_code == 200
    assert result.data.decode()


def test_ramdomize():
    result = app.test_client().get('/randomize')
    assert result.status_code == 200
    assert result.data.decode()