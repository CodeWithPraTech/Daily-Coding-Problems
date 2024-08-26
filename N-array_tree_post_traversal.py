class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ls = []
        def traverse(root):
            if root:
                for i in root.children:
                    traverse(i)
                ls.append(root.val)
        traverse(root)
        return ls
        
