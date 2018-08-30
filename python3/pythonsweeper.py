# Author: Josh Humphreys
# TO DO:
#   [ ] add output formatting
#   [ ] Refactor for readability and edge cases


import os
import math
import random
import re
import time
from typing import List


class Tile:
    def __init__(self):
        self.bomb_status = False
        self.adjacent = 0
        self.hidden = True
        self.flagged = False

def DEBUG_showMap(map,rows,cols):
    print("Bomb Map")
    for i in range(rows):
        #start building list
        line = []
        for j in range(cols):
            if map[i][j].bomb_status:
                line.append("B ")
            else:
                line.append(str(map[i][j].adjacent) + " ")
        #print
        print(''.join(str(e) for e in line))
    return

# def DEBUG_countBombs(map, rows, cols):
#     bombTotal = 0
#     for i in range(rows):
#         for j in range(cols):
#             if map[i][j].bomb_status:
#                 bombTotal+=1

# Count the number of adjacent bombs for each tile; check bomb status field, set adjacency field
def setAdjacent(map, rows, cols):
    #Row-major for consistency with other versions

    for i in range(rows):
        for j in range(cols):
            #directions
            directions = [(i - 1, j - 1),  # NW
                          (i - 1, j),  # N
                          (i - 1, j + 1),  # NE
                          (i, j - 1),  # W
                          (i, j + 1),  # E
                          (i + 1, j - 1),  # SW
                          (i + 1, j),  # S
                          (i + 1, j + 1)]  # SE
            #precomputed bool values
            validations = [(i-1 >= 0 and j-1 >= 0),  # NW
                          (i-1 >= 0),  # N
                          (i-1 >= 0 and j+1 < cols),  # NE
                          (j-1 >= 0),  # W
                          (j+1 < cols),  # E
                          (i + 1 < rows and j - 1 >= 0),  # SW
                          (i + 1 < rows),  # S
                          (i + 1 < rows and j + 1 < cols)]  # SE
            for k in range(len(directions)):
                if validations[k]:
                    if(map[int(directions[k][0])][int(directions[k][1])].bomb_status):
                        map[i][j].adjacent += 1

    return

# given number of bombs, plants them in random positions on the map (a 2d array of tile objects)
def plotBombs(bombCount, map, rows, cols):
    #print("BOMB COUNT: "+str(bombCount))
    for b in range(bombCount):
        map[random.randint(0,rows-1)][random.randint(0,cols-1)].bomb_status = True
    return

# replaces spaces with dashes
def trim(str):
    return re.sub(r'[ \t\n]', '-', str)


def getName():
    name = input("Enter your name: ")
    if len(name) < 15:
        #remove unwanted characters; will affect retrieving scores
        return trim(name)
    else:
        print("Invalid: Too Long")
        getName()

# pattern: integer+' '+integer, integers < max
# prompt area size from user, split:'x, '
def getArea():
    MIN = 5
    #DEBUG
    MIN = 1
    MAX = 15
    #prompt
    choice = input("Enter dimensions of play area (15 max) [l]x[w]: ")
    choice_list = re.split(r'[x ]', choice)
    choice_list = [str(i) for i in choice_list if i.isalnum()]

    #check input
    if len(choice_list) == 2:
        if(choice_list[0].isnumeric() and choice_list[1].isnumeric()):
            choice_list = [int(i) for i in choice_list]
            if((choice_list[0] >= MIN and choice_list[0] <= MAX) and (choice_list[1] >= MIN and choice_list[1] <= MAX)):
                return choice_list
            else:
                print("Usage ("+str(MIN)+" min): [l]x[w] --example: 10x10")
                return getArea()
        else:
            print("Usage: [l]x[w] --example: 10x10")
            return getArea()
    else:
        print("Usage: [l]x[w] --example: 10x10")
        return getArea()
    #bad: prompt usage, recurse


