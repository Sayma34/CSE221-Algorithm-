def mod_drift(b, e, mod):
    result = 1
    while e> 0:
        if e %2 == 1:
            result = (result * b)% mod
        b = (b * b) % mod
        e //= 2
    return result

def sol():
    a, n, m = map(int, input().split())
    if a == 1:
        print(n%m)
        return
    
    sum = (mod_drift(a,n+1,m) - a+m) %m
    inv = mod_drift(a-1, m-2, m)
    res = (sum * inv)% m
    print(res)
    
T = int(input())
for i in range(T):
    sol()
            