#Python Sets
# A set is a collection which is unordered, unchangeable*, and unindexed. And do not allow duplicate values.
# we can add and remove items from sets.

# For Example:

boys_set = {"Danish","Zohaib","Bilal","Arfeen"}
# print(len(boys_set))
girls_set = {"Hafsa","Zara","Areeba","Aqsa"}
# print(type(girls_set))
mix_data_set = {"Pakistan", 112, True, 1, 404, "male"}
# print(len(mix_data_set))

boys_set.add("Saeed")
print(boys_set)

# mix_data_set.update(boys_set)
# print(mix_data_set)

# boys_set.remove("akber") #if item not exist then error will be show
# print(boys_set)

# boys_set.discard("akber") # no errorif value not exist
# print(boys_set)

# x = mix_data_set.pop()  #rendom item removed
# print(x)

# mix_data_set.clear()
# print(mix_data_set)

# del mix_data_set
# print(mix_data_set)

# girls_set.copy()
# print(girls_set)

