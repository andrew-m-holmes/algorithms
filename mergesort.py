from typing import List


def mergesort(arr: List[int]) -> List[int]:
    arr = arr.copy()

    def sort(arr: List[int], start: int, end: int):
        if end - start < 1:
            return
        middle = (start + end) // 2
        sort(arr, start, middle)
        sort(arr, middle + 1, end)
        merge(arr, start, middle, end)

    sort(arr, 0, len(arr) - 1)
    return arr


def merge(arr: List[int], start: int, middle: int, end: int):
    left = arr[start : middle + 1]
    right = arr[middle + 1 : end + 1]
    i, j, k = 0, 0, start

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def main():
    arr = [38, 27, 43, 3, 9, 82, 10]
    print(arr)
    arr = mergesort(arr)
    print(arr)


if __name__ == "__main__":
    main()
