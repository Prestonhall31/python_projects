'''
Task :
Given a List [] of n integers , find minimum mumber to be inserted in a list, so that sum of all 
elements of list should equal the closest prime number .

Notes
List size is at least 2 .

List's numbers will only positives (n > 0) .

Repeatition of numbers in the list could occur .

The newer list's sum should equal the closest prime number .
'''
def is_prime(num):
    if num > 1: 
        for i in range(2, num//2): 
            if (num % i) == 0: 
                return False
                break
        else: 
            return True
        
    else: 
        return False


def minimum_number(numbers):
    sums = sum(numbers)
    if is_prime(sums):
        return 0
    prime = sums
    while not is_prime(prime):
        prime += 1
    return prime - sums

    