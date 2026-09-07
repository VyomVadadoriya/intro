hw_completed = 0

hw_assigned = int(input("How much homework do you have to do(Max 5): "))

if hw_assigned == 1:
    Homework_1 = str(input("First homework: "))
elif hw_assigned == 2:
    Homework_1 = str(input("First homework: "))
    Homework_2 = str(input("Second homework: "))
elif hw_assigned == 3:
    Homework_1 = str(input("First homework: "))
    Homework_2 = str(input("Second homework: "))
    homework_3 = str(input("Third homework: "))
elif hw_assigned == 4:
    Homework_1 = str(input("First homework: "))
    Homework_2 = str(input("Second homework: "))
    homework_3 = str(input("Third homework: "))
    homework_4 = str(input("Fourth homework: "))
elif hw_assigned == 5:
    Homework_1 = str(input("First homework: "))
    Homework_2 = str(input("Second homework: "))
    homework_3 = str(input("Third homework: "))
    homework_4 = str(input("Fourth homework: "))
    homework_5 = str(input("Fifth homework: "))
else:
    print("==========================")
    print("INVALID AMOUNT OF HOMEWORK")
    print("==========================")

while hw_completed <= hw_assigned:
    print(f"Start : {Homework_1}")
    Done = str(input("Done Y/n: "))
    if Done == 'Y':
        hw_completed += 1
        print(f"Start : {Homework_2}")
        Done = str(input("Done Y/n: "))
        if Done == 'Y':
            hw_completed += 1
            print(f"Start : {homework_3}")
            Done = str(input("Done Y/n: "))
            if Done == 'Y':
                hw_completed += 1
                print(f"Start : {homework_4}")
                Done = str(input("Done Y/n: "))
                if Done == 'Y':
                    hw_completed += 1
                    print(f"Start : {homework_5}")
                    Done = str(input("Done Y/n: "))
                elif Done == 'End':
                    hw_completed += 6
                else:
                    print("Finish and come back")
            elif Done == 'End':
                hw_completed += 6
            else:
                print("Finish and come back")
    elif Done == 'End':
        hw_completed += 6
    else:
        print("Finish and come back")
else:
    print("====================")
    print("===== ALL DONE =====")
    print("====================")
    
