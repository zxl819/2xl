from idlelib.tree import TreeNode
from typing import Optional

# 构建二叉树，求子节点的运算
import null as null


class TreeNode():
    def __init__(self, val, lchild=None, rchild=None):
        self.val = val
        self.lchild = lchild
        self.rchild = rchild


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.left is None:
            return root == 1
        l = self.evaluateTree(root.left)
        r = self.evaluateTree(root.right)
        if root == 2:
            return l or r
        if root == 3:
            return l and r


root = [2, 1, 3, null, null, 0, 1]
# Solution().evaluateTree(root)


# 求最长前缀
strs = ["flower", "flow", "flight"]


def longestCommonPrefix(strs):
    res = ''
    for tmp in zip(*strs):
        tmp_set = set(tmp)
        if len(tmp_set) == 1:
            res += tmp[0]
        else:
            break
    return res


print(longestCommonPrefix(strs))
