# Dutch National Flag (DNF) algorithm

# def sort012(self, arr):
#     # code here
#     size = len(arr)
#     low = 0
#     mid = 0
#     high = size - 1
    
#     while mid <= high:
#         if arr[mid] == 0:
#             arr[low], arr[mid] = arr[mid], arr[low]
#             mid += 1
#             low += 1
#         elif arr[mid] == 1:
#             mid += 1
#         else:
#             arr[mid], arr[high] = arr[high], arr[mid]
#             high -= 1
            
#     return arr