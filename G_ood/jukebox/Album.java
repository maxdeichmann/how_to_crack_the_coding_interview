import java.util.ArrayList;

public class Album {
    private ArrayList<Song> songs;
    private Interpret interpret;
    private String name;

    public Album(Interpret interpret, String name) {
        this.songs = new ArrayList<Song>();
        this.interpret = interpret;
        this.name = name;
    }

    public void addSong(Song song) {
        this.songs.add(song);
    }

    public void addInterpret(Interpret interpret) {
        this.interpret = interpret;
    }

    public ArrayList<Song> getSongs() {
        return this.songs;
    }

}