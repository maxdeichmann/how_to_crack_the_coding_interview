
public class Board {

    private int n;
    private int[][] fields;

    public Board(int n) {
        super();
        this.n = n;

        this.fields = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                this.fields[i][j] = 0;
            }
        }
    }


    public void setField(Player player, int x, int y) {
        this.fields[y][x] = player.getMark();
    }

    public int getField(int x, int y) {
        return this.fields[y][x];
    }

}