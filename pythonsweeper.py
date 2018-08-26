# Author: Josh Humphreys
# TO DO:
#   [ ] adding sorting for highscore; see sortLog()
#   [ ] add user prompts
#   [ ] add tile traversal; see zeroAdj()
#       Idea: recursive iteration through every direction; check null, bomb adjacency
#   [ ] finish writing functions
#   [ ] get timings for scoring and sorting performance
#       Help: https://stackoverflow.com/questions/2866380/how-can-i-time-a-code-segment-for-testing-performance-with-pythons-timeit
#   [ ] print highscore
#   [ ] add DEBUG functions for testing timings

import os
import math
import time

class Tile:
    def __init__(self):
        self.bomb_status = False
        self.adjacent = 0
        self.hidden = True
        self.flagged = False

# Count the number of adjacent bombs for each tile; check bomb status field, set adjacency field
def setAdjacent(map):
    return

# given number of bombs, plants them in random positions on the map (a 2d array of tile objects)
def plotBombs(bombCount, map):
    return

# prompt area size from user
def getArea():
    i,j = 0
    #prompt
    #get input
    #check input
    #bad: prompt usage, recurse
    return (i,j)

# draw i x j map with corresponding symbol in class ([X]hidden, [n]revealed, [F]lagged)
def drawArea(map):

    return

def checkFlag(bombCount, map_tile):
    if map_tile.bomb_status and not map_tile.flagged:
        bombCount -= 1
    return bombCount

# Get input from user in form of [B]oom or [F]lag [i][j]
# loop on error
# on boom: check class for bomb status; [n]reveal, bomb: gameover, flag: change presentation symbol
def getCommand():
    return

# check bomb status, reveal or gameover
def checkBomb(map_tile):
    if map_tile.bomb_status:
        return True
    else:
        map_tile.hidden = False
        return False

# if revealed bomb has adjacency field of 0, reveal all tiles recursively that connect and are 0 and their non-0 neighbors
def zeroAdj():
    return

#prompt play again: [Y]es/[N]o
def playAgain():
    again = False
    # prompt
    # check input
        #bad: prompt usage, recurse
    # return true or false
    if again:
        return True
    else:
        return False

def scoreGame(play_time, i, j):
    challenge = i * j
    MAX_TIME = 10000
    timeBonus = MAX_TIME - play_time
    return (timeBonus) * challenge

# on win: open a highscore file, insert name
def logScore(play_time,i,j):
    score = scoreGame(play_time,i,j)
    # calculate time: finish - start
    # open or create highscore file
    # insert formatted name and time in file
    # sort file
    sortLog("highscore.log")
    return

def sortLog(file_name):
    # open highscore log
    # make list of name-score pairs
    # if score list size > 10, remove smallest score
    # sort them -- small data set
    return

# win conditions: prompt congrats, prompt name,
def win(start_time, finish_time, rows, cols):
    print("=====YOU WIN!!=====")
    play_time = finish_time - start_time
    logScore(play_time, rows, cols)
    return playAgain()

def greeting():
    return "=====Welcome to Pythonsweeper=====\n" + \
            "GOAL: Flag every bomb!\n" + \
            "Usage: [B]oom/[F]lag [i][j]"

# RUN GAME

print(greeting())

#outer loop, play again?
#prompt player name

area_tuple = getArea()
rows = area_tuple[0]
cols = area_tuple[1]
bombCount = math.floor((rows * cols)/5)
map = [[Tile() for j in range(cols)] for i in range(rows)]
setAdjacent(map)
plotBombs(bombCount, map)

#inner loop until win/lose
drawArea(map)
getCommand()
#end inner loop
#end outer loop

os.system('cls')  # For Windows