"""
from : Hack sussex Coders Cup 2022
"""

def common_letters(s):
    count_dict = {}
    for letter in s:
        if letter in count_dict:
            count_dict[letter]+=1
        else:
            count_dict[letter]=1

    print(max(count_dict.values()))
    
if __name__ == "__main__":
    word = input("enter the word:")
    common_letters(word)