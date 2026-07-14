print("Enter marks from 5 subjects")

markone = int(input())
marktwo = int(input())
markthree = int(input())
markfour = int(input())
markfive = int(input())

total = markone + marktwo + markthree + markfour + markfive
average = int(total / 5)

validrange = range(0, 101)

if average not in validrange:
    print("Invalid inputs")
elif average in range(91, 101):
    print("You have an A1")
elif average in range(81, 91):
    print("You have an A2")
elif average in range(71, 81):
    print("You have a B1")
elif average in range(61, 71):
    print("You have a B2")
elif average in range(51, 61):
    print("You have a C1")
elif average in range(41, 51):
    print("You have a C2")
elif average in range(33, 41):
    print("You have a D")
elif average in range(21, 33):
    print("You have an E1")
elif average in range(0, 21):
    print("You have an E2")