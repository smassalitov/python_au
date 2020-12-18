+ [ Maximum Depth of Binary Tree](#Maximum-Depth-of-Binary-Tree)
+ [ Binary Tree Inorder Traversal](#Binary-Tree-Inorder-Traversal)
+ [ Invert Binary Tree](#Invert-Binary-Tree)
+ [ Binary Search Tree Iterator](#Binary-Search-Tree-Iterator)
+ [ Binary Tree Level Order Traversal](#Binary-Tree-Level-Order-Traversal)
+ [ Kth Smallest Element in a BST](#Kth-Smallest-Element-in-a-BST)
+ [ Validate Binary Search Tree](#Validate-Binary-Search-Tree)
+ [ Symmetric Tree](#Symmetric-Tree)

##  Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/
```python
class Solution(object):
    def maxDepth(self, root):
        if root:
            return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)
        else:
            return 0
```
##  Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/
```python
class Solution(object):
    def inorderTraversal(self, root):
        if root:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        else:
            return []
```
##  Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/
```python
class Solution(object):
    def invertTree(self, root):
        if root:
		    root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
		    return root
        else:
		    return None
```
##  Binary Search Tree Iterator
https://leetcode.com/problems/binary-search-tree-iterator/
```python
class BSTIterator(object):

    def __init__(self, root):
        self.traversed = []
        def inOrderTraversal(node):
            if node:
                inOrderTraversal(node.left)
                self.traversed.append(node.val)
                inOrderTraversal(node.right)
        inOrderTraversal(root)

    def next(self):
        if self.hasNext():
            return self.traversed.pop(0)


    def hasNext(self):
        if len(self.traversed) != 0:
            return True
        else:
            return False
```

##  Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/
```python
class Solution(object):
       def levelOrder(self, root):
        if not root:
            return []
        stack = [[root, 0]]
        d = {}
        while stack:
            node, level = stack.pop(0)
            d[level] = d.get(level, []) + [node.val]
            if node.left:
                stack.append([node.left, level + 1])
            if node.right:
                stack.append([node.right, level + 1])
        result = []
        for element in sorted(d):
            result.append(d[element])
        return result
```
##  Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
```python
class Solution(object):
    def kthSmallest(self, root, k):
        mem = []
        while True:
            while root:
                mem.append(root)
                root = root.left
            root = mem.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
```
##  Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/
```python
class Solution(object):
    def search(self, root, min, max):
        if not root:
            return True
        if root.val >= max or root.val <= min:
            return False
        left = self.search(root.left, min, root.val)
        right = self.search(root.right, root.val, max)
        return left and right

    def isValidBST(self, root):
        return self.search(root, float('-inf'), float('inf'))
```
##  Symmetric Tree
https://leetcode.com/problems/symmetric-tree/
```python
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        def isMirror(left_kid, right_kid):
            if not left_kid and not right_kid:
                return True
            if (left_kid and not right_kid) or (right_kid and not left_kid) or (right_kid.val != left_kid.val):
                return False
            if not isMirror(right_kid.left, left_kid.right):
                return False
            if not isMirror(right_kid.right, left_kid.left):
                return False
            return True
        return isMirror(root.left, root.right)
```
