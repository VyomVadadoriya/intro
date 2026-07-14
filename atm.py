Amount = int(input('What is the amount you want to withdraw: '))

Hundreds = Amount//100
Fifty = (Amount%100)//50
Tens = ((Amount%100)%50)//10

print(f"Number of Hundreds:  {Hundreds} \n Number of Fifties:  {Fifty} \n Number of Tens:  {Tens}")