"""

link: From Hackerrank grid Challenge
level: intermediate
score: 0


"""

import sys

def truckTour(petrolpumps):
    total = 0
    min_i = -1
    for i, (petrol, distance) in enumerate(petrolpumps):
        total += (petrol - distance)
        if total < 0:
            total = 0
            min_i = i+1
    return min_i
    
if __name__ == "__main__":
    petrolpumps = [[1, 5], [10, 3], [3,4]]
    print(truckTour(petrolpumps))