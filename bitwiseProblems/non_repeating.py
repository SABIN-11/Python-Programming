# Problem: Given an array where every element occurs 3 times except one, which occurs once. Find that element using bitwise operators only.

test_list = [2, 2, 3, 3, 3, 5, 5, 5, 9, 9, 9]

def non_repeat(test_list):

    test_list.sort()
    i = 0
    while i < len(test_list):
        if i == len(test_list) - 2 or i == len(test_list) - 1:
            return test_list[i]
        if test_list[i] ^ test_list[i + 1] == 0 and test_list[i] ^ test_list[i + 2] == 0:
            i += 3
        else:
            return test_list[i]
        
print(f"{non_repeat(test_list)}")
