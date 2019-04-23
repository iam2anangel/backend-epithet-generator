#!/usr/bin/env python
# -*- coding: utf-8 -*-

from backend_epithet_generator.app import app
import json

def test_ramdomize():
    result = app.test_client().get('/randomize')
    assert result.status_code == 200
    assert result.data.decode()