# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the largest number in a given array.

def find_max(L):
    if len(L) == 1:
        return L[0]
    else:
        return max(L[0],find_max(L[1:]))

print(find_max([1, 4, 45, 6, -50, 10, 2]))
# => 45