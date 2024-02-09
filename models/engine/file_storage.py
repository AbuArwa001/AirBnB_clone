"""
    Module for dealing with file storage
"""
import json
import os.path
import importlib
from typing import Any, Dict


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
            # Exclude __class__ key
            class_data = {key: value for key, value in data.items()
                          if key != '__class__'}
            new_instance = self.create_instance(class_name, class_data)
            class_instances[instance_id] = new_instance
        return class_instances

    @staticmethod
    def create_instance(class_name: str, class_data: Dict[str, Any]) -> Any:
        """Create an instance of a class with the given class name and data."""
        module_map = {
            "BaseModel": "..base_model",
            "User": "..user",
            "Amenity": "..amenity",
            "City": "..city",
            "Place": "..place",
            "Review": "..review",
            "State": "..state",
        }

        class_module = module_map.get(class_name)
        if class_module is None:
            raise ValueError(f"Class '{class_name}' is not supported")

        try:
            module = importlib.import_module(class_module, package=__package__)
            class_obj = getattr(module, class_name)
        except ImportError:
            raise ValueError(f"Module '{class_module}' not found")
        except AttributeError:
            raise ValueError(f"Class '{class_name}'"
                             f"not found in module '{class_module}'")

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
                # json.dumps(self.__objects,
                # indent=4, sort_keys=True, default=str)
                file.write(json.dumps(self.__objects, default=str))
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
                return self.__objects
            except OSError as e:
                print(f"Error opening file '{self.__file_path}': {e}")
                return None
            except json.JSONDecodeError as e:
                # print(f"Error decoding
                # JSON from file '{self.__file_path}': {e}")
                return None
        else:
            # Handle the case when the file doesn't exist
            # print(f"File '{self.__file_path}' doesn't exist.")
            return None
