
# largest and smallest number from the list

li = list(map(int, input().split()))

l = li[0]
s = li[0]

for i in range(1, len(li)):
    if li[i] > l:
        l = li[i]
    if li[i] < s:
        s = li[i]

print(f"Greatest number is {l}")
print(f"Smallest number is {s}")