import sys
import math
import os
import time

x_max = 5
y_max = 6
size = 20
clear = lambda: os.system('cls')

def print_ht(h,t, visited):
    for i in range(h[0]-size,h[0]+size):
        for j in range(h[1]-size, h[1]+size):
            if((i,j) == h):
                sys.stdout.write("H")
            elif((i,j) == t):
                sys.stdout.write("T")
            elif((i,j) == (0,0)):
                sys.stdout.write("s")
            elif( (i,j) in visited):
                sys.stdout.write("#")
            else:
                sys.stdout.write(".")
        print()

def move(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

def h_too_far_from_t(h,t):
    distance = (t[0]-h[0])**2 + (t[1]-h[1])**2
    return distance > 2
def part1(data):
    h = (0,0)
    t = (0,0)
    visited = set()
    moves = {
        "U": (-1, 0),
        "D": (1, 0),
        "R": (0, 1),
        "L": (0, -1)
    }
    #print_ht(h,t,visited)
    #print()
    last_moves = []
    t_hasnt_moved_since = 0
    last_t_pos = h
    for line in data:
        dir, n = line.split(" ")
        for i in range(int(n)):
            h = move(h, moves[dir])
            if(i>0):
                if(h_too_far_from_t(h,t)):
                    for m in range(t_hasnt_moved_since):
                        t = move(t, last_moves[-m-1])
                    
            if(t == last_t_pos):
                t_hasnt_moved_since +=1
            else:
                t_hasnt_moved_since = 1
            last_t_pos = t
            
            last_moves.append(moves[dir])
            visited.add(t)
            #print_ht(h,t, visited)
            #time.sleep(2)
            #clear()

    print_ht(h,t, visited) 
    print(len(visited))
        


def main():
    f = open("9.txt", "r")
    lines = f.readlines()
    f.close()
    data = []
    for line in lines:
        data.append(line.rstrip("\n"))
    part1(data)

if __name__ == "__main__":
    main()