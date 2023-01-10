#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(filename):
    """
    creates an Object from a "JSON file"
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
