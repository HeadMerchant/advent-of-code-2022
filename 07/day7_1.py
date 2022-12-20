total_size = 0

MAX_SIZE = 100_000
class DirNode:
    def __init__(self, parent):
        self.parent = parent
        self.children = {}
    
    def get_size(self):
        global total_size
        size = sum((child.get_size() for child in self.children.values()))
        if size <= MAX_SIZE:
            total_size += size
        return size

class FileNode:
    def __init__(self, size):
        self.size = size
    
    def get_size(self):
        global total_size
        return self.size

with open("input.txt", "r") as f:
    lines = f.readlines()

current_dir = root = DirNode(None)

output_mode = False

for line in lines:
    line = line.strip()

    terminal_tokens = line.split(" ")

    if output_mode:
        filetype, *_ = terminal_tokens
        if filetype == "dir":
            _, name = terminal_tokens
            current_dir.children[name] = DirNode(current_dir)
            continue
        
        elif filetype == "$":
            output_mode = False

        else:
            _, name = terminal_tokens
            current_dir.children[name] = FileNode(int(filetype))
            continue
    
    if len(terminal_tokens) == 2:
        output_mode = True
        continue

    # cd
    *_, target_dir = terminal_tokens
    if target_dir == "..":
        current_dir = current_dir.parent
    elif target_dir == "/":
        current_dir = root
    else:
        current_dir = current_dir.children[target_dir]

if __name__ == "__main__":
    root.get_size()
    print(total_size)