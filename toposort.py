from typing import Dict, List
from collections import deque


def toposort(g: Dict[str, List[str]]) -> List[str]:
    order = []
    counts = {n: 0 for n in g.keys()}
    for e in g.values():
        for a in e:
            counts[a] += 1

    nodep = deque([n for n, ndep in counts.items() if not ndep])
    while len(order) != len(counts):
        n = nodep.popleft()  # dfs use pop()
        order.append(n)
        for a in g[n]:
            counts[a] -= 1
            if not counts[a]:
                nodep.append(a)
    return order


def main():

    graph = {
        "1": ["2", "7"],
        "2": ["5"],
        "3": ["4", "6"],
        "4": [],
        "5": ["3", "6"],
        "6": [],
        "7": ["5", "8"],
        "8": [],
    }
    order = toposort(graph)
    print(order)


if __name__ == "__main__":
    main()
