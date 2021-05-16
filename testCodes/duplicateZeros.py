def duplicateZeros(arr: list) -> None:
    l = len(arr)
    i = 0
    while i < l:
        if arr[i] == 0:
            arr.insert(i, 0)
            arr.pop()
            i += 1
        i += 1


if __name__ == "__main__":
    print(duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]))
