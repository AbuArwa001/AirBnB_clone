import os
import sys

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
    print("=====TEST MODULES===== ")

    for module_name in modules_to_test:
        module_path = os.path.join(base_directory, module_name + ".py")

        if os.path.exists(module_path):
            command = f'python3 -c \'print(__import__("models.{module_name}").{module_name}.__doc__)\''
            os.system(command)
        else:
            print(f"Module '{module_name}' not found.")
    print("=====TEST CLASSES===== ")
    for module_name in modules_class.keys():
        print(f"=================================={module_name}====================================")
        klass = modules_class[module_name]
        module_path = os.path.join(base_directory, module_name + ".py")

        if os.path.exists(module_path):
            # python3 -c 'print(__import__("my_module").MyClass.__doc__)'
            # python3 -c 'print(__import__("my_module").__doc__)'
            # python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
            # python3 -c 'print(__import__("models.base_model").base_model.__doc__)'
            command = f'python3 -c \'print(__import__("models.{module_name}").{module_name}.{klass}.__doc__)\''
            os.system(command)
        else:
            print(f"Module '{module_name}' not found.")
    print("=====TEST METHODS===== ")
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
