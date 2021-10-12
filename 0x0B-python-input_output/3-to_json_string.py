#!/usr/bin/python3
'''
a modele that defines a function
that returns json representation of an object
'''
import json


def to_json_string(my_obj):
    ''' to json sring'''
    return json.dumps(my_obj)
