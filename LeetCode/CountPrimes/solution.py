class Solution:
    def isPrime(self, n) -> bool:
        """
            Checks if the given number n is prime or not
        """
        # Sieve Method
        primes = [True for i in range(n)]
     
        p = 2
        while p * p < n:
            # if prime[p] is True => number p is prime
            
            if primes[p]:    
                # update all multiples of p
                for i in range(p * p, n, p):
                    primes[i] = False
            p += 1
        return primes

    def countPrimes(self, n: int) -> int:
        # handle the basic case of 0 and 1
        if n in (0, 1): return 0
    
        # else get the primes list
        primes = self.isPrime(n)
        # print(primes)

        # spit the count of True
        return primes[2:].count(True)