
def taxCompute(money):
    if money <= 250000:
        pay = money
    elif money > 250000 and money <= 400000:
        pay = (money - 250000) * 0.15
    elif money > 400000 and money <= 800000:
        pay = 22500 + (money - 400000) * 0.2
    elif money > 800000 and money <= 2000000:
        pay = 102500 + (money - 800000) * 0.25
    elif money > 2000000 and money <= 8000000:
        pay = 402500 + (money - 2000000) * 0.3
    elif money > 8000000:
        pay = 2202500 + (money - 8000000) * 0.35
    else:
        print("========== INVALID INPUT ==========")
    
    return (pay)


income = float(input("Enter your monthly income: "))
annual = income * 12
taxRate = taxCompute(annual)
monthlyTax = taxRate/12

print("========== RECEIPT ==========")
print("Monthly Income: {}" .format(income))
print("Annual Income: {}" .format(annual))
print("Annual Tax Rate: {}" .format(taxRate))
print("Monthly Tax Rate: {}" .format(monthlyTax))
