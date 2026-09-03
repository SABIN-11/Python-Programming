# join() method joins the elements of an iterable
# join() method but manually

iterable = []

numOfElements = int(input('How many elements are needed in the list? '))
print('Enter elemens in a list: ')

for i in range (1, numOfElements + 1):
    items = input(f"Enter Item {i}: ")
    iterable.append(items)

separator = input("Enter the separator: ")

def joinMethod(iterable, separator):

    result_string = ''
    for i in range (len(iterable)):
        result_string += iterable[i] + separator

    return result_string[:len(result_string) - 1]

print(joinMethod(iterable, separator))

# print(','.join(iterable))




