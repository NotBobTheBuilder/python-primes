from itertools import count

class Primes(object):
    cached = [2]
    def __init__(self, stop=None):
        self.stop = stop or float('inf')

    def __iter__(self):
        for prime in Primes.cached:
            yield prime

        start = Primes.cached[-1]
        for num in count(start + 1, 2):
            if num > self.stop:
                break

            if not any(num % p == 0 for p in Primes.cached):
                Primes.cached.append(num)
                yield num
