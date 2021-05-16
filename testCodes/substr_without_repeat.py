def lengthOfLongestSubstring(s: str) -> int:
    count = 0
    max_count = 0

    non_dup_char_list = []
    for c in s:
        if c not in non_dup_char_list:
            non_dup_char_list.append(c)
            count += 1
        else:
            non_dup_char_list.append(c)
            non_dup_char_list = non_dup_char_list[non_dup_char_list.index(c) + 1 :]
            count = len(non_dup_char_list)
        if count > max_count:
            max_count = count
    return max_count


if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb"))
