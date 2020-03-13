import java.util.ArrayList;


public class Interpret {
    
    private String name;
    private ArrayList<Album> albums;
    private ArrayList<Song> songs;

    public Interpret(String name) {
        this.songs = new ArrayList<Song>();
        this.name = name;
        this.albums = new ArrayList<Album>();
    }

    public void addAlbum(Album album) {
        this.albums.add(album);
    }

    public void addSong(Song song) {
        this.songs.add(song);
    }

}