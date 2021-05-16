def sortedSquares(nums: list) -> list:
    n = len(nums)
    new_num = []
    i = 0
    j = n - 1
    while i < n or j >= 0:

        a = abs(nums[i])
        z = abs(nums[j])

        if i == j:
            new_num.append(a * a)
            break

        while a >= z and i != j:
            new_num.append(a * a)
            i += 1
            a = abs(nums[i])

        while z >= a and i != j:
            new_num.append(z * z)
            j -= 1
            z = abs(nums[j])
    return new_num[::-1]


if __name__ == "__main__":
    print(sortedSquares([-4, -1, 0, 1, 3, 10]))
