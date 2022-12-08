import numpy as np

def analyse_forest(data):
    visible_tree = []
    max_i, max_j = data.shape
    scenic_score_list = []
    print(max_i, max_j)
    for row,line in enumerate(data):
        for col,c in enumerate(line):
            if(row == 0 or col == 0 or row == len(data)-1 or col == len(line)-1):
                visible_tree.append((row, col))
            else:
                checked_tree = int(c)
                is_visibleFromUp = True
                is_visibleFromDown = True
                is_visibleFromLeft = True
                is_visibleFromRight = True
                print("\n checking", (row,col), "=", c)
                #check up
                print("check up")
                up = 0
                for i in reversed(range(row)):
                    print("testing: ", (i,col), "=", data[i][col])
                    up +=1
                    if(data[i][col] >= checked_tree):
                        is_visibleFromUp = False
                        print((row,col), "not visible from up")
                        break
                #check down
                print("check down")
                down = 0
                for i in range(row+1, max_i):
                    print("testing: ", (i,col), "=", data[i][col])
                    down += 1
                    if(data[i][col] >= checked_tree):
                        is_visibleFromDown = False
                        print((row,col), "not visible from down")
                        break
                
                #check left
                print("check left")
                left = 0
                for j in reversed(range(col)):
                    print("testing: ", (i,col), "=", data[row][j])
                    left += 1
                    if(data[row][j] >= checked_tree):
                        is_visibleFromLeft = False
                        print((row,col), "not visible from left")
                        break

                #check right
                print("check right")
                right = 0
                for j in range(col+1, max_j):
                    print("testing: ", (i,col), "=", data[row][j])
                    right += 1
                    if(data[row][j] >= checked_tree):
                        is_visibleFromRight = False
                        print((row,col), "not visible from right")
                        break

                scenic_score_list.append(up * down * left * right)
                
                if(is_visibleFromUp or is_visibleFromDown or is_visibleFromLeft or is_visibleFromRight):
                    visible_tree.append((row,col))

    print("amount of visible tree: ",len(visible_tree))
    print("max scenic score: ", max(scenic_score_list))
    

def main():
    with open("8.txt") as textFile:
        data = np.genfromtxt(textFile, dtype=int,delimiter=1)
    print("forest:", data)
    analyse_forest(data)

if __name__ == "__main__":
    main()