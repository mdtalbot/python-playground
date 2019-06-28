def remaining_balance_calc(balance, annualInterestRate, monthlyPaymentRate):
  monthlyInterestRate = annualInterestRate / 12
  monthsRemaining = 12

  while monthsRemaining > 0:
      monthlyPayment = balance * monthlyPaymentRate
      unpaidBalance = balance - monthlyPayment
      balance = unpaidBalance + monthlyInterestRate * unpaidBalance
      monthsRemaining -= 1

  return("Remaining balance: " + str(round(balance, 2)))
