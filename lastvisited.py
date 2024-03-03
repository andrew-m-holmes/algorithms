from typing import Dict, List, Optional


def lastvisited(graph: Dict[str, List[str]]) -> Optional[str]:
    last = None

    def dfs(node: str, visit: set):
        nonlocal last
        last = node
        for neighbor in graph[node]:
            if neighbor in visit:
                continue
            visit.add(neighbor)
            dfs(neighbor, visit)

    visit = set()
    for node in graph.keys():
        if node not in visit:
            visit.add(node)
            dfs(node, visit)
    return last


def main():
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "G"],
        "F": ["C"],
        "G": ["E"],
    }

    last_node = lastvisited(graph)
    print(last_node)


if __name__ == "__main__":
    main()
