def findMaxConsecutiveOnes(nums: list) -> int:
    count = 0

    max_count = 0
    for n in nums:
        if n == 1:
            count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count
    return max_count


if __name__ == "__main__":
    print(findMaxConsecutiveOnes([1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1]))
