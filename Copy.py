# list copy
import copy
a = [1,2,3]
a_list = list(a)
a_index = a[:]
a_copy = a.copy()
print("a: ", a)
a.append(5)
print("a (appended): ", a)
print("Shallow copy")
print("a_list: ", a_list)
print("a_index: ", a_index)
print("a_copy: ", a_copy)

# deep copy
a = [1, [2,3]]
print("\na: ", a)
print("Deep copy")
a_deepcopy = copy.deepcopy(a)
print("a_deepcopy: ", a_deepcopy)


# Shallow copy and deep copy
a = [1, [2,3]]
a_ref = a
a_shallowcopy = copy.copy(a)
a_deepcopy = copy.deepcopy(a)

print("{:<15}{:<20}{}".format("a:", f"{a}", f"id:{id(a_ref)}"))
print("{:<15}{:<20}{}".format("a_shallow_copy:", f"{a_shallowcopy}", f"id:{id(a_shallowcopy)}"))
print("{:<15}{:<20}{}".format("a_deepcopy:", f"{a_deepcopy}", f"id:{id(a_deepcopy)}"))

a[0] = 4
print("\nChange immutable part: a[0] = 4")
print("{:<15}{:<20}{}".format("a:", f"{a}", f"id:{id(a_ref)}"))
print("{:<15}{:<20}{}".format("a_shallow_copy:", f"{a_shallowcopy}", f"id:{id(a_shallowcopy)}"))
print("{:<15}{:<20}{}".format("a_deepcopy:", f"{a_deepcopy}", f"id:{id(a_deepcopy)}"))

a[1][1] = 5
print("\nChange mutable part: a[1][1] = 5")
print("{:<20}{:<20}{}".format("a:", f"{a}", f"id:{id(a_ref)}"))
print("{:<20}{:<20}{}".format("a_shallow_copy:", f"{a_shallowcopy}", f"id:{id(a_shallowcopy)}"))
print("{:<20}{:<20}{}".format("a_deepcopy:", f"{a_deepcopy}", f"id:{id(a_deepcopy)}"))

print("\nCheck variable id at deep level")
print("{:<20}{:<20}{}".format("a[1][1]:", f"{a[1][1]}", f"id:{id(a[1][1])}"))
print("{:<20}{:<20}{}".format("a_shallowcopy[1][1]:", f"{a_shallowcopy[1][1]}", f"id:{id(a_shallowcopy[1][1])}"))
print("{:<20}{:<20}{}".format("a_deepcopy[1][1]:", f"{a_deepcopy[1][1]}", f"id:{id(a_deepcopy[1][1])}"))