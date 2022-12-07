import re 
from anytree import Node, RenderTree, findall


def getChildrenWeight(node):
    nodes = findall(node)
    w = 0
    for node in nodes:
        w += node.w
    return w


def part1(data):
    i=0
    fs = Node("/", w=0)
    current_node = fs
    while i < len(data):
        if re.search("\$ cd [a-zA-Z]", data[i]) or data[i] == "$ cd /":
            name = data[i].split(" ")[2]
            current_node = Node(name, parent=current_node, w=0)
            if i+1 < len(data) and re.search("\$ ls", data[i+1]):
                j=i+2
                while j < len(data) and data[j][0] != "$":
                    w = data[j].split(" ")[0]
                    name = data[j].split(" ")[1]
                    if(w == "dir"):
                        Node(name, parent=current_node, w=0)
                    else:
                        Node(name, parent=current_node, w=int(w))
                    j+= 1
                i = j
                continue
            else:
                i += 1
        elif re.search("\$ cd ..", data[i]):
            current_node = current_node.parent
        i += 1
    sum = 0
    dirs = []
    for pre, fill, node in RenderTree(fs):
        if(node.w == 0):
            node.w = getChildrenWeight(node)
            dirs.append(node.w) # only needed for part2
        if(node.children and node.w <= 100000):
            sum += node.w
        print("%s%s %d" % (pre, node.name, node.w))  


    print("part1:", sum)

    #part2
    total_space = 70000000
    required_space = 30000000
    used_space = fs.w
    unused_space = total_space - used_space
    dirs.sort()
    for dir in dirs:
        if(unused_space + dir >= required_space):
            print("part2:", dir)
            break





def main():
    f = open("7.txt", "r")
    lines = f.readlines()
    f.close()
    data = []
    for line in lines:
        data.append(line.rstrip("\n"))
    part1(data)

if __name__ == "__main__":
    main()