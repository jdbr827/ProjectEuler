package Sudoku;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class ReadIn {

	public static void main(String[] args) throws Exception {
		//System.out.println("Hello World");
		
		File file = new File("src\\Sudoku\\p096_sudoku.txt");
		BufferedReader br = new BufferedReader(new FileReader(file));

//		String st;
//		while ((st = br.readLine()) != null) {
//			System.out.println(st);
		
		for (int puzzle_num = 0; puzzle_num < 50; puzzle_num++) {
			br.readLine(); // Grid 01 (or whatever number)
			System.out.println(puzzle_num);
			SudokuGame game = new SudokuGame(br);
			game.solve();
			System.out.println(game.toString());
		}
		
	}
}
