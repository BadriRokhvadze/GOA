numbers = [4,2,14,0,5,6,-8]

min_number = numbers[0]

for number in numbers:
    if min_number > number:
        min_number = number

print(min_number)