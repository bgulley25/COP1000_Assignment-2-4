# input statements
salary = 30000
numDependents = 6

# calculate taxes here
stateTax = (salary * .065)
federalTax = (salary * .28)
dependentDeduction = (salary * .15)
totalWitholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWitholding
# output statements
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependents: $" + str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
