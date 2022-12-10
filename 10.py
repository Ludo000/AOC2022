

def incr_cycle(cycle, x,signal_strength):
    cycle += 1
    if( cycle == 20 or (cycle-20)%40 == 0):
        signal_strength.append((cycle, cycle * x))
    return cycle

def get_sum_signal_stength(signal_strength):
    sum = 0
    for s in signal_strength:
        sum += s[1]
    return sum

def part1(data):
    x = 1
    cycle = 1
    signal_strength = []
    for line in data:
        instr = line.split(" ")
        if(instr[0] == "noop"):
            print("cycle", cycle, "x=", x)
            cycle = incr_cycle(cycle, x, signal_strength)

        elif(instr[0] == "addx"):
            for i in range(2):
                if i==1 : 
                    print("during cycle", cycle, "x=", x)
                    x += int(instr[1])
                    print("end cycle", cycle, "x=", x)
                cycle = incr_cycle(cycle, x, signal_strength)

    print(signal_strength)
    print("part1: ", get_sum_signal_stength(signal_strength))


def draw(cycle, x):
    if(cycle%40 in range (x-1, x+2)):
        print("#", end="")
    else:
        print(".", end="")
    cycle += 1
    if( cycle %40 == 0):
        print(" ", cycle, end="")
        print("\n", end="")
    return cycle

def part2(data):
    x = 1
    cycle = 0
    cycle = draw(cycle, x)
    for line in data:
        instr = line.split(" ")
        if(instr[0] == "noop"):
            cycle = draw(cycle, x)

        elif(instr[0] == "addx"):
            for i in range(2):
                if i==1 : 
                    x += int(instr[1])
                cycle = draw(cycle, x)



def main():
    f = open("10.txt", "r")
    lines = f.readlines()
    f.close()
    data = []
    for line in lines:
        data.append(line.rstrip("\n"))
    part2(data)

if __name__ == "__main__":
    main()