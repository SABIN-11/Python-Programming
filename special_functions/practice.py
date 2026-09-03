# nums = [3, 7, 2, 9, 4] result = ___ print(result) # [6, 14, 4, 18, 8]

# nums = [3, 7, 2, 9, 4]
# result = list(map(lambda x: x * 2, nums))
# print(result)

# nums = [1, 2, 3, 4, 5, 6, 7, 8] odds = ___ print(odds) # [1, 3, 5, 7]

# nums = [i for i in range(1, 9)]
# odds = list(filter(lambda x: x % 2 != 0, nums))
# print(odds)

# words = ["cat", "elephant", "ox", "tiger", "bee"] long_words = ___ print(long_words) 
# ['elephant', 'tiger']
# words = ["cat", "elephant", "ox", "tiger", "bee"]
# long_words = list(filter(lambda x: len(x) > 4, words))
# print(long_words)

# temps_c = [25, -3, 100, -10, 37, 0] valid = ___ # step 1: filter negatives kelvin = ___ # 
# step 2: convert to Kelvin print(kelvin) # [298, 373, 310, 273]

# temps_c = [25, -3, 100, -10, 37, 0]
# valid_temps = list(filter(lambda x: x >= 0, temps_c))
# kelvin = list(map(lambda x: x + 273.15, valid_temps))
# print(kelvin)

# Write a lambda that takes two arguments m and v, and 
# returns kinetic energy: KE = 0.5 × m × v². Test it with mass=10, velocity=3.

# KE = lambda m,v: 0.5 * m * v**2
# print(F"{KE(10,3)}J")

# gravity = { "Mercury": 3.7, "Venus": 8.9, "Earth": 9.8, "Mars": 3.7, "Jupiter": 24.8, "Saturn": 11.2 } 
# strong = ___ print(strong) # {'Jupiter': 24.8, 'Saturn': 11.2}
acc_gravity = { "Mercury": 3.7, "Venus": 8.9, "Earth": 9.8, "Mars": 3.7, "Jupiter": 24.8, "Saturn": 11.2 } 
strong = dict(filter(lambda item: item[1] > 9.8, acc_gravity.items()))
# acc_gravity.items() gives us dict_object iterable and then each member of that iterable goes to 
# lambda function
print(strong)
# strong = list(filter(lambda x: acc_gravity[x] > 9.8, acc_gravity.keys()))
# di = {}
# for key in strong:
#     di[key] = acc_gravity[key]

# print(di)




