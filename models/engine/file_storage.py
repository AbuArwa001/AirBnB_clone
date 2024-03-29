#!/usr/bin/python3
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
        return self.__objects

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
            raise ValueError(
                f"Class '{class_name}'" f"not found in module '{class_module}'"
            )

        return class_obj(**class_data)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        dict_to_save = {}
        for key, val in self.__objects.items():
            dict_to_save.update({key: val.to_dict()})
        try:
            with open(self.__file_path, "w", encoding="utf-8") as file:
                # json.dumps(self.__objects,
                # indent=4, sort_keys=True, default=str)
                file.write(json.dumps(dict_to_save, default=str))
                #  json.dump(self.__objects, file)
            return True  # Indicate success
        except Exception as e:
            print(f"Error occurred while saving: {e}")
            return False  # Indicate failure

    def reload(self):
        """Reloads __objects from the JSON file (path: __file_path)"""
        if os.path.isfile(self.__file_path):
            try:
                class_instances = {}
                with open(self.__file_path, "r", encoding="utf-8") as file:
                    class_instances = json.load(file)
                    for instance_id, data in class_instances.items():
                        class_name = data.get("__class__")
                        c_data = {key: value for key, value in data.items()}
                        new_instance = self.create_instance(class_name, c_data)
                        self.__objects[instance_id] = new_instance
                return True
            except OSError as e:
                print(f"Error opening file '{self.__file_path}': {e}")
                return None
            except json.JSONDecodeError as e:
                return None
        else:
            return None
