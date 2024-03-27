from typing import List


def sort(arr: List[int]):
    n = len(arr)
    res = [0 for _ in range(n)]
    l, r = 0, n - 1
    i = r

    while l <= r:
        if arr[r] > arr[l]:
            res[i] = arr[r]
            r -= 1
        else:
            res[i] = arr[l]
            l += 1
        i -= 1
    return res


def main():
    arr = [-5, -3, -2, 0, 1, 2, 4, 5, 6, 8, 9]
    squared = [v * v for v in arr]
    print(squared)
    print(sort(squared))
    assert sorted(squared) == sort(squared)


if __name__ == "__main__":
    main()
