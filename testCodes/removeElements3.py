def removeElement(nums: list, val: int) -> int:
    last_index = len(nums) - 1
    for index in range(last_index, -1, -1):
        if nums[index] == val:
            nums[index], nums[last_index] = nums[last_index], nums[index]
            last_index -= 1
    print(nums)
    return last_index + 1


if __name__ == "__main__":
    print(removeElement([2, 2, 1, 2, 3], 2))
