def modd(a, b, mod):
    
    # (base_a^exp_b)%mod
    result = 1
    while b> 0: 
        if b%2 == 1:
            result= (result *a) % mod
        a = (a * a) % mod
        b //=2
    return result

a, b = map(int, input().split())
result = modd(a, b, 107)
print(result)
            