# def findDuplicates(self, arr):
#     # code here
#     d = {}
    
#     for i in range(len(arr)):
#         if arr[i] in d:
#             d[arr[i]] += 1
#         else:
#             d[arr[i]] = 1
            
#     return [i for i in d.keys() if d[i] == 2]