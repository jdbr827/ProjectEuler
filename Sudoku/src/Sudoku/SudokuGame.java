package Sudoku;

import java.io.BufferedReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;


/**
 * The full SudokuGame and solver. Keeps track of both the board and the active constraints.
 * @author Jake
 *
 */
public class SudokuGame {
	public final static int UNSOLVED = 0;

	SudokuGameBoard board;
	Queue<Unequal_Entries_Constraint> constraint_queue = new LinkedList<Unequal_Entries_Constraint>();

	/**
	 * Used when taking in SudokuGame from the original file
	 * 
	 * @param br
	 *            the buffered reading in the txt file
	 * @throws IOException
	 *             when the BufferedReader has an exception
	 */
	public SudokuGame(BufferedReader br) throws IOException {
		this.board = new SudokuGameBoard();
		
		// Row constraints and col constraints
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				for (int k = j + 1; k < 9; k++) {
					constraint_queue.add(new Unequal_Entries_Constraint(i, j, i, k));
					constraint_queue.add(new Unequal_Entries_Constraint(j, i, k, i));
				}
			}		
		}
		
		for (int box_row = 0; box_row < 3; box_row++) {
			for (int box_col = 0; box_col < 3; box_col++) {
				for (int i1=0; i1<3; i1++) {
					for (int i2 = 0; i2< 3; i2++) {
						for (int j1=0 ; j1<3; j1++) {
							for (int j2=0; j2<3; j2++) {
								if (i1 != i2 || j1 != j2) {
									constraint_queue.add(new Unequal_Entries_Constraint(box_row * 3 + i1, box_col*3 + j1, box_row *3 + i2, box_col * 3 + j2));
								}
							}
						}
					}
				}
			}
		}
				
			
		// Build out the starting constraints
		for (int i = 0; i < 9; i++) {
			char[] row = br.readLine().toCharArray();
			for (int j = 0; j < 9; j++) {
				int num = row[j] - '0';
				if (num != UNSOLVED) {
					board.board[i][j].solve(num);
				}
			}
		}


	}
	public String toString() {
		return board.toString();
	}

	
//	/**
//	 * Used when making a guess; copies the game and enforces the guess as the first constraint.
//	 * @param oldGame -- the previous state of the game before the guess
//	 * @param guess -- the guess on which this new game state is predicated.
//	 */
//	public SudokuGame(SudokuGame oldGame, Guess guess) {
//		
//		assert(oldGame.constraint_queue.isEmpty()); // Note this must be true for us to need to be guessing!
//		this.board = new SudokuGameBoard(oldGame.board);
//		//this.constraint_queue.add(new EqualityConstraint(guess.row, guess.col, guess.val));
//	}
//	
	public void solve() throws NoSolutionError {
		System.out.println(board);
		
		while (!constraint_queue.isEmpty()) {
				Unequal_Entries_Constraint this_constraint = constraint_queue.remove();
				if (!board.enforce_unequal_entries_constraint(this_constraint)) {
					constraint_queue.add(this_constraint);
				}
			}
		
//		if (!board.is_solved()) {
//			Guess next_guess = board.make_new_guess();
//			System.out.println("Next Guess:" + next_guess.toString());
//			SudokuGame guess_game = new SudokuGame(this, next_guess);
//			try {
//				guess_game.solve();
//			} catch (NoSolutionError e) {
//				//constraint_queue.add(new InequalityConstraint(next_guess.row, next_guess.col, next_guess.val));
//				solve();	
//			}
//		}
		return;
	}
}

//	/**
//	 * A constraint in a game of Sudoku
//	 * 
//	 * @author Jake
//	 */
//	interface Constraint {
//
//		void enforce() throws NoSolutionError;
//		
//	}
//
//	public class EqualityConstraint implements Constraint {
//
//		int row;
//		int col;
//		int val;
//		
//		public EqualityConstraint(int row, int col, int val) {
//			this.row = row;
//			this.col = col;
//			this.val = val;
//		}
//		
//		public int get_val() {
//			return val;
//		}
//
//		@Override
//		public void enforce() throws NoSolutionError {
//			System.out.println(this);
//			board = board.enforce_equality_constraint(this);
//			
//			// Generate_new_constraints, but only if the entry was previously an unsolved one.
//			for (int i=0; i<9; i++) {
//				if (i != row) {
//					constraint_queue.add(new InequalityConstraint(i, col, val));
//				}
//				if (i != col) {
//					constraint_queue.add(new InequalityConstraint(row, i, val));
//				}
//			}
//			
//			int box_row = row / 3;
//			int box_col = col / 3;
//			for (int box_row_delta = 0; box_row_delta < 3; box_row_delta++) {
//				for (int box_col_delta = 0; box_col_delta < 3; box_col_delta++) {
//					int my_row = box_row * 3 + box_row_delta;
//					int my_col = box_col * 3 + box_col_delta;
//					if (my_row != row || my_col != col) {
//						constraint_queue.add(new InequalityConstraint(my_row, my_col, val));
//					}
//				}
//			}
//		
//			
//			
//		}
//		
//		public String toString() {
//			return "board[" + row + "][" + col + "] = " + val;
//		}
//
//		
//		@Override
//		public List<Constraint> generate_new_constraints() {
//			// TODO Auto-generated method stub
//			return null;
//		}
//
//	}
//
//	public class InequalityConstraint implements Constraint {
//
//		int row;
//		int col;
//		int val;
//		public InequalityConstraint(int row, int col, int val) {
//			this.row = row;
//			this.col = col;
//			this.val = val;
//		}
//			
//		public int get_val() {
//			return val;
//		}
//			
//		
//		@Override
//		public void enforce() throws NoSolutionError {
//			System.out.println(this.toString());
//			board = board.enforce_inequality_constraint(this);
//		}
//			
//			
//			
//			
//			
//			
//		
//		public String toString() {
//			return "board[" + row + "][" + col + "] != " + val;
//		}
//		
//	}


