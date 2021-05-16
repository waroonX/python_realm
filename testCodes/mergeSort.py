def merge(nums1: list, m: int, nums2: list, n: int) -> None:
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    nums1[:n] = nums2[:n]
    print(nums1)


if __name__ == "__main__":
    print(merge(nums1=[0], m=0, nums2=[1], n=1))
