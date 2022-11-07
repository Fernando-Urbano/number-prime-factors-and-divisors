import itertools as it
import pandas as pd
import numpy as np
import re
import decimal
import math
import sympy
import collections


class NumberDNA:
  def __init__(self, number, calculate_prime_factors=True, calculate_divisors=None):
    if number > 10 ** 10 and calculate_divisors is None:
        calculate_divisors = False
    if number <= 10 ** 10 and calculate_divisors is None:
        calculate_divisors = True
    self.calculate_divisors = calculate_divisors
    self.calculate_prime_factors = calculate_prime_factors
    self.number = number
    if self.number >= 10 ** 15 and calculate_divisors:
        print(
            "Number is too big. The result might take a while to be calculated.\n"
            "If you only need 'unit digit' or 'prime factors', use 'calculate_divisors=False'."
        )
    if calculate_prime_factors:
        self.prime_factors = []
    else:
        self.prime_factors = "Assign 'calculate_prime_factors=True' to verify prime factors."
    if calculate_divisors:
        self.divisors = [1, self.number]
    else:
        self.divisors = "Assign 'calculate_divisors=True' to verify divisors."
    if calculate_prime_factors:
        # Prime Factors ----
        while number % 2 == 0:  
            self.prime_factors.append(2) 
            number = number / 2  
        for i in range(3, int(math.sqrt(number)) + 1, 2):  
            while number % i == 0:  
                self.prime_factors.append(i)
                number = number / i
        if number > 2:  
            self.prime_factors.append(number)
        self.prime_factors.sort()
    if calculate_divisors:
        # Divisors ----
        for d in range(2, int(math.sqrt(self.number)) + 1):
            if self.number % d == 0:
                self.divisors.append(d)
                self.divisors.append(self.number / d)
        self.divisors.sort()

        
  def __repr__(self):
    partial_result = "".join([
        "Number:\n", str(decimal.Decimal(self.number)),
        ";\n15 first digits: ", str(decimal.Decimal(self.number))[-15:],
    ])
    if self.calculate_divisors:
        divisors_result = "".join([
            "\n\nDivisors (Qt: ", str(len(self.divisors)),
            "; Qt without repetiton: ", str(len(set(self.divisors))),
            "):\n",
            ", ".join([str(int(d)) for d in self.divisors])
        ])
    else:
        divisors_result = "\n\nDivisors: assign 'calculate_divisors=True' to verify divisors."
    if self.calculate_prime_factors:
        prime_factors_str = [
            "".join([str(t[0]), " (qt: ", str(t[1]), ")"]) for t in [
                a for a in collections.Counter(self.prime_factors).items()
            ]
        ]
        # n_div = 1
        # for p in [p + 1 for p in list(collections.Counter(self.prime_factors).values())]:
        #     n_div *= math.factorial(p)
        prime_factors_result = "".join([
            ";\n\nPrime Factors (Qt: ", str(len(self.prime_factors)), "):\n- ",
            "\n- ".join(prime_factors_str),
            # "\n\nNº de Divisores: ", str(n_div)
        ])
    else:
        prime_factors_result = "\n\nPrime Factors: assign 'calculate_prime_factors=True' to verify prime factors."
    result = "".join([partial_result, prime_factors_result, divisors_result])
    return result
    
