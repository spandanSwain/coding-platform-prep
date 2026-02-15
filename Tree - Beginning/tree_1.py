class tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_tree_preorder(l): # inorder way can never be created
    idx = [-1] # for postorder, this is [len(l)] move from last end of list (input should match postorder way)
    def build():
        idx[0] += 1 # decrease the i value for postorder input
        if l[idx[0]] == -1: return None
        newChild = tree(l[idx[0]])
        newChild.left = build() # build right tree first then left tree for postorder input
        newChild.right = build()
        return newChild
    return build()

"""
This is our input
    1
   / \
  2   3
 / \\   \
 4  5   6
"""
root_node = create_tree_preorder([1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1])
# example of post_order input = [-1,-1,4,-1,-1,5,2,-1,-1,-1,6,3,1] # apna college dekhide
# print(f"Root value = {root_node.val}")
# will print root's value, as in recursion call stack (LIFO or First In Last Out) 
# i.e. The first called element is returned after completion of process

def create_tree_postorder(l):
    idx = [len(l)]
    def build():
        idx[0] -= 1
        if l[idx[0]] == -1: return None
        newChild = tree(l[idx[0]])
        newChild.right = build()
        newChild.left = build()
        return newChild
    return build()
# post_root_node = create_tree_postorder([-1,-1,4,-1,-1,5,2,-1,-1,-1,6,3,1])
# print(f"Root value in postorder input = {post_root_node.val}")

def traverse_preorder_tree(root):
    if root == None: return
    print(root.val)
    traverse_preorder_tree(root.left)
    traverse_preorder_tree(root.right)

print("Pre Order Traversal") # root left right
traverse_preorder_tree(root_node)

def traverse_inorder_tree(root):
    if root == None: return
    traverse_inorder_tree(root.left)
    print(root.val)
    traverse_inorder_tree(root.right)

# print("In Order Traversal") # left root right
# traverse_inorder_tree(root_node)


def traverse_postorder_tree(root):
    if root == None: return
    traverse_postorder_tree(root.left)
    traverse_postorder_tree(root.right)
    print(root.val)

# print("Post Order Traversal") # left right root
# traverse_postorder_tree(root_node)


# if you want values inside a list then
def try_inorder(root):
    ans = []
    build_inorder(root, ans)
    print(ans)
def build_inorder(root, ans):
    if root:
        build_inorder(root.left, ans)
        ans.append(root.val)
        build_inorder(root.right, ans)

# print("Array of inorder traversal -- doing for root node from post_order")
# try_inorder(post_root_node)

"""
BFS of Tree is Level Order Traversal:
for this Tree:
    1
   / \
  2   3
 / \\   \
 4  5   6

 Level Order Traversal is:
 1
 2 3
 4 5 6
"""

def level_order_traversal(root: tree | None) -> None | list: # BFS traversal of tree, just remove and don't print level wise
    # BFS of this input should give 1 2 3 4 5 6
    # this uses Queue for FIFO, no recursion is needed
    if not root: return []
    q: list = [root, None] # queue
    ans = [] # store BFS result
    while q:
        curr_node = q.pop(0)
        if curr_node == None:
            print()
            # ans.append(-1) # Optional, it shows start of new level
            if not q: return ans # if queue is empty halt process
            else: q.append(None) # else add None, this will separate levels
        else:
            print(curr_node.val, end=" ")
            ans.append(curr_node.val)
            if curr_node.left != None:
                q.append(curr_node.left)
            if curr_node.right != None:
                q.append(curr_node.right)
    return ans
print("Level Order Traversal")
bfs_res = level_order_traversal(root_node)
print(f"BFS Result = {bfs_res}")

def depth_of_binary_tree(root: tree | None):
    if not root: return 0
    q, depth = [root, None], 0
    while q:
        curr = q.pop(0)
        if curr == None:
            depth+=1
            if not q: return depth
            else: q.append(None)
        else:
            if curr.left: q.append(curr.left)
            if curr.right: q.append(curr.right)

print(f"Depth of Tree = {depth_of_binary_tree(root_node)}") # 3 for our example


def depth_using_DFS(root):
    if not root: return 0
    left = 1 + depth_using_DFS(root.left)
    right = 1 + depth_using_DFS(root.right)
    return max(left, right)
print(f"Depth using recursion and DFS: {depth_using_DFS(root_node)}")

"""
Level Order Traversal
1
2 3
4 5 6
BFS Result = [1, 2, 3, 4, 5, 6]
"""

"""
Root value = 1
Root value in postorder input = 1
Pre Order Traversal
1
2
4
5
3
6
In Order Traversal
4
2
5
1
3
6
Post Order Traversal
4
5
2
6
3
1
Array of inorder traversal -- doing for root node from post_order
[4, 2, 5, 1, 3, 6]
"""