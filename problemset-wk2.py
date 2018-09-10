
#determines how much of balance remains if paying only lowest monthly payment each month for a year.
monthlyInterestRate = annualInterestRate/12

for month in range(1,13):
    balance = (balance * (1-monthlyPaymentRate))*(1+monthlyInterestRate)

print("Remaining balance: " + str(round(balance,2)))



#Determines lowest monthly payment to pay off entire balance in a year. Uses increments.
principle = balance
monthlyInterestRate = annualInterestRate/12
lowestpayment = round((balance/12),-1)


while balance > 0:
    balance = principle
    for month in range(1,13):
        balance = (balance - lowestpayment)*(1+monthlyInterestRate)
    lowestpayment += 10
        

print("Lowest payment: " + str(int(lowestpayment-10)))


#Determines lowest monthly payment to pay off entire balance in a year. Uses bisection.
principle = balance
monthlyInterestRate = annualInterestRate/12
UB = (balance * (1+annualInterestRate)) / 12
LB = balance/12

guess = (UB + LB)/2


while round(balance, 1) != 0:
    balance = principle
    for month in range(1,13):
        balance = (balance - guess)*(1+monthlyInterestRate)
    if balance > 0:
        LB = guess
        guess = (UB + guess)/2
        
    elif balance < 0:
        UB = guess
        guess = (guess + LB)/2

        
if round(balance, 1)  == 0:
    print("Lowest payment: " + str(round(guess, 2)))