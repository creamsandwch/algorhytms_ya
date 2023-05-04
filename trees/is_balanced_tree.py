# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:  
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def find_height(root: Node) -> int:
    if not root:
        return 0
    else:
        return max(find_height(root.left), find_height(root.right)) + 1


def solution(root):
    if not is_balanced(root):
        return False
    if root.left:
        if not is_balanced(root.left):
            return False
        else:
            return solution(root.left)
    if root.right:
        if not is_balanced(root.right):
            return False
        else:
            return solution(root.right)
    return True


def is_balanced(root) -> bool:
    left = find_height(root.left)
    right = find_height(root.right)
    return abs(left - right) <= 1


def test():
    node8 = Node(8, None, None)
    node7 = Node(7, None, None)
    node6 = Node(6, None, None)
    node5 = Node(5, None, None)
    node4 = Node(4, node7, node8)
    node3 = Node(3, node5, node6)
    node2 = Node(2, None, node4)
    node1 = Node(1, node3, None)
    node0 = Node(0, node1, node2)
    print(solution(node0))


if __name__ == '__main__':
    test()
