import sys
import math
import os
import time

x_max = 5
y_max = 6
size = 30
clear = lambda: os.system('cls')

def print_ht(h,ts, visited):
    for i in range(h[0]-size,h[0]+size):
        for j in range(h[1]-size, h[1]+size):
            if((i,j) == h):
                print("H", end="")
            elif((i,j) in ts):
                print(ts.index((i,j))+1, end="")
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

def do_move_tail(t1,t2,hasnt_moved_since, last_move, last_moves_t, pos):
    if(h_too_far_from_t(t1,t2)):
        move_tail = (0,0)
        for m in range(hasnt_moved_since):
            move_tail = move(move_tail,last_move[-m-1-pos])
        t2 = move(t2, move_tail)
        last_moves_t.append(move_tail)
    return t2, last_moves_t

def check_hasnt_move(ts, ts_hasnt_moved_since,last_ts_pos, i):
    if(i>9):
         return
    if(ts[i] == last_ts_pos[i]):
        ts_hasnt_moved_since[i] += 1
    else:
        ts_hasnt_moved_since[i] = 1
        check_hasnt_move(ts, ts_hasnt_moved_since,last_ts_pos, i+1)
    last_ts_pos[i] = ts[i]
    
def part1(data):
    h = (0,0)
    ts = [(0,0)] * 10
    visited_part1 = set()
    visited_part2 = set()
    moves = {
        "U": (-1, 0),
        "D": (1, 0),
        "R": (0, 1),
        "L": (0, -1)
    }
    last_moves_h = []
    last_moves_ts = []
    for i in range(10):
        last_moves_ts.append([(0,0)])
    ts_hasnt_moved_since = []
    for i in range(10):
        ts_hasnt_moved_since.append(0)
    last_ts_pos = []
    for i in range(10):
        last_ts_pos.append(h)
    for line in data:
        dir, n = line.split(" ")
        for i in range(int(n)):
            h = move(h, moves[dir])
            ts[0],last_moves_ts[0] = do_move_tail(h,ts[0],ts_hasnt_moved_since[0],last_moves_h, last_moves_ts[0], 0)
            for j in range(1,9):
                ts[j],last_moves_ts[j]  = do_move_tail(ts[j-1],ts[j],ts_hasnt_moved_since[j],last_moves_ts[j-1], last_moves_ts[j], 1)
                    
            check_hasnt_move(ts, ts_hasnt_moved_since,last_ts_pos, 0)
            
            last_moves_h.append(moves[dir])
            visited_part1.add(ts[0])
            visited_part2.add(ts[8])
            print_ht(h,ts, visited_part2)
            time.sleep(0.2)
            clear()

    print_ht(h,ts, visited_part2) 
    print(len(visited_part2))
        


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