number = int(input("Enter a number: "))
string_number = str(number)
reversed_string = string_number[::-1]
if string_number == reversed_string:
    print(number, "is a palindrome")
else:
    print(number, "is not a palindrome")
