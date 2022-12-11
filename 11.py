


def part1(data):
    monkeys = []
    for i in range(10):
        monkeys.append([])
    monkeys_inspect_count = []
    for i in range(10):
        monkeys_inspect_count.append(0)
    worry = 0
    current_monkey = 0
    starting_items = []
    operation = ""
    operand = 0
    divider = 1
    throw = {
        "true": 0,
        "false": 0
    }
    for round in range(10000):
        for line in data:
            cs = line.strip().split(" ")
            if len(cs) == 2:
                current_monkey = int(cs[1].rstrip(":"))
            elif cs[0] == "Starting":
                if(round>0): continue
                starting_items = []
                for c in cs:
                    if c.rstrip(",").isnumeric() :
                        starting_items.append(int(c.rstrip(",")))
                starting_items += monkeys[current_monkey]
                monkeys[current_monkey] = starting_items
            elif cs[0] == "Operation:":
                operation = cs[4]
                operand = cs[-1]
            elif cs[0] == "Test:":
                divider = int(cs[-1])
            elif cs[0] == "If":
                throw[cs[1].rstrip(":")] = int(cs[-1])
            else:
                i=0
                for item in monkeys[current_monkey]:
                    monkeys_inspect_count[current_monkey] += 1
                    if operand == "old":
                        if operation == "*":
                            monkeys[current_monkey][i] *= monkeys[current_monkey][i]
                        else: 
                            monkeys[current_monkey][i] += monkeys[current_monkey][i]
                    else:
                        if operation == "*":
                            monkeys[current_monkey][i] *= int(operand)
                            
                        else: 
                            monkeys[current_monkey][i] += int(operand)
                        
                    #part1:
                    #monkeys[current_monkey][i] //= 3
                    #part2:
                    monkeys[current_monkey][i] = monkeys[current_monkey][i] % (11 * 7 * 13 * 5 * 3 * 17 * 2 * 19)
                    if(monkeys[current_monkey][i] % divider == 0):
                        result="true"
                    else:
                        result="false"
                    
                    monkeys[throw[result]].append(monkeys[current_monkey][i])
                    i += 1
                monkeys[current_monkey] = []

    monkeys_inspect_count.sort()
    monkeys_inspect_count.reverse()
    print(monkeys_inspect_count)
    print("part1:", monkeys_inspect_count[0]*monkeys_inspect_count[1])


def main():
    f = open("11.txt", "r")
    lines = f.readlines()
    f.close()
    data = []
    for line in lines:
        data.append(line.rstrip("\n"))
    part1(data)

if __name__ == "__main__":
    main()