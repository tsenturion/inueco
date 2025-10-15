from src.capitalize import capitalize

if capitalize("hello") != "Hello":
    raise Exception("hello is not capitalized")

if capitalize("") != "":
    raise Exception("empty string is capitalized")

if capitalize(None) != None:
    raise Exception("None is capitalized")

assert capitalize("hello") == "Hello"
assert capitalize("") == ""
assert capitalize(None) == None

print("all tests passed!")