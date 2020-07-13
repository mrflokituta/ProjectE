def lpf(num):
    array = []
    iteration = 2
    while iteration * iteration <= num:
        if num%iteration:
            iteration += 1
        else:
            num //= iteration
            array.append(iteration)
    if num > 1:
        array.append(num)
    return(array[-1])

print(lpf(600851475143))
