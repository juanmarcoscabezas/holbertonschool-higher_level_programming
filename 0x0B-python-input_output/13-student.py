#!/usr/bin/python3


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None and all(isinstance(item, str) for item in attrs):
            dictionary = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    dictionary[key] = value
            return dictionary
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            self.__dict__[key] = value
