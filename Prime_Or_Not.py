def smallestDivisor(n):
    if n <= 3:
        return 1
    
    if (n % 2 == 0):
        return 2
 
    i = 3
    while(i * i <= n):
        if (n % i == 0):
            return i
        i += 2
 
    return 1