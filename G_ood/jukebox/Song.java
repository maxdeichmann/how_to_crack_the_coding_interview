public class Song {
    private String name;
    private Interpret interpret;
    private Album album;

    public Song(Interpret interpret, String name) {
        this.name = name;
        this.interpret = interpret;
    }


    public void addInterpret(Interpret interpret) {
        this.interpret = interpret;
    }

    public void addAlbum(Album album) {
        this.album = album;
    }
}