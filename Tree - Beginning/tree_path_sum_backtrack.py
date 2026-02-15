class tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_tree(l: list) -> tree:
    idx = [-1]
    def build(): # root left right
        idx[0] += 1
        if l[idx[0]] == -1: return
        node = tree(l[idx[0]])
        node.left = build()
        node.right = build()
        return node
    return build()

def preorder(root: tree) -> list: # root left right
    ans = []
    build_preorder(root, ans)
    return ans

def build_preorder(root: tree, ans: list) -> list:
    if root:
        build_preorder(root.left, ans)
        ans.append(root.val)
        build_preorder(root.right, ans)

def level_order(root: tree) -> None:
    if not root: return
    q = [root, None]
    while q:
        curr = q.pop(0)
        if curr == None:
            print()
            if not q: return
            else: q.append(None)
        else:
            print(curr.val, end=" ")
            if curr.left != None: q.append(curr.left)
            if curr.right != None: q.append(curr.right)
    

def backtrack_path_sum(root: tree, target: int) -> bool:
    curr_sum = 0
    return help_backtrack(root, target, curr_sum)

def help_backtrack(root, target, curr_sum):
    if not root: return False
    curr_sum += root.val
    if not root.left and not root.right: return target == curr_sum# we reached leaf node
    else: return help_backtrack(root.left, target, curr_sum) or help_backtrack(root.right, target, curr_sum)


root_node = create_tree([1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1])
level_order(root_node)
print(f"For target = 8 can we get path sum: {backtrack_path_sum(root_node, 8)}")


def hasPathSum(root: tree, target: int) -> bool:
    # use either of them
    # return backtrack_path(root, target, [])
    return backtrack_int(root, target, 0)

def backtrack_int(root: tree, target: int, curr_sum: int):
    if not root: return False
    curr_sum += root.val

    if not root.left and not root.right:
        if curr_sum == target: return True # if leaf simply return if they are same or not
    
    # curr_sum -= root.val not needed as recursion handles it (i don't get how)
    return backtrack_int(root.left, target, curr_sum) or backtrack_int(root.right, target, curr_sum)

def backtrack_path(root: tree, target: int, path: list):
    if not root: return False
    path.append(root.val)

    if not root.left and not root.right:
        if sum(path) == target: return True # if leaf simply return if they are same or not
    
    left = backtrack_path(root.left, target, path)
    right = backtrack_path(root.right, target, path)

    path.pop()
    return left or right

print(f"For target = 8 can we get path sum: {hasPathSum(root_node, 8)}")