# understanding tuple in detail
#An ordered collection of items, similar to lists but immutable (cannot be changed after creation).

my_tuple = (1, 3, 5, 6, 7, "Imran ", True)

empty_tuple = ()

single_tuple = (12,) ## Comma is essential for single-item tuples

#Accessing elements:

first_element = my_tuple[0] # 1
last_element = my_tuple[-1] # True


#Slicing:

sub_tuple = my_tuple[1:4]

#Common operations:

if "Imran" in my_tuple:
    print("Apple is present")

#Concatenation: Creates a new tuple by combining existing tuples:

my_new_tuple  = my_tuple +("Asghar", "Sultan", "Maaz Saleem")

#Repetition

tuple_repetations = my_tuple*2



print("First_Element :", first_element)
print("Last_Element :", last_element)
print("subtupple = : ", sub_tuple)
print("my_new_tuple", my_new_tuple)
print("Repetation :", tuple_repetations)

# Methods of Tuple 1. count 2.index


# number of one count in the my_tuple_count
one_count = my_tuple.count(1)
# Find the index of the first occurrence of 2
index_of_two = my_tuple.index(1)

print(f"Index of two: {index_of_two}")
print(f"Number of ones: {one_count}")
