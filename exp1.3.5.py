#Simple function
def multiplication_tables():
    for i in range(2, 21):
        print(f"Multiplication table of {i}")
        for j in range(1, 11):
            print(f"{i} x {j} = {i*j}")
        print("\n")
multiplication_tables()
