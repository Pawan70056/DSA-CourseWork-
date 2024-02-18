from collections import defaultdict

def find_nodes_with_only_target_as_parent(edges, target):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    # Build the graph and calculate in-degree of each node
    for from_node, to_node in edges:
        graph[from_node].append(to_node)
        in_degree[to_node] += 1
    # Perform DFS starting from the target node
    result = []
    dfs(graph, in_degree, target, target, result)
    return result

def dfs(graph, in_degree, node, target, result):
    # If the current node has no incoming edges other than from the target node,
    # add it to the result
    if in_degree.get(node, 0) == 1 and node != target:
        result.append(node)
    # Recursively explore the children of the current node
    if node in graph:
        for child in graph[node]:
            dfs(graph, in_degree, child, target, result)

if __name__ == "__main__":
    edges = [(0, 1), (0, 2), (1, 3), (1, 6), (2, 4), (4, 6), (4, 5), (5, 7)]
    target = 4
    unique_parents = find_nodes_with_only_target_as_parent(edges, target)
    print(f"Nodes whose only parent is {target}: {{", end="")
    for i, node in enumerate(unique_parents):
        end_char = ", " if i < len(unique_parents) - 1 else ""
        print(node, end=end_char)
    print("}")


