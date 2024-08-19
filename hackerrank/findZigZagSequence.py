"""
This is a mock test

"""

def findZigZagSequence(a, n):
    a.sort()
    mid = n//2
    a[mid], a[n-1] = a[n-1], a[mid]
    # 1 2 5 4 3
    st = mid + 1
    ed = n - 2
    while(st < ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range(n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return


if __name__ == "__main__":
    findZigZagSequence([2, 3, 5, 1, 4], 5)