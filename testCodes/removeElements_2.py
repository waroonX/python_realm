def removeElement(nums: list, val: int) -> int:
    n = len(nums)
    i = 0
    while i < n:
        if nums[i] == val:
            nums[i] = nums[n - 1]
            n -= 1
        else:
            i += 1

    print(nums[:n])
    print(n)


if __name__ == "__main__":
    print(removeElement([2, 2, 1, 2, 2], 2))
