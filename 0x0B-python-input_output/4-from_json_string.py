#!/usr/bin/python3
'''
a module that defines a funtion
that returns an object (Python data structure)
represented by a JSON string
'''
import json


def from_json_string(my_str):
    """from json string"""
    return json.loads(my_str)
