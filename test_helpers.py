#!/usr/bin/env python
# -*- coding: utf-8 -*-



import pytest
import os
from backend_epithet_generator.helpers import Vocabulary
from backend_epithet_generator.helpers import EpithetGenerator

json_data = Vocabulary.read_json("resources/data.json")


def test_random_word():
    assert isinstance(json_data, dict)
    assert len(json_data.keys()) == 3
    assert 'artless' in json_data['Column 1']
    assert 'base-court' in json_data['Column 2']
    assert 'apple-john' in json_data['Column 3']
    assert 'Jen was here' not in json_data.keys()

def test_random_word_fail():
    with pytest.raises(AssertionError):
        assert isinstance(json_data, str)
        assert len(json_data.keys()) == 'Not a Shakesperian word'
    

def test_epithet():
    assert isinstance(EpithetGenerator.generate_words(), str)
    assert len(EpithetGenerator.generate_words, list)
    assert EpithetGenerator.generate_words()[1].split(' ') in json_data['Column 2']

def test_epithet_fail():
    with pytest(AssertionError):
        assert isinstance(EpithetGenerator.generate_words(), str)
        assert len(EpithetGenerator.generate_words()) == 50
   

   