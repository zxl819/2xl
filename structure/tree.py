# 二叉树的定义
class TreeNode():
    def __init__(self,val,lchild=None,rchild=None):
        self.val = val
        self.lchild = lchild
        self.rchild = rchild

# 根据前序遍历得到二叉树
def Creat_Tree(Root,vals):
    if len(vals) == 0:
        return Root
    if vals[0] != 'null':
        Root = TreeNode(vals[0])
        vals.pop(0)
        Root.lchild = Creat_Tree(Root.lchild,vals)
        Root.rchild = Creat_Tree(Root.rchild,vals)
        return Root
    else:
        Root = None
        vals.pop(0)
        return Root

if __name__ == '__main__':
    Root = None
    strs = "abc##d##e##"
    vals = list(strs)
    Roots = Creat_Tree(Root,vals)
    print(Roots)