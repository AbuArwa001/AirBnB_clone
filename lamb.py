import re
import cmd

class YourClass(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.class_methods = {
            "BaseModel": {"all": lambda klass: f"all {klass}", "count": lambda klass: "c", "show": lambda klass, id: f"show {klass} {id}", "update": lambda klass: ""},
            "User": {"all": lambda klass: f"all {klass}", "count": lambda klass: "c", "show": lambda klass, id: f"show {klass} {id}", "update": lambda klass: ""},
            "Amenity": {"all": lambda klass: f"all {klass}", "count": lambda klass: "c", "show": lambda klass, id: f"show {klass} {id}", "update": lambda klass: ""},
            "City": {"all": lambda klass: f"all {klass}", "count": lambda klass: "c", "show": lambda klass, id: f"show {klass} {id}", "update": lambda klass: ""},
            "Place": {"all": lambda klass: f"all {klass}", "count": lambda klass: "c", "show": lambda klass, id: f"show {klass} {id}", "update": lambda klass: ""},
            "Review": {"all": lambda klass: f"all {klass}", "count": lambda klass: "c", "show": lambda klass, id: f"show {klass} {id}", "update": lambda klass: ""},
            "State": {"all": lambda klass: f"all {klass}", "count": lambda klass: "c", "show": lambda klass, id: f"show {klass} {id}", "update": lambda klass: ""}
        }

    def _commands(self, klass, method, id=None):
        if id:
            return self.class_methods[klass][method](klass, id)
        else:
            return self.class_methods[klass][method](klass)

    def precmd(self, line):
        """Check for command if it uses .all() notation"""
        line = line.strip()
        pattern = r"(^[A-Z][a-zA-Z]{2,})\.(all|count|show|update)\((\w+)\)"
        match = re.search(pattern, line)
        if match:
            klass = match.group(1)
            method = match.group(2)
            if klass in self.class_methods and method in self.class_methods[klass]:
                if method == "count":
                    line = self._commands(klass, method)
                    num_of_klasses = self.count(klass)
                    print(num_of_klasses)
                    line = ""
                elif method == "show":
                    id = match.group(3)
                    line = self._commands(klass, method, id)
                else:
                    line = self._commands(klass, method)
        return line

# Example usage:
# your_instance = YourClass()
# your_instance.cmdloop()
