def sortedSquares(nums: list) -> list:
    n = len(nums)
    new_num = []
    i = 0
    j = n - 1
    while i < n and j >= 0 and i <= j:
        a = abs(nums[i])
        z = abs(nums[j])

        if a < z:
            new_num.append(z * z)
            j -= 1
        else:
            new_num.append(a * a)
            i += 1
    return new_num[::-1]


if __name__ == "__main__":
    print(sortedSquares([-7, -3, 2, 3, 11]))
