user_input = input('Take string:')

#escape

if not user_input:
    print('-----')

count_ch = 0

for ch in user_input:
    # if ch == 'a':
    #     count_ch += 1
    print(ord(ch))
    
print(f'{count_ch}')