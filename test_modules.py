import os
import sys
import inspect


def test_modules(base_directory="models", modules_to_test=None):
    if modules_to_test is None:
        modules_to_test = ["base_model", "user", "review", "place", "amenity", "state", "city"]
        modules_class =  {
                'base_model': 'BaseModel',
                'user': 'User',
                'review': 'Review',
                'place': 'Place',
                'amenity': 'Amenity',
                'state': 'State',
                'city': 'City'
            }
    # modules_class = ["base_model", "User", "Review", "Place", "Amenity", "State", "City"]
    print("===============================MODULES DOCUMENTATIONS=================================")

    for module_name in modules_to_test:
        module_path = os.path.join(base_directory, module_name + ".py")

        print(f"===== {module_name}-MODULE---DOCUMENTATION===== ")
        if os.path.exists(module_path):
            command = f'python3 -c \'print(__import__("models.{module_name}").{module_name}.__doc__)\''
            os.system(command)
        else:
            print(f"Module '{module_name}' not found.")
    print("================================END OF MODULES DOCUMENTATIONS===========================")
    print("================================CLASS DOCUMENTATIONS====================================")
    for module_name in modules_class.keys():
       
        klass = modules_class[module_name]
        print(f"=================================={klass}-CLASS-DOCUMENTATION-============================")
        module_path = os.path.join(base_directory, module_name + ".py")

        if os.path.exists(module_path):
            # python3 -c 'print(__import__("my_module").MyClass.__doc__)'
            # python3 -c 'print(__import__("my_module").__doc__)'
            # python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
            # python3 -c 'print(__import__("models.base_model").base_model.__doc__)'
            command = f'python3 -c \'print(__import__("models.{module_name}").{module_name}.{klass}.__doc__)\''
            os.system(command)
            module = __import__(f"models.{module_name}", fromlist=[klass])
            class_obj = getattr(module, klass)
            print("================================METHOD DOCUMENTATIONS==============================")
            for method_name, method in inspect.getmembers(class_obj, inspect.isfunction):
                print(f"================================{method_name}-METHOD--DOCUMENTATION================")
                print(f"Method: {method_name}")
                print(f"Docstring: {method.__doc__}")
            print("====END=====")
        else:
            print(f"Module '{module_name}' not found.")

    # for module_name in modules_to_test:
    #     module_path = os.path.join(base_directory, module_name + ".py")

    #     if os.path.exists(module_path):
    #         # python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    #         # python3 -c 'print(__import__("my_module").__doc__)'
    #         # python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    #         command = f'python3 -c \'print(__import__("models.{module_name}").{module_name}.__doc__)\''
    #         os.system(command)
    #     else:
    #         print(f"Module '{module_name}' not found.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # User provided custom directory and module names
        directory = sys.argv[1]
        modules = sys.argv[2:]
        test_modules(base_directory=directory, modules_to_test=modules)
    else:
        # Use default directory and module names
        test_modules()
