class FileNode:
    def __init__(self, name, file_type):
        self.name = name
        self.file_type = file_type
        self.size = 0
        self.parent = None
        self.childs = []

class DirectoryTree:
    def __init__(self):
        self.root = FileNode("/", "directory")
        self.curr = self.root

    def change_dir(self, to):
        if to == "/":
            self.curr = self.root
        elif to == "..":
            if self.curr.parent != None:
                self.curr = self.curr.parent
        else:
            for child in self.curr.childs:
                if child.file_type == "directory" and child.name == to:
                    self.curr = child

    def insert(self, file_node):
        file_node.parent = self.curr
        self.curr.childs.append(file_node)

    def update_dir_size(self):
        def helper(curr):
            if len(curr.childs) == 0:
                return curr.size

            total_size = 0
            for child in curr.childs:
                total_size += helper(child)
            curr.size = total_size
            return total_size

        helper(self.root)

    def print(self):
        def helper(curr, level=0):
            print("    "*level + "-", curr.name, end=" ")
            print("(" + curr.file_type + ",", "size=" + str(curr.size) + ")")
            if len(curr.childs) != 0:
               for child in curr.childs:
                    helper(child, level+1)

        helper(self.root)

    def print_dir(self):
        def helper(curr, level=0):
            print("    "*level + "-", curr.name, end=" ")
            print("(" + curr.file_type + ",", "size=" + str(curr.size) + ")")
            if len(curr.childs) != 0:
               for child in curr.childs:
                    if child.file_type == "directory":
                        helper(child, level+1)

        helper(self.root)

    def calculate_dir_most_100000(self):
        def helper(curr):
            if len(curr.childs) == 0:
                return 0

            total_size = 0
            for child in curr.childs:
                total_size += helper(child)
            if curr.size <= 100000:
                total_size += curr.size
            return total_size

        return helper(self.root)

    def search_delete(self, key):
        def helper(curr):
            all_size = [70000000]
            if key + curr.size >= 30000000:
                all_size.append(curr.size)
            for child in curr.childs:
                if child.file_type == "directory":
                    all_size.append(helper(child))
            return min(all_size)

        return helper(self.root)

def solution1(inputs, dirtree):
    cmds = []
    is_ls = False
    ls = []
    for inp in inputs:
        if inp[0] == "$":
            if is_ls:
                is_ls = False
                cmds.append(ls)
                ls = []
            if inp[2] == "c":
                cmds.append(inp[2:].split())
            elif inp[2] == "l":
                is_ls = True
        else:
            ls.append(inp.split())
    if is_ls:
        is_ls = False
        cmds.append(ls)
        ls = []

    for cmd in cmds:
        if cmd[0] == "cd":
            dirtree.change_dir(cmd[1])
        else:
            for file in cmd:
                if file[0] == "dir":
                    file = FileNode(file[1], "directory")
                    dirtree.insert(file)
                else:
                    file_node = FileNode(file[1], "file")
                    file_node.size = int(file[0])
                    dirtree.insert(file_node)
    dirtree.update_dir_size()
    return dirtree.calculate_dir_most_100000()

def solution2(inputs, dirtree):
    key = 70000000 - dirtree.root.size
    return dirtree.search_delete(key)

def main():
    dirtree = DirectoryTree()
    print("Solution 1: " + str(solution1(read_input(), dirtree)))
    print("Solution 2: " + str(solution2(read_input(), dirtree)))

def read_input():
    f = open("input.txt", "r")
    all_lines = f.read().splitlines()
    return all_lines

if __name__ == "__main__":
    main()
