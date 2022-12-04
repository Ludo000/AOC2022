import portion as P

def part1(data):
    count = 0
    for line in data:
        first_part,second_part = line.split(",")
        first1, first2 = first_part.split("-")
        second1, second2 = second_part.split("-")
        first_interval = P.closed(int(first1),int(first2))
        second_interval = P.closed(int(second1),int(second2))
        if(first_interval in second_interval or second_interval in first_interval):
            count += 1
    print("part1: ", count)


def part2(data):
    count = 0
    for line in data:
        first_part,second_part = line.split(",")
        first1, first2 = first_part.split("-")
        second1, second2 = second_part.split("-")
        first_interval = P.closed(int(first1),int(first2))
        second_interval = P.closed(int(second1),int(second2))
        intersection = first_interval & second_interval
        if(intersection != P.empty()):
            count +=1
    print("part2: ", count)


def main():
    f = open("4.txt", "r")
    lines = f.readlines()
    f.close()
    data = []
    for line in lines:
        data.append(line.rstrip("\n"))
    part1(data)
    part2(data)

if __name__ == "__main__":
    main()