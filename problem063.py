"""Project Euler, Problem 63"""

count = 0
power = 1
while (10 ** (power - 1)) ** (1 / power) <= 9:
    for n in range(1, 10):
        if len(str(n ** power)) == power:
            count += 1
        elif len(str(n ** power)) > power:
            break
    power += 1

print(count)
