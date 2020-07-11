# projecteuler.net
# ID:2

# By considering the terms in the Fibonacci
#  sequence whose values do not exceed four
# million, find the sum of the even-valued terms.

def even_fib(w):
    bool = True
    array = [1,2]
    final = []
    while bool:
        i = len(array)
        x = array[i-2]+array[i-1]
        if x > w:
            bool = False
        else:
            array.append(x)
    for number in array:
        if number%2 == 0:
            final.append(number)
    return sum(final)

print(even_fib(4000000))
