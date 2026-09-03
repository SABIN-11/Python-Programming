# Enter the row size for the pattern: 5
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

# === Code Execution Successful ===

n_row = int(input("Enter the row size for the pattern: "))

for i in range(n_row, 0, -1):
    for j in range(i):
        print("* ", end = "")
    print()