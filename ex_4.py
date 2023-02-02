deposit = 100
percent = 0.05
period = 10

for y in range(1, period+1):
    new_deposit = (deposit * percent) + deposit
    deposit = new_deposit

print(deposit)