# draw i x j map with corresponding symbol in class ([X]hidden, [n]revealed, [F]lagged)
def drawArea(map, rows, cols):
    #Row-major for consistency with other versions
    for i in range(rows):
        #start building list
        line = []
        if i < 9:
            line.append(str(i + 1) + "|  ")
        else:
            line.append(str(i + 1) + "| ")
        for j in range(cols):
            if map[i][j].flagged:
                line.append("F ")
            elif map[i][j].hidden:
                line.append("X ")
            else:
                line.append(str(map[i][j].adjacent)+" ")
        #print
        print(''.join(str(e) for e in line))
    return

def checkFlag(bombCount, map_tile):
    if map_tile.bomb_status and map_tile.flagged:
        bombCount -= 1
    return bombCount

# Pattern: [B/F] <i> <j>
def validateCmd(input_list, rows, cols):
    # lower boundary subject change
    LOWER_BOUND = 0
    valid = False

    # length of list must equal 3
    if len(input_list) == 3:
        # [0] must be 'B' or 'F'
        cmd = input_list[0].lower()
        if (cmd[0] == 'b' or cmd[0] == 'f') and input_list[1].isnumeric() and input_list[2].isnumeric():
            # [1] & [2] must be integer and in bounds!
            i = int(input_list[1])
            j = int(input_list[2])
            if ((i-1 >= LOWER_BOUND and i-1 < rows) and (j-1 >= LOWER_BOUND and j-1 < cols)):
                valid = True

    return valid

# Get input from user in form of [B]oom or [F]lag [i][j]
# loop on error
# on boom: check class for bomb status; [n]reveal, bomb: gameover, flag: change presentation symbol
def getCommand(map):
    cmd = input("Enter command: ")
    cmd_list = re.split(r'[x ]',cmd)
    cmd_list = [str(i) for i in cmd_list  if i.isalnum()]
    if validateCmd(cmd_list, len(map), len(map[0])):
        #cmd_list = [int(i) for i in cmd_list if i.isnumeric()]
        return cmd_list
    else:
        print("Usage: [B/F] <x> <y>")
        return getCommand(map)

# check bomb status, reveal or gameover
def checkBomb(map_tile):
    if map_tile.bomb_status:
        return True
    else:
        map_tile.hidden = False
        return False

# if revealed bomb has adjacency field of 0, reveal all tiles recursively that connect and are 0 and non-0 neighbors
# NOTE: REMEMBER THE PREVIOUS DIRECTION OR ELSE WILL JUST KEEP TRAVELING (HITS DEPTH LIMIT)
def zeroAdj(map, i, j, visited):
    if((i >= 0 and i < len(map) and (j >= 0 and j < len(map[0])))):
        map[i][j].hidden = False
        if map[i][j].adjacent > 0:
            return

        # Traversal
        directions = [(i-1, j-1), #NW
                      (i-1, j), #N
                      (i-1, j+1), #NE
                      (i, j-1), #W
                      (i, j+1), #E
                      (i+1, j-1), #SW
                      (i+1, j), #S
                      (i+1, j+1)] #SE
        for d in directions:
            if (d[0], d[1]) not in visited:
                visited.append(d)
                zeroAdj(map, d[0], d[1], visited)
    else:
        return
#pattern [Yes/Y/No/N]
#prompt play again: [Y]es/[N]o
def playAgain():
    while True:
        choice = input("Play Again? [Y]es/[N]o: ")
        if choice[0].lower() == 'y' and len(choice) < 15:
            again = True
            return True
        elif choice[0].lower() == 'n' and len(choice) < 15:
            return False

def scoreGame(play_time, i, j):
    challenge = i * j
    MAX_TIME = 10000
    timeBonus = MAX_TIME - play_time
    #make sure score can't < 1
    if timeBonus < 1:
        timeBonus = 1
    return (timeBonus) + challenge

