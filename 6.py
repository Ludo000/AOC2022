
def find_n_first_disctinct_chars_pos(data, n):
    for line in data:
       i=0
       start=0
       while start < len(line)-n:
        buffer = ""
        for i in range(start, start+n):
            if(i >= len(line)-1):
                break
            buffer += line[i]
        start += 1
        occurence = False
        for c in buffer:
            if(buffer.count(c)>1):
                occurence=True
                break
        if(not occurence):
            return start+n-1

def main():
    f = open("6.txt", "r")
    lines = f.readlines()
    f.close()
    data = []
    for line in lines:
        data.append(line.rstrip("\n"))
    print("part1:",find_n_first_disctinct_chars_pos(data, 4))
    print("part2:",find_n_first_disctinct_chars_pos(data, 14))

if __name__ == "__main__":
    main()