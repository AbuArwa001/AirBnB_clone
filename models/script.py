import os

# List of module names to test
modules_to_test = ["user", "review", "place", "amenity", "state", "city"]

# Base directory where the modules are located
base_directory = "models"

# Iterate over each module and execute the command
for module_name in modules_to_test:
    # Construct the full module path
    module_path = os.path.join(base_directory, module_name + ".py")

    # Check if the module file exists
    if os.path.exists(module_path):
        # Construct the command
        command = (f'python3 -c \'print(__import__("models.{module_name}")'
                   f'.{module_name}.__doc__)\'')

        # Execute the command
        os.system(command)
    else:
        print(f"Module '{module_name}' not found.")
