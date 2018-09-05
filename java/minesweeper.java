/* 
    Author: Joshua Humphreys

    Style Guide(s): https://www.geeksforgeeks.org/java-naming-conventions/
    DB guide: https://nodehead.com/java-how-to-connect-to-xampps-mysql-in-eclipse/
 */

import java.util.*;
import java.io.*;

public class Tile{
        boolean bomb_status;
        boolean hidden;
        boolean flagged;
        int adjacent;
    public Tile(){
        self.bomb_status = false;
        self.hidden = true;
        self.flagged = false;
        self.adjacent = 0;
    }
}
//DEFINE TUPLE CLASS
public class minesweeper {
    
    public static void main(String[] args) {
        
    }
    public static String greeting(){
        return "=====Welcome to Pythonsweeper=====\n" + 
            "GOAL: Flag every bomb!\n" + 
            "Usage: [D]etonate/[F]lag [i][j]";
    }
    public static void lose(){
        String msg="=====Ka-BOOM! GAME OVER!=====";
    }
    public static void win(String name, int start_time, int finish_time,int rows,int cols){
        String msg="=====YOU WIN!!=====";
        play_time = finish_time - start_time;
        logScore(name, play_time, rows, cols);
    }
    public static void sortLog(String file_name){
        //return 
    }
	//send to DB
    public static void logScore(String name, int play_time, int i, int j){
        //return 
    }
	//query from  DB
    public static void printHighscore(HashMap<String, String> dict){
        String msg="=====HIGHSCORES=====";
        //return 
    }
    public static int scoreGame(play_time, i, j){
        int challenge = i * j;
        final int MAX_TIME = 10000;
        int timeBonus = MAX_TIME - play_time;
        //make sure score can't < 1;
        if timeBonus < 1
            timeBonus = 1;
        return (timeBonus) + challenge;
    }
    public static boolean playAgain(){
        //return 
    }
    public static void zeroAdj(List<Tile> map, int i, int j, List<Tuple<int X,int Y>> visited){
        //return 
    }
    public static boolean checkBomb(Tile map_tile){
        if map_tile.bomb_status
            return true;
        else
            map_tile.hidden = false;
        return false;
    }
    public static List<String> getCommand(List<Tile> map){
        //return 
    }
    public static boolean validateCmd(List<String> input_list, int rows, int cols){
        //return 
    }
    public static int checkFlag(int bombCount, Tile map_tile){
        if (map_tile.bomb_status && map_tile.flagged)
            bombCount -= 1;
        return bombCount;
    }
    public static void drawArea(List<Tile> map,int rows, int cols){
         
    }
    public static List<String> getArea(){
        //return 
    }
    public static String getName(){
        //return 
    }
    //Format name for storage
    public static void formatName(String name){
        return name;
    }
    public static void plotBombs(int bombCount, List<Tile> map, int rows, int cols){

    }
    public static void setAdjacent(List<Tile> map, int rows, int cols){

    }
    public static void DEBUG_showMap(List<Tile> map, int rows, int cols){

    }
}
