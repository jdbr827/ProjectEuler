package Sudoku;

public class Guess {
	public static final int NO_GUESS = -1;
	public int row;
	public int col;
	public int val;

	public Guess(int row, int col, int val) {
		this.row = row;
		this.col = col;
		this.val = val;
	}
	
	public String toString() {
		return "board[" + row + "][" + col + "] ?= " + val; 
	}
}