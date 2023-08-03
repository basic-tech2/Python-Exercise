def default_parameter(name="Loading...."):
    return print(name)

default_parameter()

def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}")
    print("Welcome on board")


greet("Astainy", "Harris")

print("Loading...........")

def get_greeting(name):
    return f"Hi {name}"


function = get_greeting(input("Name: "))
print(function)

print("-------------------------------")
local = "Hi"

def modified_local_variabel(name):
    global local # bad practice
    local = 'Hello '
    return local + name

function = modified_local_variabel("Joe")
print(function)
print(local)



