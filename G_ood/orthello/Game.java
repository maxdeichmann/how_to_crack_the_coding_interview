public class Game {

    private Board board;
    private Player player1;
    private Player player2;
    private int turns;
    private int n;
    
    public Game(int n, Player player1, Player player2) {
        super();
        this.board = new Board(n);
        this.player1 = player1;
        this.player2 = player2;
        this.n = n;
        this.turns = 0;
    }

    public void setField(Player player, int x, int y) throws Exception {
        int offset = (this.n - 2) / 2;
        if (((this.turns >= 4) || ((this.turns >= 4) && ((x > offset &&  x < offset + 2) && (y > offset &&  y < offset + 2)))) && (this.board.getField(x, y) == 0)) {
            this.board.setField(player, x, y);
            this.turns++;
            System.out.println(this.board);
        } else {
            throw new Exception("Invalid turn");
        }
    }
    


    public static void main(String[] args) {

        Player player1 = new Player(10);
        Player player2 = new Player(11);
        
        Game game = new Game(10, player1, player2);

        try {
            game.setField(player1, 5, 5);
        } catch(Exception  e) {
            System.out.println(e);
        }
        

    }

}