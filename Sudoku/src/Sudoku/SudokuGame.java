package Sudoku;

import java.io.BufferedReader;
import java.io.IOException;

public class SudokuGame {
	
	int game_num;
	int[][] board = new int[9][9];

	/**
	 * Used when taking in SudokuGame from the original file
	 * 
	 * @param br
	 *           the buffered reading in the txt file
	 * @throws IOException
	 *             when the BufferedReader has an exception
	 */
	public SudokuGame(BufferedReader br) throws IOException {
		for (int i = 0; i < 9; i++) {
			char[] row = br.readLine().toCharArray();
			for (int j = 0; j < 9; j++) {
				int num = row[j] - '0';
				board[i][j] = num;
			}

		}

	}
	
	public String toString() {
		String msg = "";
		for (int i=0; i<9; i++) {
			
			for (int j=0; j<9; j++) {
				msg += (board[i][j]);
				msg += (" ");
				if (j % 3 == 2) {
					msg += ("| ");
				}
			}
			msg += "\n";
			
			if (i % 3 == 2) {
				msg += "----------------------\n";
			}	
		}
		return msg;
		
	}

}
