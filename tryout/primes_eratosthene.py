def get_least_primes_linear(n):
    lp = [0] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        print(f'old lp[{i}] = {lp[i]}', end=' | ')
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
            print(f'i={i} new lp[{i}]={lp[i]} primes={primes}', end=' | ')
        for p in primes:
            x = p * i
            if (p > lp[i]) or (x > n):
                break
            lp[x] = p
            print(f'x={x} lp[{x}]={lp[x]}', end=' ')
        print('')
    return primes, lp


print(get_least_primes_linear(17))
