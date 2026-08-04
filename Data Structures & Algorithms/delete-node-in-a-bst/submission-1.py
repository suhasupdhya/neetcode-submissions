class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:

            # Case 1: No left child
            if not root.left:
                return root.right

            # Case 2: No right child
            if not root.right:
                return root.left

            # Case 3: Two children
            curr = root.right
            while curr.left:
                curr = curr.left

            root.val = curr.val

            root.right = self.deleteNode(root.right, curr.val)

        return root
        