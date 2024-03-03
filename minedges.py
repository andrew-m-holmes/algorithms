from typing import Dict, List, Set
from collections import deque


def minedges(graph: Dict[str, List[str]]) -> int:
    def bfs(node: str, visit: Set[str]):
        queue = deque([node])
        visit.add(node)

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor in visit:
                    continue
                queue.append(neighbor)
                visit.add(neighbor)

    visit, components = set(), 0
    for node in graph.keys():
        if node in visit:
            continue
        bfs(node, visit)
        components += 1
    return components - 1


def main():
    graph = {"A": ["B"], "B": ["A", "C"], "C": ["B"], "D": ["E"], "E": ["D"], "F": []}
    edges = minedges(graph)
    print(edges)


if __name__ == "__main__":
    main()
