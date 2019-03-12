/* 
    Author: Joshua Humphreys

    Style Guide(s): https://www.geeksforgeeks.org/java-naming-conventions/
    DB guide: https://nodehead.com/java-how-to-connect-to-xampps-mysql-in-eclipse/
 */

import java.util.*;
import java.io.*;

public class Tile{
        boolean mine_status;
        boolean hidden;
        boolean flagged;
        int adjacent;
    public Tile(){
        mine_status = false;
        hidden = true;
        flagged = false;
        adjacent = 0;
    }
}
//DEFINE TUPLE CLASS
public class minesweeper {
    
    public static void main(String[] args) {
        
    }
    public static String greeting(){
        return "=====Welcome to Pythonsweeper=====\n" + 
            "GOAL: Flag every mine!\n" + 
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
    public static boolean checkMine(Tile map_tile){
        if map_tile.mine_status
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
    public static int checkFlag(int mineCount, Tile map_tile){
        if (map_tile.mine_status && map_tile.flagged)
            mineCount -= 1;
        return mineCount;
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
    public static void plotmines(int mineCount, List<Tile> map, int rows, int cols){

    }
    public static void setAdjacent(List<Tile> map, int rows, int cols){
		for(int i = 0; i < rows; i++){
			for(int j = 0; j < cols; j++){
				//directions
				int directions[][] = {{i - 1, j - 1},  // NW
							  {i - 1, j},  // N
							  {i - 1, j + 1},  // NE
							  {i, j - 1},  // W
							  {i, j + 1},  // E
							  {i + 1, j - 1},  // SW
							  {i + 1, j},  // S
							  {i + 1, j + 1}};  // SE
				//precomputed bool values
				int validations[][] = {{i-1 >= 0 and j-1 >= 0},  // NW
							  {i-1 >= 0},  // N
							  {i-1 >= 0 and j+1 < cols},  // NE
							  {j-1 >= 0},  // W
							  {j+1 < cols},  // E
							  {i + 1 < rows and j - 1 >= 0},  // SW
							  {i + 1 < rows},  // S
							  {i + 1 < rows and j + 1 < cols}};  // SE
				for(int k = 0; k < directions.Length; k++){
					if validations[k]{
						if(map[int(directions[k][0])][int(directions[k][1])].mine_status)
							map[i][j].adjacent++;
					}
				}
			}
		}
    }
    public static void DEBUG_showMap(List<Tile> map, int rows, int cols){

    }
}
