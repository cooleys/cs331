import java.util.ArrayList;

/**
 * This class represents the module for minimax.
 * @author Chris Ventura
 *
 */
public class MiniMax implements Player {
	int p;
	
	/**
	 * Constructor
	 *
	 */
	public MiniMax(int player) {
		p=player;
	}

	/**
	 * Returns the next move.
	 * @param state The current board state in the game
	 * @return The next move
	 */
	public Position getNextMove(TicTacToeBoard state) throws Exception {
		Position move = null;
		
		int score = max(state);
		ArrayList<TicTacToeBoard> s = getSuccessors(state);

		while (s.size() > 0) {
			System.out.println("Num Successors = "+s.size());
			System.out.println(move);
			
			//check the next possible move
			TicTacToeBoard child = s.remove(0);
			if (min(child) == score)
				for (int row = 0; row < child.SIZE; row++)
					for (int col = 0; col < child.SIZE; col++)
						if (child.getState(row, col) != state.getState(row, col)) {
							move = new Position(row, col); 
							return move;
						}
		}
		
		return move;
	}
	
	private int max(TicTacToeBoard state) throws Exception {
		if (state.isGameOver())
			return val(state);
		int value = -2;

		ArrayList<TicTacToeBoard> s = getSuccessors(state);

		while (s.size() > 0) {
			int mv = min(s.remove(0));
			value = Math.max(value, mv);
		}
		
		return value;
	}
	
	private int min(TicTacToeBoard state) throws Exception {
		if (state.isGameOver())
			return val(state);
		int value = 2;
		
		ArrayList<TicTacToeBoard> s = getSuccessors(state);

		while (s.size() > 0) {
			int mv = max(s.remove(0));
			value = Math.min(value, mv);
		}
		
		return value;
	}
	
	private int val(TicTacToeBoard state) throws Exception {
		//System.out.println("Current: "+p+ " Opponent: "+(p+1)%2);
		//System.out.println("Current: "+state.isWin(p)+ " Opponent: "+state.isWin((p+1)%2));
		//System.out.println(state);
		if (state.isWin(p)) 
			return 1;
		if (state.isWin((p+1)%2))
			return -1;
			
		return 0;
	}

	public ArrayList<TicTacToeBoard> getSuccessors(TicTacToeBoard state) throws Exception{
		ArrayList<TicTacToeBoard> moves = new ArrayList<TicTacToeBoard>();

		for (int row = 0; row < state.SIZE; row++) {
			for (int col = 0; col < state.SIZE; col++) {
				if (state.getState(row, col) == state.BLANK) {
					System.out.println(row + " " + col);
					TicTacToeBoard move = (TicTacToeBoard)state.clone();
					move.setState(row, col, move.getTurn());
					move.setTurn((move.getTurn() + 1) % 2);
					moves.add(move);
				}
			}
		}

		return moves;
	}
	
	/**
	 * Returns the player type 
	 */
	public int getPlayerType() {
		return MINIMAX_PLAYER;
	}

}
