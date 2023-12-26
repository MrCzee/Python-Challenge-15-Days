# DICTIONARIES

#Key-value pairs - unique values and used to access its associated value.
# Think of them like a phonebook, where names are keys and phone numbers are values.


#Curly braces: my_dict = {"name": "Alice", "age": 30}.

#Unordered: and mutable (can add remove insert values)

#Accessing values = name = my_dict["name"]




#  getting started ....

my_phone_dict = {"name": "imrna", "phone_No": 0o306562657}

print(my_phone_dict)

# accessing
name = my_phone_dict["name"]
print(name)

#Common operations:

my_phone_dict["City"] = "New York"
print(my_phone_dict)
del my_phone_dict["name"]
print(my_phone_dict)

# getting all keys

keys = my_phone_dict.keys()
print(keys)
values = my_phone_dict.values()
print(values)
items = my_phone_dict.items()
print(items)

# checking if exists
if "phone_No" in my_phone_dict:
    print("Phone_No availables")



#Advanced Dictionary

# 1. Marging dictionaries

dic_A = {"A": "1","B":"2"}

dic_B = {"C":"3", "D":"4"}

marged_dicts = {**dic_A, **dic_B}
print(marged_dicts)

# 2. Using get() for Safe Key Access:

person = {"name": "Muhammad"}

age = person.get("age","unknown")

print(age)






from  collections import defaultdict

words_count = defaultdict(int) # value int 0 default

text  = "Apple Mango Banana"

for word in text.split():
    words_count[word] =+ 1
    print(word)














