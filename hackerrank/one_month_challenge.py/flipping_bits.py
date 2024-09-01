"""

link: https://www.hackerrank.com/challenges/flipping-bits/problem
level: Easy
score: 40

"""

def flippingBits(n):
    # this number is (2**32)-1
    # unsigned integers given which is 32
    # 2**32 = 4294967296
    # to flip is to just minus 1
    THE_FLIPPING = 4294967295
    
    # ^ = bitwise XOR
    return n ^ THE_FLIPPING


if __name__ == "__main__":
    print(flippingBits(1))