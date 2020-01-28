#!/usr/bin/python3


"""
Base class
"""

import json
import os
import csv


class Base:

    """Base class definition"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        jsons = "[]"

        if list_objs is not None:
            jsons = cls.to_json_string([o.to_dictionary() for o in list_objs])

        with open(filename, 'w') as f:
            f.write(jsons)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            base = cls(1, 1)
        else:
            base = cls(1)
        cls.update(base, **dictionary)
        return base

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        if os.path.isfile(filename):
            with open(filename, 'r') as f:
                result = cls.from_json_string(f.read())
                return [cls.create(**r) for r in result]
        else:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as csvfile:
            fieldnames = list_objs[0].to_dictionary()
            fieldnames = list(fieldnames)
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            [writer.writerow(obj.to_dictionary()) for obj in list_objs]

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        if os.path.isfile(filename):
            with open(filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                my_list = []
                for row in reader:
                    for key in row:
                        row[key] = int(row[key])
                    my_list.append(cls.create(**row))
                return my_list
        else:
            return []
