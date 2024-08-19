"""

link: From Hackerrank grid Challenge
level: basic
score: 0

Comment:

Time complexity: O(n)

Space complexity: O(1)

Language: Java

Approach:

We loop from right to left. 
If a person's sticker minus their position is greater than 2, print "Too chaotic" and return. 
That is, the person has bribed more than two people. 
Be careful, most programming languages have indices starting from 0. 

Java for intance, you will have if(sticker-i-1>2) as opposed to if(sticker-i>2) where i is the index

One key information needed to solve this problem in linear time is the fact that no person can bribe more than twice. 
This means that, as long as we do not print "Too chaotic", 
a person could have only bribed the two people on his right with stickers less than theirs. 
Or in other words, for every person at index i with a sticker p, 
there can only be a maximum of 2 persons to their right with stickers less than p. 
So, while looping through our collection from right to left, we can keep track of the two least values (stickers) encountered. 
These values are stored as min1 and min2 in my code.

Now, in our loop, for each sticker, we check to see if it is greater than our min1 and min2 values 
and in both situations increment our counter for minimum number of bribes which should be initially set to 0.

After that, we check to see if our current sticker is a possible min1 or min2 value and update them accordingly.

At the end of the loop, our counter for minimum number of bribes will be updated appropriately.

"""

import sys

def minimumBribesOld(q):
    bribes = 0
    for i, pos in enumerate(q):
        diff = pos - (i+1)
        if diff > 2:
            return "Too chaotic"
        elif diff > 0:
            bribes += diff
    return bribes

def minimumBribes(q):
    bribes = 0
    min1, min2 = sys.maxsize, sys.maxsize
    n = len(q)
    for i in range(n-1, -1, -1):
        sticker = q[i]
        if sticker - i - 1 > 2:
            print("Too chaotic")
            return
        
        if sticker > min1:
            bribes += 1
            
        if sticker > min2:
            bribes += 1
            
        if (sticker < min1) or (sticker < min2):
            if min1 > min2:
                min1 = sticker
            else:
                min2 = sticker
        # print(f"sticker: {sticker}; min1: {min1}; min2: {min2}; bribes: {bribes}")
                
    print(bribes)
    


if __name__ == "__main__":
    print(minimumBribes([1, 2, 5, 3, 7, 8, 6, 4]))