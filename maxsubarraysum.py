from typing import List


def maxsubsum(nums: List[int]) -> int:
    currsum, maxsum = 0, -float("inf")
    start, tmp, end = 0, 0, 1

    for i, e in enumerate(nums):
        if e > currsum + e:
            currsum = e
            tmp = i
        else:
            currsum += e

        if currsum > maxsum:
            maxsum = currsum
            start = tmp
            end = i + 1
    return sum(nums[start:end])


def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxsubsum(nums))
    nums = [5, 4, -1, 7, 8]
    print(maxsubsum(nums))
    nums = [-1, -2]
    print(maxsubsum(nums))


if __name__ == "__main__":
    main()
