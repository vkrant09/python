number = int(input("Enter a number: "))
string_number = str(number)
num_digits = len(string_number)
sum = 0
for digit in string_number:
    sum += int(digit) ** num_digits
if sum == number:
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")
