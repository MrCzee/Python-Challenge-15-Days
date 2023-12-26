

my_list = ['Apples', 'Bananas', 'Oranges']
my_Numbers = [1,3,2,6,7]
my_mixed_list = [1,3,4,5,"abcd", True]

# accessing Element: using index

my_new_list = my_list[2]

print(f"List Accessing using Indexing: {my_new_list}")

# accessing Element: using Slicing

my_list_slice = my_Numbers[1:3]

print(f"List Accesing using slicing: {my_list_slice}")



#modifying list adding, remove, insert, pop

# Adding item - list

my_list.append("Cherries")

# insert item - list

my_list.insert(2, "mango")


print(f"After Inserting:{my_list} ")
# remove item - list

#my_Numbers.remove("Bananas")
my_list.remove("Bananas")

print(f"Values Removed (Bananas): {my_list}")
# pop item - list

mylist = my_list.pop()

print(f"POP Values: {mylist}")

#Common operations:

#Find index
 #item_index = my_list.index("Apples")
item_index = my_list.index("Apples")

#Check membership:

if "mango" in my_list:
    print("Mango available")

#Sort

my_Numbers.sort()
print(my_Numbers)

#Reverse

my_mixed_list.reverse()

print(my_mixed_list)