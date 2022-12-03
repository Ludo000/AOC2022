
def part1(data):
    count = 0
    ascii_delta = {
        True: 96,
        False: 38
    }
    for line in data:
        firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
        common = "".join(set(firstpart).intersection(secondpart))
        for c in common:
            count += ord(c) - ascii_delta[c.islower()]
    print("part1:", count)


def part2(data):
    count = 0
    ascii_delta = {
        True: 96,
        False: 38
    }
    current_group = []
    i=0
    for line in data:
        current_group.append(line)
        if(i == 2):
            common = set.intersection(*map(set,current_group))            
            for c in common:
                count += ord(c) - ascii_delta[c.islower()]
            current_group = []
            i = 0
        else:
            i += 1
    print("part1", count)

def main():
    f = open("3.txt", "r")
    lines = f.readlines()
    f.close()
    data = []
    for line in lines:
        data.append(line.rstrip("\n"))
    part1(data)
    part2(data)
 

if __name__ == "__main__":
    main()