def multiplication_table(num):
    table = ""
    table += f"Multiplication table of {num}\n"
    for i in range(1, 11):
        table += f"{num} x {i} = {num*i}\n"
    return table
for i in range(2, 21):
    table = multiplication_table(i)
    print(table)
    print("\n")
