#!/usr/bin/python3
"""Defines the Base class
"""


json = __import__('json')


class Base:
    """Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialise base class
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def validate_integer(self, name, value=None):
        """validate integers passed, raises an
        exception if not an interger
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0 and name in ['x', 'y']:
            raise ValueError("{} must be >= 0".format(name))
        if value <= 0 and name not in ['x', 'y']:
            raise ValueError("{} must be > 0".format(name))

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries == None:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        with open(
                "{}.json".format(cls.__name__),
                'w',
                encoding='utf-8'
                ) as f:
            if list_objs == None:
                return
            dicts = map(cls.to_dictionary, list_objs)
            f.write(Base.to_json_string(list(dicts)))

    @staticmethod
    def from_json_string(json_string):
        if json_string == None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if 'size' in dictionary.keys():
            new_obj = cls(1, 1)
        else:
            new_obj = cls(1, 1)
        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def load_from_file(cls):
        with open(
                "{}.json".format(cls.__name__),
                'r',
                encoding='utf-8'
                ) as f:
            list_dictionaries_str = f.read()
            list_dictionaries = Base.from_json_string(list_dictionaries_str)
            list_instances = []
            for item in list_dictionaries:
                list_instances.append(cls.create(**item))
            return list_instances