def printHighscore(dict):
    print("=====HIGHSCORES=====")
    for k,v in dict.items():
        print(k+"\t"+str(v))

# on win: open a highscore file, insert name
def logScore(name,play_time,i,j):
    score = scoreGame(play_time,i,j)
    line = name+"\t"+str(score)+"\n"
    # open or create highscore file
    file_name = "highscore.log"
    with open(file_name, 'a+') as log:
        # insert formatted name and time in file
        log.write(line)
    # sort file
    sortLog(file_name)
    return

def sortLog(file_name):
    # open highscore log
 #   log = open(file_name, 'w')
    # make list of name-score pairs
    top = {}
    kvpair = []
    with open(file_name, 'r') as f:
        for line in f:
            kvpair = line.replace("\n", '').split("\t")
            #linepair[i].strip('\n').split("[\t]",kvpair)
            #if(len(kvpair)>1):
            key,value = kvpair[0],int(kvpair[1])
            top[key] = int(value)
    f.close()

    # if score list size > 10, remove smallest score
    if len(top) > 10:
        minpair = min(top, key=top.get)
        del top[minpair]
    # sort them -- small data set
    sorted(top.values(), reverse=True)
    printHighscore(top)
    log = open(file_name, 'w')
    for k,v in top.items():
        log.write(k+"\t"+str(v)+"\n")
    log.close()
    return

# def bubbleSort(dict):
#     n = len(dict)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if dict[j][1] > dict[j+1][1]:
#                 temp = dict[j]
#                 dict[j] = dict[j+1]
#                 dict[j+1] = temp
#     return dict

# win conditions: prompt congrats, prompt name,
def win(name, start_time, finish_time, rows, cols):
    print("=====YOU WIN!!=====")
    play_time = int(finish_time - start_time)
    logScore(name, play_time, rows, cols)
    return

def lose():
    print("=====Ka-BOOM! GAME OVER!=====")
    return

def greeting():
    return "=====Welcome to Pythonsweeper=====\n" + \
            "GOAL: Flag every bomb!\n" + \
            "Usage: [B]oom/[F]lag [i][j]"
# RUN GAME
print(greeting())

#outer loop, play again?
while True:
    #prompt player name
    name = getName()

    area_tuple = getArea()  # type: List[int]
    rows = area_tuple[0]
    cols = area_tuple[1]
    bombCount = math.floor((rows * cols)/5)
    flagCount = bombCount
    MAX_FLAGS = flagCount
    #map is a matrix
    map = [[Tile() for j in range(cols)] for i in range(rows)]
    plotBombs(bombCount, map, rows, cols)
    setAdjacent(map, rows, cols)
    start_time = time.time()
    while True:
        #inner loop until win/lose: all mines flagged or boom
        os.system('clear' if os.name == 'posix' else 'cls')  # For Windows
        drawArea(map, rows, cols)
        DEBUG_showMap(map, rows, cols)
        print("Flags: "+ str(flagCount))
        playerInput = getCommand(map)
        action = playerInput[0]
        playerInput = [int(i) for i in playerInput if i.isnumeric()]
        x = playerInput[0]-1 #Type: int
        y = playerInput[1]-1
        chosen = map[x][y]

        if action == 'b':
            if (checkBomb(chosen)):
                lose()
                break
            elif chosen.adjacent == 0:
                zeroAdj(map, x,y,[])
        elif chosen.flagged and chosen.hidden:
                chosen.flagged = False
                flagCount += 1
        elif chosen.hidden:
            if(flagCount - 1 >= 0):
                chosen.flagged = True
                flagCount -= 1
            elif (bombCount > 0):
                print("Out of flags? Try retrieving some.")

        # cheat: flag everything; MUST CAP FLAG COUNT
        bombCount = checkFlag(bombCount, chosen)
        if bombCount < 1:
            win(name, start_time, time.time(), rows, cols)
            break
        #end inner loop

    if playAgain() == False:
        break
    #end outer loop

