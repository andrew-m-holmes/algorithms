from typing import List, Tuple


def schedule(
    intervals: List[Tuple[int, int]], start: int, end: int
) -> Tuple[List[Tuple[int, int]], int]:
    ordered = sorted(intervals, key=lambda i: i[0])
    scheduled, prev = [], 0
    for s, e in ordered:
        if s >= start and e <= end and s >= prev:
            prev = e
            scheduled.append((s, e))
    return scheduled, len(scheduled)


def main():
    start = 9
    end = 20
    intervals = [
        (14, 16),
        (10, 12),
        (17, 19),
        (11, 13),
        (15, 17),
        (12, 14),
        (13, 15),
        (16, 18),
    ]
    print(schedule(intervals, start, end))


if __name__ == "__main__":
    main()
