"""
    Module for dealing with file storage
"""

import json
import os.path

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
        """returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        # print(obj)
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects.update({key: obj})

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
                print(f"Error decoding JSON from file '{self.__file_path}': {e}")
                return None
        else:
            # Handle the case when the file doesn't exist
            # print(f"File '{self.__file_path}' doesn't exist.")
            return None
