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
	Queue<UnequalEntriesConstraint> constraintQueue = new LinkedList<UnequalEntriesConstraint>();

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
					constraintQueue.add(new UnequalEntriesConstraint(i, j, i, k));
					constraintQueue.add(new UnequalEntriesConstraint(j, i, k, i));
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
									constraintQueue.add(new UnequalEntriesConstraint(box_row * 3 + i1, box_col*3 + j1, box_row *3 + i2, box_col * 3 + j2));
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
	
	
	public SudokuGame(SudokuGameBoard board, Queue<UnequalEntriesConstraint> constraintQueue) {
		this.board = board;
		this.constraintQueue = constraintQueue;
	}
	
	public SudokuGame copy() {
		// copy the constraintqueue.
		// Note this way of doing it cycles through it, ultimately maintaining (and thus copying) order.
		Queue<UnequalEntriesConstraint> new_queue = new LinkedList<UnequalEntriesConstraint>();
		for (int i = 0; i < constraintQueue.size(); i++) {
			UnequalEntriesConstraint this_constraint = constraintQueue.remove();
			new_queue.add(this_constraint);
			constraintQueue.add(this_constraint);
		}
		
		return new SudokuGame(this.board.copy(), new_queue);
	}
	
	public String toString() {
		return board.toString();
	}

	
	public void solve() throws NoSolutionError {
		
		/*
		 * waitingConstraintQueue keeps track of constraints that are unresolved, and have not been
		 * checked since the last insight was made (here specifically, the last possibility removed)
		 */
		Queue<UnequalEntriesConstraint> waitingConstraintQueue = new LinkedList<UnequalEntriesConstraint>();
		
		while (!constraintQueue.isEmpty()) {
				UnequalEntriesConstraint this_constraint = constraintQueue.remove();
				if (board.enforce_unequal_entries_constraint(this_constraint)){
					constraintQueue.addAll(waitingConstraintQueue);
					waitingConstraintQueue.clear();
				} else {
					waitingConstraintQueue.add(this_constraint);
				}
				//System.out.println(constraintQueue.size());
			}
		
		if (waitingConstraintQueue.isEmpty()) {
			// the puzzle is solved;
			return;
		}
		
		Guess guess = board.nextGuess();
		//System.out.println(guess.toString());
		
		
		// in the new game, the constraint queue is our waitingConstraintqueue.
		SudokuGame new_game = this.copy();
		new_game.board.board[guess.row][guess.col].solve(guess.val); // make the assignment
		new_game.constraintQueue.addAll(waitingConstraintQueue); 
		
		try {
			new_game.solve();
			board = new_game.board;
		} catch (NoSolutionError e) {
			board.fixGuess(guess);
			constraintQueue.addAll(waitingConstraintQueue);
			waitingConstraintQueue.clear();
			solve();
			
			
			
		}
		
	}
}
