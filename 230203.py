from idlelib.tree import TreeNode


class ListNode:
    def __init__(self, val):
        if isinstance(val, int):
            self.val = val
            self.next = None
            cur = self
        for i in val[1:]:
            cur.next = ListNode(i)
            cur = cur.next

    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
        return self.__class__.__name__ + " {" + "{}".format(self.gatherAttrs()) + "}"


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if isinstance(l1, list):
            l1 = ListNode(l1)
            l2 = ListNode(l2)
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        xNode = None

        def getSubtreeSize(node):
            if not node:
                return 0
            if node.val == x:
                nonlocal xNode
                xNode = node
            return 1 + getSubtreeSize(xNode.left) + getSubtreeSize(xNode.right)

        getSubtreeSize(root)

        leftSize = getSubtreeSize(xNode.left)
        if leftSize >= (n + 1) // 2:
            return True
        rightSize = getSubtreeSize(xNode.right)
        if rightSize >= (n + 1) // 2:
            return True

        remain = n - leftSize - rightSize - 1
        return remain >= (n + 1) // 2


root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
n = 11
x = 3
Solution().btreeGameWinningMove()
