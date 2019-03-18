from projecteuler import prime_sieve, is_prime


def prime_concats(n):
    """
    Generates a dictionary of primes less than n with a list of other primes
    that, when concatenated together, also form a prime.
    """
    primes = prime_sieve(n)
    prime_concats = {}
    for i in range(len(primes)):
        p = primes[i]
        prime_concats[p] = []
        for q in primes[i+1:]:
            if is_prime(int(str(p)+str(q))) and is_prime(int(str(q)+str(p))):
                prime_concats[p].append(q)
    prime_concat_list = {}
    for p in prime_concats:
        if prime_concats[p] != []:
            prime_concat_list[p] = prime_concats[p]
    return prime_concat_list

concat_list = []
prime_concats = prime_concats(10000)
for p in prime_concats:
    for q in prime_concats[p]:
        if q in prime_concats:
            for r in prime_concats[q]:
                if r in prime_concats and r in prime_concats[p]:
                    for s in prime_concats[r]:
                        if (s in prime_concats and
                                s in prime_concats[p] and
                                s in prime_concats[q]):
                            for t in prime_concats[s]:
                                if (t in prime_concats[p] and
                                        t in prime_concats[p] and
                                        t in prime_concats[q] and
                                        t in prime_concats[r]):
                                    concat_list.append([p, q, r, s, t])

Sum = float('inf')
record = None
for c in concat_list:
    if sum(c) < Sum:
        Sum = sum(c)
        record = c
print(record)
print(sum(record))
