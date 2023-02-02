side1 = float(input('First side:'))
side2 = float(input('Second side:'))
side3 = float(input('Third side:'))

if side1 == side2 and side2 == side3:
    print('Рівносторонній')
elif side1 == side2 or side2 == side3 or side3 == side1:
    print('Рівнобедрений')
else:
    print('Різносторонній')