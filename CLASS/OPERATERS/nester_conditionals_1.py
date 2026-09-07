choice = int(input("What type of echile do you want. 1 is bike, 2 is car: "))

if choice == 1:
    bike_type = int(input("What bike type, 1 or 2: "))
    if bike_type == 1:
        print("Scooty - 80km/h")
    else:
        print("Mountain Bike - 40km/h")
elif choice == 2:
    car_type = int(input("What type of car do you want. 1 for sedan, 2 for SUV: "))
    if car_type == 1:
        print("Sedan - 5 seats")
    else:
        print("SUV - 7 seats")
else:
    print("INVALID OPTION")