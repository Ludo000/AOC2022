import sys
import math
import os
import time

x_max = 5
y_max = 6
size = 20
clear = lambda: os.system('cls')

def print_ht(h,t, t2, visited):
    for i in range(h[0]-size,h[0]+size):
        for j in range(h[1]-size, h[1]+size):
            if((i,j) == h):
                print("H", end="")
            elif((i,j) == t):
                print("1", end="")
            elif((i,j) == t2):
                print("2", end="")
            elif((i,j) == (0,0)):
                print("s", end="")
            elif( (i,j) in visited):
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()

def move(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

def h_too_far_from_t(h,t):
    distance = (t[0]-h[0])**2 + (t[1]-h[1])**2
    #print("dist", distance)
    return distance > 2
def part1(data):
    h = (0,0)
    t = (0,0)
    t2 = (0,0)
    visited = set()
    moves = {
        "U": (-1, 0),
        "D": (1, 0),
        "R": (0, 1),
        "L": (0, -1)
    }
    last_moves = []
    last_moves_t = []
    t_hasnt_moved_since = 0
    t2_hasnt_moved_since = 0
    last_t_pos = h
    last_t2_pos = h
    for line in data:
        dir, n = line.split(" ")
        for i in range(int(n)):
            h = move(h, moves[dir])
            if(h_too_far_from_t(h,t)):
                move_t = (0,0)
                for m in range(t_hasnt_moved_since):
                    move_t = move(move_t,last_moves[-m-1])
                t = move(t, move_t)
                last_moves_t.append(move_t)
            if(h_too_far_from_t(t,t2)):
                move_t2 = (0,0)
                for m in range(t2_hasnt_moved_since):
                    move_t2 = move(move_t2,last_moves_t[-m-2])
                t2 = move(t2, move_t2)
                    
            
            if(t == last_t_pos):
                t_hasnt_moved_since += 1
            else:
                t_hasnt_moved_since = 1
                if(t2 == last_t2_pos):
                    t2_hasnt_moved_since += 1
                else:
                    t2_hasnt_moved_since = 1
                last_t2_pos = t2
            last_t_pos = t
            
            

            last_moves.append(moves[dir])
            visited.add(t2)
            print_ht(h,t,t2, visited)
            time.sleep(2)
            clear()

    print_ht(h,t,t2, visited) 
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