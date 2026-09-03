# Enter the row size for the pattern: 5
#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 

# === Code Execution Successful ===

n_row = int(input("Enter the row size for the pattern: "))

for i in range(1, n_row + 1):
    for j in range(1, n_row - i + 1):
        print(" ", end = "")

    for k in range(1, 2*i):
        print("*", end = "")

    print()