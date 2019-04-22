#!/usr/bin/env python
# -*- coding: utf-8 -*-



import pytest
from helpers import Vocabulary
from helpers import EpithetGenerator

json_data = Vocabulary.read_json("resources/data.json")


def test_read_json_happy():
    assert isinstance(json_data, dict)
    assert len(json_data.keys()) == 3
    assert "bootless" in json_data["Column 1"]
    assert "base-court" in json_data["Column 2"]
    assert "coxcomb" in json_data["Column 3"]