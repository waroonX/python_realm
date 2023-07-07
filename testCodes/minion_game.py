
VOWELS = "AEIOU"

def calc_score(string, main_str):
    l = len(string)
    score = 0
    for i in range(0, len(main_str)-l+1):
        if string == main_str[i: i+l]:
            score += 1
    return score

def do_work(string, main_str, main_dict={}):
    if not string or string in main_dict:
        return 0, 0, main_dict
    score = calc_score(string, main_str)
    act_score = (0, score) if string[0] in VOWELS else (score, 0)
    main_dict[string] = act_score
    l_score1, l_score2, main_dict = do_work(string[:-1], main_str, main_dict)
    r_score1, r_score2, main_dict = do_work(string[1:], main_str, main_dict)
    return act_score[0]+l_score1+r_score1, act_score[1]+l_score2+r_score2, main_dict
    

# def minion_game(string, main_dict={}):
#     p1, p2, _ = do_work(string, string)
#     if p1 == p2:
#         print("Draw")
#     elif p1 > p2:
#         print(f"Stuart {p1}")
#     else:
#         print(f"Kevin {p2}")

def minion_game(string):
    vowels = "AEIOU"
    stuart_consoant = 0
    kevin_vowel = 0

    for index, letter in enumerate(string):
        # print(letter, len(string) - index)
        if letter in vowels:
            kevin_vowel += len(string) - index
        else:
            stuart_consoant += len(string) - index

    if stuart_consoant > kevin_vowel:
        print('Stuart', stuart_consoant)

    if stuart_consoant == kevin_vowel:
        print('Draw')

    if stuart_consoant < kevin_vowel:
        print('Kevin', kevin_vowel)
    

if __name__ == '__main__':
    s = "BANANA"
    minion_game(s)
    # print(calc_score("ANA", "BANANA"))