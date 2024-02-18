import heapq

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def closest_values(root, target, x):
    result = []
    if root is None or x == 0:
        return result
    pq = []
    in_order_traversal(root, target, x, pq)
    while pq:
        result.append(heapq.heappop(pq)[1])
    return result

def in_order_traversal(node, target, x, pq):
    if node is None:
        return
    in_order_traversal(node.left, target, x, pq)
    diff = abs(target - node.val)
    heapq.heappush(pq, (diff, node.val))
    if len(pq) > x:
        heapq.heappop(pq)
    in_order_traversal(node.right, target, x, pq)

if __name__ == "__main__":
    # Construct the BST
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    k = 3.8
    x = 2
    closest = closest_values(root, k, x)
    print(f"Closest values to {k} with distance {x}: {closest}")


