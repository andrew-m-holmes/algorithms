from typing import List, Tuple, Optional, Dict
from collections import deque


def designate(
    wrestlers: List[str], rivalries: List[Tuple[str, str]]
) -> Optional[Dict[str, int]]:

    graph = dict()
    for w in wrestlers:
        graph[w] = list()
    for w, x in rivalries:
        graph[w].append(x)
        graph[x].append(w)
    partition = {w: 0 for w in wrestlers}

    def bfs(node: str):
        queue = deque([node])

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if partition[neighbor] != 0:
                    if partition[node] == partition[neighbor]:
                        return False
                    continue
                if partition[node] == 1:
                    partition[neighbor] = 2
                else:
                    partition[neighbor] = 1
                queue.append(neighbor)
        return True

    for w in wrestlers:
        if partition[w] != 0:
            continue
        partition[w] = 1
        if not bfs(w):
            return None
    return partition


def main():
    wrestlers = ["John", "Doe", "Jane", "Dane"]
    rivalries = [("John", "Jane"), ("Doe", "Dane")]
    result = designate(wrestlers, rivalries)
    print(result)

    wrestlers_possible = ["John", "Doe", "Jane", "Dane", "Kyle", "Leo"]
    rivalries_possible = [
        ("John", "Jane"),
        ("Doe", "Dane"),
        ("Kyle", "Leo"),
        ("Jane", "Kyle"),
    ]

    wrestlers_impossible = ["John", "Doe", "Jane", "Dane"]
    rivalries_impossible = [
        ("John", "Jane"),
        ("Doe", "Dane"),
        ("Jane", "Doe"),
        ("Jane", "Dane"),
    ]

    print(designate(wrestlers_possible, rivalries_possible))
    print(designate(wrestlers_impossible, rivalries_impossible))


if __name__ == "__main__":
    main()
