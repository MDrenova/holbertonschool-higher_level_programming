#!/usr/bin/python3
'''Write a function that returns the dictionary description
with simple data structure (list, dictionary, string,
integer and boolean) for JSON serialization of an object:'''


def class_to_json(obj):
    '''class to json'''
    return obj.__dict__


"""def class_to_json(obj):
    Converts an object to a dictionary suitable for JSON serialization.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary containing serializable attributes.
    serialized_dict = {}  # Initialize an empty dictionary

    # Get all attributes of the object
    attributes = dir(obj)

    for attr_name in attributes:
        # Skip private attributes (those starting with an underscore)
        if not attr_name.startswith('_'):
            # Get the attribute value
            attr_value = getattr(obj, attr_name)

            # Check if the attribute value is serializable
            if isinstance(attr_value, (list, dict, str, int, bool)):
                # Add the attribute to the dictionary
                serialized_dict[attr_name] = attr_value

    return serialized_dict

# Example usage:
class Person:
    def __init__(self, name, age, hobbies):
        self.name = name
        self.age = age
        self.hobbies = hobbies

# Create an instance of the Person class
person_obj = Person(name="Alice", age=30, hobbies=["reading", "swimming"])

# Serialize the object to a dictionary
serialized_data = class_to_json(person_obj)

# Print the serialized data
print(serialized_data)
"""
