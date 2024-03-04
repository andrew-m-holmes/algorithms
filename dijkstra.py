import heapq
from typing import Dict, List, Tuple


def minpath(graph: Dict[str, Dict[str, int]], source: str, destination: str) -> int:
    distances = {n: float("inf") if n != source else 0 for n in graph.keys()}
    pqueue: List[Tuple[int, str]] = [(0, source)]
    while pqueue:
        dist, node = heapq.heappop(pqueue)
        for neighbor, weight in graph[node].items():
            path = dist + weight
            if path < distances[neighbor]:
                distances[neighbor] = path
                heapq.heappush(pqueue, (path, neighbor))
    return int(distances[destination])


def main():
    graph = {
        "A": {"B": 1, "C": 4},
        "B": {"A": 1, "C": 2, "D": 5},
        "C": {"A": 4, "B": 2, "D": 1},
        "D": {"B": 5, "C": 1},
    }
    source = "A"
    destination = "D"

    path = minpath(graph, source, destination)
    print(path)

    graph = {
        "A": {"B": 2, "C": 5},
        "B": {"A": 2, "C": 6, "D": 1, "E": 3},
        "C": {"A": 5, "B": 6, "D": 4},
        "D": {"B": 1, "C": 4, "E": 2},
        "E": {"B": 3, "D": 2},
    }
    source = "A"
    destination = "E"

    path = minpath(graph, source, destination)
    print(path)

if __name__ == "__main__":
    main()
