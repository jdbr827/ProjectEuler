package Sudoku;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Tells us whether or not the entry is solved:
 *  if it is, what the value of the entry is; if it isn't what the possible values are.
 * @author Jake
 *
 */
public class Entry {
	public static final int UNSOLVED = -1;
	
	int val = UNSOLVED; 
	List<Integer> possibilities = new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9)); 
	Entry(){}
	
	boolean is_solved() {
		return val != UNSOLVED;
	}
	
	void solve(int ans) {
		val = ans;
	}
	
	void remove_possibility(int poss) throws NoSolutionError {
		if (is_solved()) {
			if (val == poss) {
				throw new NoSolutionError();
			}
				
		}
		
		possibilities.remove((Object) poss);
		if (possibilities.size() == 1) {
			val = possibilities.get(0);
		}
	}
	
	

}


