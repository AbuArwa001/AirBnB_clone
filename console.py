#!/usr/bin/python3
"""
Module that imports  cmd module:
    console Starting point
"""
import cmd
import json
import re
from models import storage
import importlib
from typing import Any, Dict
import io
import sys


class HBNBCommand(cmd.Cmd):
    """
    console Command class that inherits
        cmd class
    """

    prompt = "(hbnb) "

    def __init__(self, stdin=None, stdout=None):
        """update BaseModel 1234-1234-1234 email aibnb@mail.com"""
        super().__init__()
        self.stdin = stdin if stdin else sys.stdin
        self.stdout = stdout if stdout else sys.stdout
        classes = [
            "BaseModel",
            "User",
            "Amenity",
            "City",
            "Place",
            "Review",
            "State",
        ]
        class_methods = {
            "all": lambda klass: f"all {klass}",
            "count": lambda klass: "c",
            "show": lambda klass, id=None:  (
                f"show {klass} {id}"
                if id
                else (
                    f"show {klass}"
                )
                ),
            "update": lambda klass, id, *args, **kwargs: (
                f"update {klass} {id} {args[0]} {args[1]}"
                if len(args) >= 2
                else (
                    f"update {klass} {id} {kwargs}"
                    if kwargs
                    else f"update {klass} {id}"
                )
            ),
            "destroy": lambda klass, id: f"destroy {klass} {id}",
        }
        self.class_methods = {
            klass: {method: func for method, func in class_methods.items()}
            for klass in classes
        }

    def _commands(self, klass, method, id=None, *args, **kwargs):
        if id or method == "show":
            if args:
                return self.class_methods[klass][method](klass, id, *args)
            elif kwargs:
                return self.class_methods[klass][method](klass, id, **kwargs)
            else:
                return self.class_methods[klass][method](klass, id)
        else:
            return self.class_methods[klass][method](klass)

    def precmd(self, line):
        """Check for command if it uses .all() notation"""
        # line = line.strip()
        pattern = (
            r"(^[A-Z]\w*)\."
            r"(all|count|show|update|destroy)"
            r'\("?([a-zA-z0-9\-]*)"?'
            r"("
            r'(?:,?\s?"?(\w*)"?)(?:,?\s?"?(\w*)"?)'
            r"|"
            r"(?:,?\s(\{.*\})))"
            r"\)"
        )
        match = re.search(pattern, line)
        if match:
            klass = match.group(1)
            method = match.group(2)
            id = match.group(3)
            group5 = match.group(5)
            group6 = match.group(6)
            group7 = match.group(7)
            if (
                klass in self.class_methods
                and method in self.class_methods[klass]
            ):
                if method == "count":
                    line = self._commands(klass, method)
                    num_of_klasses = self.count(klass)
                    print(num_of_klasses)
                    line = ""
                elif method == "show" or method == "destroy":
                    print(id)
                    print(klass)
                    line = self._commands(klass, method, id)
                    print(line)
                elif method == "update":
                    if group7:
                        dictionry = eval(group7)
                        self.do_update(f"{klass} {id}", **dictionry)
                        line = ""
                    elif group5 and group6:
                        line = self._commands(
                            klass, method, id, group5, group6
                        )
                else:
                    line = self._commands(klass, method)

        return cmd.Cmd.precmd(self, line)

    def do_quit(self, arg):
        """Quits the cmd interface usin quit command"""
        return True

    def do_EOF(self, line):
        """Exits command using key interrupt"""
        return True

    def postloop(self):
        print("")

    @staticmethod
    def count(arg):
        classes = [
            "BaseModel",
            "User",
            "Amenity",
            "City",
            "Place",
            "Review",
            "State",
        ]
        storage.reload()
        all_objs = storage.all()
        all = []
        for obj_id in all_objs.keys():
            class_name, _ = obj_id.split(".")
            if arg in classes and arg == class_name:
                obj = str(all_objs[obj_id])
                all.append(obj)
        length = len(all)
        return length

    @staticmethod
    def create_instance(class_name: str, class_data: Dict[str, Any]) -> Any:
        """Create an instance of a class with the given class name and data."""
        module_map = {
            "BaseModel": "models.base_model",
            "User": "models.user",
            "Amenity": "models.amenity",
            "City": "models.city",
            "Place": "models.place",
            "Review": "models.review",
            "State": "models.state",
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

    def do_create(self, arg):
        """
        Create a new instance of BaseModel,
        save it to the JSON file, and print its id.

        Args:
            arg (str): The argument
            specifying the type of instance to create.

        Returns:
            Model id created

        Example:
           create BaseModel
        """
        classes = [
            "BaseModel",
            "User",
            "Amenity",
            "City",
            "Place",
            "Review",
            "State",
        ]
        if not arg:
            print("** class name missing **")
        elif arg not in classes:
            # print(arg)
            print("** class doesn't exist **")
        else:
            class_name = arg
            # Exclude __class__ key
            # class_data = {key: value for key, value in data.items()
            #               if key != '__class__'}
            new_instance = self.create_instance(class_name, {})
            print(new_instance.id)
            new_instance.save()
            #
            # if arg == "BaseModel":
            #     model = BaseModel()
            #     print(model.id)
            #     model.save()
            # elif arg == "User":
            #     model = User()
            #     print(model.id)
            #     model.save()

    def do_show(self, arg):
        """
        Display the string representation of
        one or more instances based on their class name and id.

        Args:
            *arg: Variable number of
            arguments representing instances to display.

        Returns:
            string representation of an instance
        Example:
            show BaseModel 1234-1234-1234
        """
        #
        # TODO: 1) consider when the arguments are three
        #

        # classes = ["BaseModel", "User", "Amenity",
        #            "City", "Place", "Review", "State"]
        print(arg)
        ln = arg.split()
        size = len(ln)
        all_objs = storage.all()
        if size == 0:
            print("** class name missing **")
        elif ln[0] not in self.class_methods:
            print("** class doesn't exist **")
        elif size == 1:
            print("** instance id missing **")
        elif size == 2:
            key = ln[0] + "." + ln[1]
            if key in all_objs.keys():
                obj = all_objs[key]
                print(obj)
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Display the string representation of
         all instances based on the specified class name, or of
         all instances if no class name is provided.
        Args:
            arg (str): The class name to filter instances by.
            If not provided, all instances are displayed.
        Returns:
            None
        Prints:
            List of strings representing the
            instances matching the specified class name,
            or all instances if no class name is provided.
            If the class name doesn't
            exist, prints "** class doesn't exist **".

        Examples:
            all MyModel
            all
        """
        #
        # TODO: 1) CONSIDER A SCENARIO WHERE THERE ARE MANY ARGUMENTS
        #       2)
        #
        #
        storage.reload()
        all_objs = storage.all()
        all = []
        class_names = []
        if not arg:
            for obj_id in all_objs.keys():
                obj = str(all_objs[obj_id])
                all.append(obj)
        for obj_id in all_objs.keys():
            obj = str(all_objs[obj_id])
            [class_name, id] = obj_id.rsplit(".")
            class_names.append(class_name)
            if class_name == arg:
                all.append(obj)
        if arg and arg not in class_names:
            print("** class doesn't exist **")
        else:
            print(all)

    def do_destroy(self, arg):
        """
        Deletes an instance of a class based on the provided name and id.

        Args:
            arg (str): The id of the instance to be deleted.

        Returns:
            None
        """
        # classes = ["BaseModel", "User", "Amenity",
        #            "City", "Place", "Review", "State"]
        ln = arg.split()
        size = len(ln)
        all_objs = storage.all()
        if size == 0:
            print("** class name missing **")
        elif ln[0] not in self.class_methods:
            print("** class doesn't exist **")
        elif size == 1:
            print("** instance id missing **")
        elif size == 2:
            key = ln[0] + "." + ln[1]
            if key in all_objs.keys():
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def emptyline(self):
        pass

    @staticmethod
    def process_match(match):
        return "'" + match.group(2).replace('"', "'") + "'"

    def do_update(self, arg, *ags, **kwargs):
        """
        Update an instance based on the class name and id
        by adding or updating attributes (save the changes into the JSON file).

        Args:
            arg (str): A string containing the class name,
            instance id, attribute name, and attribute value.
        Returns:
            None

        Example:
            update BaseModel 1234-1234-1234 email aibnb@mail.com
        """
        ln = arg.split()
        size = len(ln)
        all_objs = storage.all()

        if not kwargs:
            if size == 0:
                print("** class name missing **")
            elif ln[0] not in self.class_methods:
                print("** class doesn't exist **")
            elif size == 1:
                print("** instance id missing **")
            elif size == 2:
                print("** attribute name missing **")
            elif size == 3:
                print("** value missing **")
            elif size == 4:
                _, _, attr_name, attr_value = arg.split()
                # attr_name = ln[2]
                # attr_value = ln[3].replace('"', "")
                attr_value = attr_value.replace('"', "")
                key = ln[0] + "." + ln[1]
                if key in all_objs.keys():
                    setattr(all_objs[key], attr_name, attr_value)
                    storage.save()
                else:
                    print("** no instance found **")
        else:
            key = ln[0] + "." + ln[1]
            if key in all_objs.keys():
                for attr, val in kwargs.items():
                    setattr(all_objs[key], attr, val)
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
