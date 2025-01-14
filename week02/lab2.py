elements = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "carbon"]
print("Elements: ", elements)
#  git add . && git commit -m "add elements array" && git push

# def funct_name():
#     return True
# def say_greeting(name, message="hi"):
#     print(f" {message}, {name}")
# say_greeting("Joel")
# say_greeting("joel", "Hello")

def get_valid_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Please enter a valid integer!")
            continue
