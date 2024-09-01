def findNumbers(nums: list) -> int:
    return len([n for n in nums if len(str(n)) % 2 == 0])


if __name__ == "__main__":
    print(findNumbers([12, 345, 2, 6, 7896]))
