print("==========================")
print("Welcome to Holiday Planner")
print("==========================")

holiday_length = int(input("How many days long is your holidays: "))

holiday_activities = int(input("1 for the Beach, 2 for Camping or 3 for Resting or Random. 'This is for the first activity'"))

if holiday_activities is 1:
    days_at_beach = int(input("How many days are you going to stay at the beach: "))
    holiday_length = holiday_length - days_at_beach
    print(f"You have {holiday_length} days left to plan")
    if holiday_length >= 1:
        second_activity_1 = int(input("For the second activity, 1 for Camping or 2 for Resting or Random"))
        if second_activity_1 is 1:
            days_at_camping = int(input("How many days are you going to stay camping for: "))
            holiday_length = holiday_length - days_at_camping
            print(f"You have {holiday_length} days left to plan")
            if holiday_length >= 1:
                print("Last activity is Resting or Random")
                print("Spend the rest of the holidays doing this")
                print("=============================")
                print("This is your complete holiday")
                print("=============================")   
            else:
                days_random_or_resting = int(input("How many days are you going to be doing Resting or Random for: "))
                holiday_length = holiday_length - days_random_or_resting
                if holiday_length >= 1:
                    print("Last activity is Camping")
                    print("Spend the rest of the holidays doing this")
                    print("=============================")
                    print("This is your complete holiday")
                    print("=============================")
                else:
                    print("=========================")
                    print("NO MORE DAYS LEFT TO PLAN")
                    print("=========================")
    else:
        print("=========================")
        print("NO MORE DAYS LEFT TO PLAN")
        print("=========================")

if holiday_activities is 2:
    days_at_camping = int(input("How many days are you going to be Camping: "))
    holiday_length = holiday_length - days_at_camping
    print(f"You have {holiday_length} days left to plan")
    if holiday_length >= 1:
        second_activity = int(input("For the second activity, 1 for Resting or Random or 2 for Beach"))
        if second_activity is 1:
            days_at_camping = int(input("How many days are you going to be doing Resting or Random for: "))
            holiday_length = holiday_length - days_random_or_resting
            print(f"You have {holiday_length} days left to plan")
            if holiday_length >= 1:
                print("Last activity is Beach")
                print("Spend the rest of the holidays doing this")
                print("=============================")
                print("This is your complete holiday")
                print("=============================")   
            else:
                days_at_beach = int(input("How many days are you going to stay the beach: "))
                holiday_length = holiday_length - days_at_beach
                if holiday_length >= 1:
                    print("Last activity is Resting or Random")
                    print("Spend the rest of the holidays doing this")
                    print("=============================")
                    print("This is your complete holiday")
                    print("=============================")
                else:
                    print("=========================")
                    print("NO MORE DAYS LEFT TO PLAN")
                    print("=========================")
    else:
        print("=========================")
        print("NO MORE DAYS LEFT TO PLAN")
        print("=========================")

if holiday_activities is 3:
    days_random_or_resting = int(input("How many days are you going to be doing Resting or Random: "))
    holiday_length = holiday_length - days_random_or_resting
    print(f"You have {holiday_length} days left to plan")
    if holiday_length >= 1:
        second_activity = int(input("For the second activity, 1 for Beach or 2 for Camping"))
        if second_activity is 1:
            days_at_beach = int(input("How many days are you going to stay at the beach: "))
            holiday_length = holiday_length - days_at_beach
            print(f"You have {holiday_length} days left to plan")
            if holiday_length >= 1:
                print("Last activity is Camping")
                print("Spend the rest of the holidays doing this")
                print("=============================")
                print("This is your complete holiday")
                print("=============================")   
            else:
                days_at_camping = int(input("How many days are you going to stay camping: "))
                holiday_length = holiday_length - days_at_camping
                if holiday_length >= 1:
                    print("Last activity is Resting or Random")
                    print("Spend the rest of the holidays doing this")
                    print("=============================")
                    print("This is your complete holiday")
                    print("=============================")
                else:
                    print("=========================")
                    print("NO MORE DAYS LEFT TO PLAN")
                    print("=========================")
    else:
        print("=========================")
        print("NO MORE DAYS LEFT TO PLAN")
        print("=========================")