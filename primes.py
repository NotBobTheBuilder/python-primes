from itertools import count

class Primes(object):
    cached = [2]
    def __init__(self, stop=None):
        self.stop = stop or float('inf')

    def __iter__(self):
        for prime in Primes.cached:
            if prime > self.stop:
                return
            yield prime

        start = Primes.cached[-1]
        for num in count(start + 1, 2):
            if num > self.stop:
                return

            if num in self:
                Primes.cached.append(num)
                yield num

    def __contains__(self, num):
        stop = (num ** 0.5)
        for prime in self:
            if prime > stop:
                return True

            if num % prime == 0:
                return False
