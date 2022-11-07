# Number DNA: Prime Factors and Divisors
This repository presents a class to calculate number factors and divisors.
```
NumberDNA(48 ** 25)
```
Result:
```
Number:
1074065914326960788028149801831911881965568;
15 first digits: 831911881965568;

Prime Factors (Qt: 125):
- 2 (qt: 100)
- 3 (qt: 25)

Divisors: assign 'calculate_divisors=True' to verify divisors.
```
To calculate number divisors as well add `calculate_divisors=True`. If the number is bigger than ${10}^{15}$, a message will be shown warning that the result might take a while to be calculated.
```
NumberDNA(24 ** 4, calculate_divisors=True)
```
Result:
```
Number:
331776;
15 first digits: 331776;

Prime Factors (Qt: 16):
- 2 (qt: 12)
- 3 (qt: 4)

Divisors (Qt: 66; Qt without repetiton: 65):
1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32, 36, 48, 54, 64, 72, 81, 96, 108, 128, 144, 162, 192, 216, 256, 288, 324, 384, 432, 512, 576, 576, 648, 768, 864, 1024, 1152, 1296, 1536, 1728, 2048, 2304, 2592, 3072, 3456, 4096, 4608, 5184, 6144, 6912, 9216, 10368, 12288, 13824, 18432, 20736, 27648, 36864, 41472, 55296, 82944, 110592, 165888, 331776
```
To view only the divisors:
```
NumberDNA(40, calculate_divisors=True).divisors
```
To view only the prime factors:
```
NumberDNA(40).prime_factors
```
