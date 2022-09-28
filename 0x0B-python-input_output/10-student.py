#!/usr/bin/python3
"""student module with class student"""


class Student:
    """class student and blah blah"""

    def __init__(self, first_name, last_name, age):
        """Description: instantiation"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Discription: retrieves a dict representation
        of student

        Args:
            - attrs: list of atrributes
        Returns: dictionary
        """

        if (type(attrs) == list and
                all(type(x) == str for x in attrs)):
            new = dict()
            for l in attrs:
                if l in self.__dict__:
                    new[l] = self.__dict__[l]
            return new
        return self.__dict__
