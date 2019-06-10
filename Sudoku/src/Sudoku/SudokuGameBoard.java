package Sudoku;


/**
 * The current game board of a SudokuGame.
 * @author Jake
 *
 */
public class SudokuGameBoard {
	
	
	/**
	 * The actual current game board.
	 * 
	 * if !board[i][j].isSolved(), then it is unsolved otherwise, board[i][j] is the
	 * established solution for it
	 */
	public Entry[][] board;

	/**
	 * Used when initializing a SudokuGameBoard for the first time.
	 */
	public SudokuGameBoard() {
		Entry[][] board = new Entry[9][9];
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				board[i][j] = new Entry();
			}
		}
		this.board = board;
		return;
	}
		
	public boolean enforce_unequal_entries_constraint(int row1, int col1, int row2, int col2) throws NoSolutionError {
		Entry entry1 = board[row1][col1];
		Entry entry2 = board[row2][col2];
		
		if (entry1.is_solved() && entry2.is_solved()) {
			if (entry1.val == entry2.val) {
				throw new NoSolutionError();
			} else {
				return true;
			}
		}
		
		if (entry1.is_solved() && !entry2.is_solved()) {
			entry2.remove_possibility(entry1.val);
			return true;
		}
		
		if (entry2.is_solved() && !entry1.is_solved()) {
			entry1.remove_possibility(entry2.val);
			return true;
		}
		
		return false;
	}
		
			
	public String toString() {
		String msg = "";
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				Entry entry = board[i][j];
				if (entry.is_solved()) {
					msg += entry.val;
				} else {
					msg += "0";
				}
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

	public boolean enforce_unequal_entries_constraint(Unequal_Entries_Constraint this_constraint) throws NoSolutionError {
		return enforce_unequal_entries_constraint(this_constraint.row1, this_constraint.col1, this_constraint.row2, this_constraint.col2);
	}
	
}