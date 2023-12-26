try:
    result = 10 + "hello"  # This will raise a TypeError
except TypeError:
    print("Cannot add a number and a string.")

try:
    res = 10/0
except ZeroDivisionError:
    print("Zero devision Error")