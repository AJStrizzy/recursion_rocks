# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨`

# This function returns an array of all possible outcomes from flipping a coin N times.
# Input type: Integer 
# H stands for Heads and T stands for tails
# Represent the two outcomes of each flip as "H" or "T"

def coin_flips(n):
    result = []
    def add_flips(n, result, current):
        if n == 1:
           result.append(current + 'H')
           result.append(current + 'T')
        else:
            add_flips(n - 1, result, current + 'H' )     
            add_flips(n - 1, result, current + 'T' )     

    add_flips(n,result, '')
    return result

print(coin_flips(3))    

