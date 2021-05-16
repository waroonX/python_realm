def removeElement(nums: list, val: int) -> int:
    l = len(nums)
    m = l
    i = 0
    total = 0

    while i < l and m >= 0:
        while m >= 0:
            m -= 1
            if nums[m] != val:
                break
            elif m >= i:
                total += 1

        while i < l:
            if nums[i] == val:
                nums[i] = nums[m]
                if i <= m:
                    total += 1
                break
            i += 1
    nums = nums[: l - total]
    return l - total


if __name__ == "__main__":
    print(removeElement([2, 2, 1, 2, 3], 2))
