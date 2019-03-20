"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
and concatening them in any order the result will always be prime. For example,
taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes,
792, represents the lowest sum of a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
"""

from problem003 import prime_sieve, is_prime


def prime_concats(n):
    """
    Generates a dictionary of primes less than n with a list of other primes
    that, when concatenated together, also form a prime.
    """
    primes = prime_sieve(n)
    prime_dict = {}
    for i in range(len(primes)):
        p = primes[i]
        prime_dict[p] = []
        for q in primes[i+1:]:
            if is_prime(int(str(p)+str(q))) and is_prime(int(str(q)+str(p))):
                prime_dict[p].append(q)
    prime_concat_list = {}
    for p in prime_dict:
        if prime_dict[p] != []:
            prime_concat_list[p] = prime_dict[p]
    return prime_concat_list


def main():
    concat_list = []
    prime_dict = prime_concats(10000)
    for p in prime_dict:
        for q in prime_dict[p]:
            if q in prime_dict:
                for r in prime_dict[q]:
                    if r in prime_dict and r in prime_dict[p]:
                        for s in prime_dict[r]:
                            if (s in prime_dict and
                                s in prime_dict[p] and
                                s in prime_dict[q]):
                                for t in prime_dict[s]:
                                    if (t in prime_dict[p] and
                                        t in prime_dict[q] and
                                        t in prime_dict[r]):
                                        concat_list.append([p, q, r, s, t])
    return min([sum(x) for x in concat_list])

if __name__ == '__main__':
    print(main())
