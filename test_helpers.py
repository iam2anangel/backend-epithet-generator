#!/usr/bin/env python
# -*- coding: utf-8 -*-



import pytest
import os
# from backend_epithet_generator import app
from backend_epithet_generator.helpers import Vocabulary as V
from backend_epithet_generator.helpers import EpithetGenerator as Epg
# from backend_epithet_generator.helpers import EpithetGenerator


json_data = V.read_json("resources/data.json")
Ep = Epg().generate_word()





def test_random_word():
    assert isinstance(single_ep, dict)
    assert len(json_data.keys()) == 3
    assert 'artless' in json_data['Column 1']
    assert 'base-court' in json_data['Column 2']
    assert 'apple-john' in json_data['Column 3']

def test_random_word_fail():
    with pytest.raises(AssertionError):
        assert isinstance(json_data, str)
        assert len(json_data.keys()) == 'Not a Shakesperian word'
        assert "Oopsie" not in json_data["Column 1"]
        assert "Oopsie" not in json_data["Column 2"]
        assert "Oopsie" not in json_data["Column 3"]


def test_single_ep():
    assert isinstance(Ep, str)
    assert len(Ep.split(" ")) == 3
    assert Ep.split(" ")[0] in json_data["Column 1"]
    assert Ep.split(" ")[1] in json_data["Column 2"]
    assert Ep.split(" ")[2] in json_data["Column 3"]


def test_single_ep_fail():
    with pytest.raises(AssertionError):
        assert isinstance(Ep, dict)
    with pytest.raises(AssertionError):
        assert len(Ep.split(" ")) == "Flask is awesome"
   

   



    


   

   