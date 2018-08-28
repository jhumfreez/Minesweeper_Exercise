# Author: Josh Humphreys
# TO DO:
#   [ ] adding sorting for highscore; see sortLog()
#   [ ] add file i/o
#   [ ] cap flag count and flag toggle
#   [ ] get timings for scoring and sorting performance
#       Help: https://stackoverflow.com/questions/2866380/how-can-i-time-a-code-segment-for-testing-performance-with-pythons-timeit
#   [ ] print highscore
#   [ ] add DEBUG functions for testing timings

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
    MAX = 15
    #prompt
    choice = input("Enter dimensions of play area (15 max) [l]x[w]: ")
    choice_list = re.split("[x ]", choice)

    #check input
    if len(choice_list) == 2:
        if(choice_list[0].isnumeric() and choice_list[1].isnumeric()):
            choice_list = [int(i) for i in choice_list]
            if((choice_list[0] > 1 and choice_list[0] <= MAX) and (choice_list[1] > 1 and choice_list[1] <= MAX)):
                return choice_list
            else:
                print("Usage: [l]x[w] --example: 10x10")
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
    MIN = 0
    valid = False

    # length of list must equal 3
    if len(input_list) == 3:
        # [0] must be 'B' or 'F'
        cmd = input_list[0].lower()
        if (cmd[0] == 'b' or cmd[0] == 'f') and input_list[1].isnumeric() and input_list[2].isnumeric():
            # [1] & [2] must be integer and in bounds!
            i = int(input_list[1])
            j = int(input_list[2])
            if ((i >= MIN and i < rows) and (j >= MIN and j < cols)):
                valid = True

    return valid

# Get input from user in form of [B]oom or [F]lag [i][j]
# loop on error
# on boom: check class for bomb status; [n]reveal, bomb: gameover, flag: change presentation symbol
def getCommand(map):
    cmd = input("Enter command: ")
    cmd_list = re.split("[x ]",cmd)
    if validateCmd(cmd_list, len(map), len(map[0])):
        cmd_list = [int(i) for i in cmd_list if i.isnumeric()]
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

# if revealed bomb has adjacency field of 0, reveal all tiles recursively that connect and are 0 and their non-0 neighbors
# NOTE: REMEMBER THE PREVIOUS DIRECTION OR ELSE WILL JUST KEEP TRAVELING (HITS DEPTH LIMIT)
def zeroAdj(map, i, j, visited):
    if((i >= 0 and i < len(map) and (j >= 0 and j < len(map[0])))):
        map[i][j].hidden = False
        if map[i][j].adjacent > 0:
            return

        directions = [(i-1, j-1), #NW
                      (i-1, j), #N
                      (i-1, j+1), #NE
                      (i, j-1), #W
                      (i, j+1), #E
                      (i+1, j-1), #SW
                      (i+1, j), #S
                      (i+1, j+1)] #SE
        # else: recursive call in every adjacent direction
        for d in directions:
            if (d[0], d[1]) not in visited:
                visited.append(d)
                zeroAdj(map, d[0], d[1], visited)

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
    return (timeBonus) * challenge

# on win: open a highscore file, insert name
def logScore(name,play_time,i,j):
    score = scoreGame(play_time,i,j)
    insert = name+"\t"+str(score)
    # open or create highscore file
    # insert formatted name and time in file
    # sort file
    sortLog("highscore.log")
    return

def sortLog(file_name):
    # open highscore log
    # make list of name-score pairs
    # if score list size = 10, remove smallest score
    # sort them -- small data set
    return


def bubbleSort(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j][1] > list[j+1][1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

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
    bombCount = math.floor((rows * cols)/3)
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
        print("Bombs: "+ str(bombCount))
        playerInput = getCommand(map)
        x = playerInput[0] #Type: int
        y = playerInput[1]
        chosen = map[x][y]

        if playerInput[0] == 'b':
            if (checkBomb(chosen)):
                lose()
                break
            elif chosen.adjacent == 0:
                zeroAdj(map, playerInput[0],playerInput[1],[])
        else:
            chosen.flagged = True
        #cheat: flag everything; MUST CAP FLAG COUNT
        bombCount = checkFlag(bombCount, map[playerInput[0]][playerInput[1]])
        if bombCount < 1:
            win(name, start_time, time.time(), rows, cols)
            break
        #end inner loop

    if playAgain() == False:
        break
    #end outer loop

