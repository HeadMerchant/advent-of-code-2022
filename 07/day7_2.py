from cgitb import small
from day7_1 import root, DirNode

FILESYSTEM_CAPACITY = 70_000_000
REQUIRED_SPACE = 30_000_000

used_space = root.get_size()
print(used_space)

space_to_free = used_space-(FILESYSTEM_CAPACITY-REQUIRED_SPACE)
print(space_to_free)
inf = float('inf')
def smallest_node_to_delete(node):
    if isinstance(node, DirNode):
        dir_size = 0
        smallest_valid = inf
        for child in node.children.values():
            candidate_size, size = smallest_node_to_delete(child)
            dir_size += size
            smallest_valid = min(smallest_valid, candidate_size)
        
        if dir_size >= space_to_free:
            smallest_valid = min(smallest_valid, dir_size)
        return smallest_valid, dir_size
    
    smallest_valid = inf if node.size < space_to_free else node.size
    return smallest_valid, node.size

print(smallest_node_to_delete(root))