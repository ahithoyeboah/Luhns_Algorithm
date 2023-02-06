number = input('Please enter credit card number: ')
num_list = [int(char) for char in number]
num_len = len(num_list)

num_list_rev = num_list[::-1]
double = 0
single = 0
for i in range(0, num_len):
    if i % 2 != 0:
        if 2 * num_list_rev[i] > 9:
            double = double + 2 * num_list_rev[i] - 9
        else:
            double = double + 2 * num_list_rev[i]
    else:
        single = single + num_list_rev[i]

if (double+single) % 10 == 0:
    print(f'{number} is a valid credit card number.')
else:
    print(f'{number} is not a valid credit card number.')
