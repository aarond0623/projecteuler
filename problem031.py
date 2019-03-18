"""
In England the currency is made up of pound, £, and pence, p, and there are
eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

1*£1 + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p

How many different ways can £2 be made using any number of coins?
"""


def coin_combos(coins, goal, combos=0, p=0, i=0):
    coins = sorted(coins)[::-1]
    for q in range(p, goal + 1, coins[i]):
        if coins[i] == coins[-1]:
            return combos + 1
        else:
            combos = coin_combos(coins, goal, combos, q, i+1)
    return combos


if __name__ == '__main__':
    print(coin_combos([200, 100, 50, 20, 10, 5, 2, 1], 200))
