#!/usr/bin/python3
import cmd
import json

from models.base_model import BaseModel
from models import storage
import re
from datetime import datetime

"""
Module that imports  cmd module:
    console Starting point
"""


class HBNBCommand(cmd.Cmd):
    """
    console Command class that inherits
        cmd class
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quits the cmd interface usin quit command"""
        return True

    def do_EOF(self, line):
        """Exits command using key interrupt"""
        return True

    def do_create(self, arg):
        """
            Create a new instance of BaseModel, save it to the JSON file, and print its id.

            Args:
                arg (str): The argument specifying the type of instance to create.

            Returns:
                Model id created

            Example:
               create BaseModel
        """
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            model = BaseModel()
            print(model.id)
            model.save()

    def do_show(self, arg):
        """
        Display the string representation of one or more instances based on their class name and id.

        Args:
            *arg: Variable number of arguments representing instances to display.

        Returns:
            string representation of an instance
        Example:
            show BaseModel 1234-1234-1234
        """
        # 
        # TODO: 1) consider when the arguments are three
        #       2) Enter shouldnt execute anything (FOR NOW IT EXECUTE PREVIOUS COMMANDS)
        # 
        # 
        ln = arg.split()
        size = len(ln)
        all_objs = storage.all()
        if size == 0:
            print("** class name missing **")
        elif ln[0] != "BaseModel":
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

        # 
        # TODO: Implement destroy on file storage
        #  

    def do_all(self, arg):
        """
        Display the string representation of all instances based on the specified class name, or of all instances if no class name is provided.
        
        Args:
            arg (str): The class name to filter instances by. If not provided, all instances are displayed.

        Returns:
            None
        
        Prints:
            List of strings representing the instances matching the specified class name, or all instances if no class name is provided.
            If the class name doesn't exist, prints "** class doesn't exist **".

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
                obj = all_objs[obj_id]
                all.append(obj)
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            class_name = obj_id.split(".")
            class_names.append(class_name[0])
            if class_name[0] == arg:
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
        ln = arg.split()
        size = len(ln)
        all_objs = storage.all()
        if size == 0:
            print("** class name missing **")
        elif ln[0] != "BaseModel":
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

    def do_update(self, arg):
        """
        Update an instance based on the class name and id by adding or updating attributes (save the changes into the JSON file).

        Args:
            arg (str): A string containing the class name, instance id, attribute name, and attribute value.
            
        Returns:
            None

        Example:
            update BaseModel 1234-1234-1234 email aibnb@mail.com 
    """
        ln = arg.split()
        size = len(ln)
        all_objs = storage.all()
        if size == 0:
            print("** class name missing **")
        elif ln[0] != "BaseModel":
            print("** class doesn't exist **")
        elif size == 1:
            print("** instance id missing **")
        elif size == 2:
            print("** attribute name missing **")
        elif size == 3:
            print("** value missing **")
        elif size == 4:
            attr_name = ln[2]
            attr_value = ln[3].replace('"', "'")
            key = ln[0] + "." + ln[1]
            first_part = f"[{ln[0]}] ({ln[1]}) "
            second_part = f"'{attr_name}': {attr_value}, "
            #  update BaseModel 6a448ca5-9ac6-4b52-b830-2e63658e168d first_name "Khalfan"
            # Replace strings within double quotes with strings within single quotes
            # processed_string = re.sub(pattern, self.process_match, second_part)
            if key in all_objs.keys():
                """
                {
                    "BaseModel.6a448ca5-9ac6-4b52-b830-2e63658e168d": 
                    "[BaseModel] (6a448ca5-9ac6-4b52-b830-2e63658e168d) 
                    {
                    'id': '6a448ca5-9ac6-4b52-b830-2e63658e168d', 
                    'created_at': datetime.datetime(2024, 2, 7, 10, 51, 51, 128175), 
                    'updated_at': datetime.datetime(2024, 2, 7, 10, 51, 51, 128238)}"
                }
                """
                dict_part_match = re.search(r'\{.*\}', all_objs[key])
                dict_part = dict_part_match.group()
                # setattr(dict_part, attr_name, attr_value)
                modified = dict_part[:1] + second_part + dict_part[1:]
                all_objs[key] = first_part + modified
                storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    # 
    # TODO: 1) IMPLEMET NON-INTERACTIVE MODE
    #       2)  ADD NEW LINE F0R NIM (NON-INTERSCTIVE MODE)
    #
    # 
    # 
    interpreter = HBNBCommand()
    interpreter.cmdloop()
