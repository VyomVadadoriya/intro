def cube(number):
    return number*number*number
def cube_cube(number):
    return cube(number)*cube(number)*cube(number)

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False

cubed_no = int(input("What number do you want to be cubed twice: "))

print(cube(cubed_no))
print(cube_cube(cubed_no))