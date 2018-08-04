class Solution:
    def mergeTrees(self, t1, t2):
        if (not t1) and (not t2):
            return None
        else:
            if (not t1) and t2:
                t1 = TreeNode(t2.val)
                t1.left = self.mergeTrees(t1.left, t2.left)
                t1.right = self.mergeTrees(t1.right, t2.right)           
            elif t1 and t2:
                t1.val = t1.val + t2.val
                t1.left = self.mergeTrees(t1.left, t2.left)
                t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

s = Solution()

def mergeTrees(self, t1, t2):
    if not t1 and not t2: return None
    ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
    ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
    ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
    return ans

class Solution(object):
    def mergeTrees(self, t1, t2):
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
            return root
        else:
            return t1 or t2
