"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    if number_of_primes <= 0:
        raise ValueError
    for x in range(0, 100):
            if x == 0 or x == 1:
                continue
            else:
                for y in range(2, int(x)):
                    if x % y == 0:
                        break
                    elif len(list) >= number_of_primes:
                        break
                else:
                    list.append(x)
    return list