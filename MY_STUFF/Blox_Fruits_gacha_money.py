level = int(input("Level: "))



if level <= 49:
    print("Unable to roll fruit \n===== LEVEL 50 NEEDED =====")
else:
    proper_lv = level - 50
    money = proper_lv * 150
    cost = money + 25000
    print(f"You need {cost} to roll")