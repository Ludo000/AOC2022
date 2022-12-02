
def part1(data):
    score = 0
    points = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }
    win_relation = {
        "X":"C",
        "Y":"A",
        "Z":"B"
    }
    draw_relation = {
        "X":"A",
        "Y":"B",
        "Z":"C"
    }
    for line in data:
        op,me = line.split(" ")
        score += points[me];
        if win_relation[me]==op:
            score += 6
        elif draw_relation[me]==op:
            score += 3

    print("part1", score)

def part2(data):
    score = 0
    points = {
        "A": 1,
        "B": 2,
        "C": 3
    }
    win_relation = {
        "A":"B",
        "B":"C",
        "C":"A"
    }
    loose_relation = {
        "A":"C",
        "B":"A",
        "C":"B"
    }
    strategy = {
        "X": "lose",
        "Y": "draw",
        "Z": "win"
    }
    for line in data:
        op, me = line.split(" ")
        round_strat = strategy[me]
        if(round_strat == "draw"):
            score += points[op]
            score += 3
        elif(round_strat == "lose"):
            score += points[loose_relation[op]]
        else:
            score += 6
            score += points[win_relation[op]]
    print("part2:", score)

        
            



def main():
    f = open("2.txt", "r")
    lines = f.readlines()
    f.close()
    data = []
    for line in lines:
        data.append(line.rstrip("\n"))
    part1(data)
    part2(data)
 

if __name__ == "__main__":
    main()