
# 1. Find prime factorization of a given number. 
# function should take in one parameter, integer
# Returns a list containing all of its prime factors


def get_prime_factors(int):
    factors = list()
    divisor = 2
    while(divisor <= int):
        if (int % divisor) == 0:
            factors.append(divisor)
            int = int/divisor
        else: 
            divisor += 1
    return factors 

get_prime_factors(630)

