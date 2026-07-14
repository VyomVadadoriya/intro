name = "Penguin"
age = 15
is_student = True
weight = 38.5

print("Name :", name)
print("Data type for Name is", type(name))

print("Age :", age)
print("Data type for Age is", type(age))

print("Student :", is_student)
print("Data type for is_student is", type(is_student))

print("Weight :", weight)
print("Data type for Weight is", type(weight))

print("\nAfter Type Casting....")
age = str(age)
print(age)
print("Data type of Age is", type(age))
weight = int(weight)
print(weight)
print("Data type of weight is", type(weight))
