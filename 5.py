def part1(data):
    moves = [] 
    stack_size = 0
    cargo_lines = []
    #formating...
    for line in data:
        if(len(line) <= 0):
            continue
        if(line[0] == "m"):
            move_line = line.split(" ")
            moves.append((int(move_line[1]), int(move_line[3])-1, int(move_line[5])-1))
        elif(line.strip()[0] == "1"):
            stripped_line = line.strip()
            stack_size = int(stripped_line[len(stripped_line) -1])
        else:
            cargo_lines.append(line.replace(" ", "*").replace("****", "[ ]").replace("*","").replace("][", ",").replace("[","").replace("]",""))
            
    cargo_columns = []
    for i in range(stack_size):
        cargo_columns.append([])
    for cargo_line in cargo_lines:
        cargos = cargo_line.split(",")
        for i,cargo in enumerate(cargos):
            if(cargo != " "):
                cargo_columns[i].append(cargo)
    
    for c in cargo_columns:
        c.reverse()

    #playing moves
    for move in moves :
        nb = move[0]
        frome = move[1]
        to = move[2]
        for i in range(nb):
            tail = cargo_columns[frome][-1]
            cargo_columns[frome].pop()
            cargo_columns[to].append(tail)
    
    top = ""
    for c in cargo_columns:
        top += c[-1]   

    print("part1: ", top) 


def part2(data):
    moves = [] 
    stack_size = 0
    cargo_lines = []
    #formating
    for line in data:
        if(len(line) <= 0):
            continue
        if(line[0] == "m"):
            move_line = line.split(" ")
            moves.append((int(move_line[1]), int(move_line[3])-1, int(move_line[5])-1))
        elif(line.strip()[0] == "1"):
            stripped_line = line.strip()
            stack_size = int(stripped_line[len(stripped_line) -1])
        else:
            cargo_lines.append(line.replace(" ", "*").replace("****", "[ ]").replace("*","").replace("][", ",").replace("[","").replace("]",""))
            
    cargo_columns = []
    for i in range(stack_size):
        cargo_columns.append([])
    for cargo_line in cargo_lines:
        cargos = cargo_line.split(",")
        for i,cargo in enumerate(cargos):
            if(cargo != " "):
                cargo_columns[i].append(cargo)
    
    for c in cargo_columns:
        c.reverse()

    #playing moves
    for move in moves :
        nb = move[0]
        frome = move[1]
        to = move[2]
        moved_list = []
        for i in range(nb):
            tail = cargo_columns[frome][-1]
            cargo_columns[frome].pop()
            moved_list.append(tail)
        moved_list.reverse()
        for i in moved_list:
            cargo_columns[to].append(i) 
    
    top = ""
    for c in cargo_columns:
        top += c[-1]   

    print("part2: ", top) 

def main():
    f = open("5.txt", "r")
    lines = f.readlines()
    f.close()
    data = []
    for line in lines:
        data.append(line.rstrip("\n"))
    part1(data)
    part2(data)

if __name__ == "__main__":
    main()