# multiplication table

def mul_table(num: int) -> None:
    for i in range(1, 11):
        print(F"{num} x {i} = {num * i}")

num = int(input("Enter a number whose multiplication table is needed: "))
mul_table(num)