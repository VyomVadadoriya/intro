print("=======================")
print("WELCOME TO RIDE BUILDER")
print("=======================")
print()

print("Pick your Vechile")
print(" 1 = Bike")
print(" 2 = Car")
print()

choice = int(input("Choose the vechile : "))
print()

if choice == 1:
    print(" 1 = Scooty")
    print(" 2 = Mountain Bike")
    bike_type = int(input("Which Bike do you want"))
    if bike_type == 1:
        print("You Picked  :  Scooty")
        print("Top Speed   :  80km/ph")
        print("Best For    :  City Roads")
    else:
        print("You Picked  :  Mountain Bike")
        print("Top Speed   :  40km/ph")
        print("Best For    :  Off-road Trails")

elif choice == 2:
    print(" 1 = Sedan")
    print(" 2 = SUV")
    car_type = int(input("Which Car do you want"))
    if car_type == 1:
        print("You Picked  :  Sedan")
        print("Seats       :  5 passengers")
        print("Best For    :  Family Trips")
    else:
        print("You Picked  :  SUV")
        print("Seats       :  7 passengers")
        print("Best For    :  Off-road Adventures")
else:
    print("THAT IS NOT A VALID OPTION")

print()
print("=========================")
print("Your custom ride is ready")
print("!!!!Enjoy your journey!!!")
print("=========================")