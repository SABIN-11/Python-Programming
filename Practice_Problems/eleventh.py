# Enter the row size for the pattern: 5
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

# === Code Execution Successful ===

n_row = int(input("Enter the row size for the pattern: "))
for i in range(n_row):
    for j in range(i+1):
        print("*  ", end = "")
    print()