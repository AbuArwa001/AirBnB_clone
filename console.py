#!/usr/bin/python3
import cmd
from models import storage
import importlib
from typing import Any, Dict

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
            raise ValueError(f"Class '{class_name}'"
                             f"not found in module '{class_module}'")
        return class_obj(**class_data)

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
        classes = ["BaseModel", "User", "Amenity",
                   "City", "Place", "Review", "State"]
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

        classes = ["BaseModel", "User", "Amenity",
                   "City", "Place", "Review", "State"]
        ln = arg.split()
        size = len(ln)
        all_objs = storage.all()
        if size == 0:
            print("** class name missing **")
        elif ln[0] not in classes:
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
        classes = ["BaseModel", "User", "Amenity",
                   "City", "Place", "Review", "State"]
        ln = arg.split()
        size = len(ln)
        all_objs = storage.reload()
        if size == 0:
            print("** class name missing **")
        elif ln[0] not in classes:
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
        #
        #  TODO: Take note on what can be done about the quotes
        #       in attr_val what if it appears on attr_name(we will have undesire quotes)
        #
        #
        classes = ["BaseModel", "User", "Amenity",
                   "City", "Place", "Review", "State"]
        ln = arg.split()
        size = len(ln)
        all_objs = storage.reload()
        if size == 0:
            print("** class name missing **")
        elif ln[0] not in classes:
            print("** class doesn't exist **")
        elif size == 1:
            print("** instance id missing **")
        elif size == 2:
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
                all_objs[key][attr_name] = attr_value
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
