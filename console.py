import cmd
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
    pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
