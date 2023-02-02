d = input('take day:')
m = input('take month:')
y = input('take year:')

try:
    d = int(d)
    m = int(m)
    y = int(y)
except ValueError as e:
    print(e)

if m <= 0 or m > 12:
    raise ValueError('Month mus be from 1 to 12')

if m in (1, 3, 5, 7, 8, 10, 12):
    if d <= 0 or d > 31:
        raise ValueError('Day between 1 and 31')
elif m == 4 or m == 6 or m == 9 or m == 11:
    if d <= 0 or d > 30:
        raise ValueError(f'In month {m} between 1 and 30')
else:
    if y % 400 == 0:
        isLeapYear = True
    elif y % 100 == 0:
        isLeapYear = False
    elif y % 4 == 0:
        isLeapYear = True
    else:
        isLeapYear = False
    
    if isLeapYear:
        if d <= 0 or d > 29:
            raise ValueError(f'In month {m} between 1 and 29')
    else:
        if d <= 0 or d > 28:
            raise ValueError(f'In month {m} between 1 and 28')

print(f'{d}.{m}.{y}')

