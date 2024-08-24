"""

link: https://www.hackerrank.com/challenges/sparse-arrays/problem
level: Medium
score: 25

"""

from typing import List
from collections import Counter

def matchingStrings(stringList: List[str], queries: List[str]) -> List[int]:
    counter = Counter(stringList)
    return [counter[query] for query in queries]


if __name__ == "__main__":
    stringList = ["abcde", "sdaklfj", "asdjf", "na", "basdn", "sdaklfj", "asdjf", "na", "asdjf", "na", "basdn", "sdaklfj", "asdjf"]
    queries = ["abcde","sdaklfj","asdjf","na","basdn"]
    print(matchingStrings(stringList, queries))