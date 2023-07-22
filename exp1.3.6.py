def multiplication_table(num):
    print(f"Multiplication table of {num}")
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")
for i in range(2, 21):
    multiplication_table(i)
    print("\n")
