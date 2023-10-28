import importlib

def call_function(name):

    try:
        module = importlib.import_module(name) # Each file name should be its function name
        function = getattr(module, name)
        return function()
    except ModuleNotFoundError:
        print(f"Function {n} not found.")

if __name__ == '__main__':
    names_function = ["b64_decode"]

    print("Available functions:")
    for i, name in enumerate(names_function):
        print(f"{i}: {name}")

    while True:
        try:
            n = int(input(f"Enter a number between 0 and {len(names_function)-1}: "))
            if 0 <= n < len(names_function):
                result = str(call_function(names_function[n]))
                print(f"Result of function: {result}")
                break
            else:
                print(f"Enter a valid number between 0 and {len(names_function)-1}")
        except ValueError:
            print("Enter a valid number.")