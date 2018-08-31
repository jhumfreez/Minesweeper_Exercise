/*  
    Author: Joshua Humphreys
    Style Guide: https://www.dofactory.com/reference/csharp-coding-standards

 */

using System;
namespace Minesweeper
{
    public class Tile{
        boolean bomb_status;
        boolean hidden;
        boolean flagged;
        int adjacent;
        //constructor
        public Tile(){
            self.bomb_status = false;
            self.hidden = true;
            self.flagged = false;
            self.adjacent = 0;
    }
}
    class Minesweeper 
    {
        static void Main() 
        {

        }
        public static string Greeting(){
            return "=====Welcome to Pythonsweeper=====\n" + \
                    "GOAL: Flag every bomb!\n" + \
                    "Usage: [D]etonate/[F]lag [i][j]";
        }
        public static void Lose(){
            string msg="=====Ka-BOOM! GAME OVER!=====";
        }
        public static void Win(string name, int start_time, int finish_time,int rows,int cols){
            string msg="=====YOU WIN!!=====";
            play_time = finish_time - start_time;
            logScore(name, play_time, rows, cols);
        }
        public static void SortLog(string file_name){
            //return 
        }
        public static void LogScore(string name, int play_time, int i, int j){
            //return 
        }
        public static void PrintHighscore(Dictionary<string, string> dict){
            string msg="=====HIGHSCORES=====";
            //return 
        }
        public static int ScoreGame(play_time, i, j){
            int challenge = i * j;
            const int MAX_TIME = 10000;
            int timeBonus = MAX_TIME - play_time;
            #make sure score can't < 1;
            if timeBonus < 1
                timeBonus = 1;
            return (timeBonus) + challenge;
        }
        public static boolean PlayAgain(){
        //return 
        }
        public static void ZeroAdj(List<Tile> map, int i, int j, List<Tuple<int X,int Y>> visited){
        //return 
        }
        public static boolean CheckBomb(Tile map_tile){
            if map_tile.bomb_status
                return true;
            else
                map_tile.hidden = false;
            return false;
        }
        public static List<string> GetCommand(List<Tile> map){
            //return 
        }
        public static boolean ValidateCmd(List<string> input_list, int rows, int cols){
            //return 
        }
        public static int CheckFlag(int bombCount, Tile map_tile){
            if (map_tile.bomb_status && map_tile.flagged)
                bombCount -= 1;
            return bombCount;
        }
        public static void DrawArea(List<Tile> map,int rows, int cols){

        }
        public static List<string> GetArea(){
            //return 
        }
        public static string GetName(){
            //return 
        }
        //Format name for storage
        public static void FormatName(string name){
            return name;
        }
        public static void PlotBombs(int bombCount, List<Tile> map, int rows, int cols){

        }
        public static void SetAdjacent(List<Tile> map, int rows, int cols){

        }
        public static void DEBUG_ShowMap(List<Tile> map, int rows, int cols){

        }
    }
}
