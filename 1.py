def calorie_count(data):
    buffer = 0
    calories = []
    for i,n in enumerate(data):
        if(n != ""):
            buffer += int(n)
        if(n == "" or i==len(data)-1):
            calories.append(buffer)
            buffer = 0

    return(calories)



def main():
    f = open("1.txt", "r")
    lines = f.readlines()
    f.close()
    data = []
    for line in lines:
        data.append(line.rstrip("\n"))

    calories = calorie_count(data)
    print("part1: ", max(calories))
    
    top_three = []
    for i in range(3):
        max_calorie = max(calories)
        top_three.append(max_calorie)
        calories.remove(max_calorie)
    print("part2: ", sum(top_three))
if __name__ == "__main__":
    main()