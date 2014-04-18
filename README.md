python-primes
=============

Example Usage:

    from primes import Primes
    
    Primes() #Infinite, lazily evaluated prime series
    Primes(7) #All prime numbers up to and including 7
    list(Primes(7)) == [2, 3, 5, 7]
    
Calling `Primes()` gives a new iterable of the primes series. It is recommended to call this once, store and reuse that value, as prime numbers are continually cached as they're evaluated.

Recommended Use:

    from primes import Primes
    
    primes = Primes()
    
    7 in primes == True
    4 in primes == False
