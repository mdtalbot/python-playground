def smallest_monthly_payment(balance, annualInterestRate):
  monthlyInterestRate = annualInterestRate/12


  balanceStorage = balance
  lo = balance/12
  hi = (balance*(1+monthlyInterestRate)**12)/12
  epsilon = .01

  guess = (lo + hi)/2

  while True:
    for month in range(1, 13):
        balance = balance - guess
        balance = balance + (monthlyInterestRate*balance)

    if balance > 0 and balance > epsilon:
        lo = guess
        balance = balanceStorage
    elif balance < 0 and balance < -epsilon:
        hi = guess
        balance = balanceStorage
    else:
        return ('Lowest payment: ', str(round(guess, 2)))
        break

    guess = (lo + hi)/2
