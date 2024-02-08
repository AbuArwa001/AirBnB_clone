"""
    Module for dealing with file storage
"""

import json
import os.path
import importlib


class FileStorage:
    """
    Serializes instances to a JSON file 
    and deserializes JSON file to instances:
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self) -> None:
        pass

    def all(self):
        """Returns instances of classes based on data in __objects."""
        from models.base_model import BaseModel

        class_instances = {}
        for instance_id, data in self.__objects.items():
            class_name = data['__class__']
            class_data = {key: value for key, value in data.items() if key != '__class__'}  # Exclude __class__ key
            new_instance = self.create_instance(class_name, class_data)
            class_instances[instance_id] = new_instance
        return class_instances

    def create_instance(self, class_name, class_data):
        """Creates an instance of a class with the given class name and data."""
        try:
            module = importlib.import_module('..base_model',
                                             package=__package__)  # Assuming `base_model` is the module name
            class_obj = getattr(module, class_name)
        except (ImportError, AttributeError):
            raise ValueError(f"Class '{class_name}' not found in module '..base_model'")
        return class_obj(**class_data)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        # print(obj)
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects.update({key: obj.__dict__})

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        try:
            with open(self.__file_path, 'w', encoding='utf-8') as file:
                # json.dumps(self.__objects, indent=4, sort_keys=True, default=str)
                file.write(json.dumps(self.__objects, indent=4, sort_keys=True, default=str))
                #  json.dump(self.__objects, file)
            return True  # Indicate success
        except Exception as e:
            print(f"Error occurred while saving: {e}")
            return False  # Indicate failure

    def reload(self):
        """Reloads __objects from the JSON file (path: __file_path)"""
        if os.path.isfile(self.__file_path):
            try:
                with open(self.__file_path, 'r', encoding='utf-8') as file:
                    self.__objects = json.load(file)
            except OSError as e:
                print(f"Error opening file '{self.__file_path}': {e}")
                return None
            except json.JSONDecodeError as e:
                # print(f"Error decoding JSON from file '{self.__file_path}': {e}")
                return None
        else:
            # Handle the case when the file doesn't exist
            # print(f"File '{self.__file_path}' doesn't exist.")
            return None
