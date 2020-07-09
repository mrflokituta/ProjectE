# projecteuler.net
# ID:1

# Find the sum off all the multiples of 3
# and 5 below 1000

def multiple(x): a = [] for i in range(x): 
        if i%3 == 0 or i%5 == 0:
            a.append(i)
    return sum(a)
print(multiple(1000))
