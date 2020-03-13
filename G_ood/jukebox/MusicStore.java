import java.util.ArrayList;


public class MusicStore {

    private ArrayList<Interpret> interprets;
    private ArrayList<Album> albums;
    private ArrayList<Song> songs;


    public MusicStore() {
        this.interprets = new ArrayList<Interpret>();
        this.albums = new ArrayList<Album>();
        this.songs = new ArrayList<Song>();
    }


    public void addSong(Song song) {
        this.songs.add(song);
    }

    public void addInterpret(Interpret interpret) {
        this.interprets.add(interpret);
    }

    public void addAlbum(Album album) {
        this.albums.add(album);
    }


    public void addSongs(ArrayList<Song> songs) {
        for (Song song : songs) {
            this.songs.add(song);
        }
    }

    public void addInterprets(ArrayList<Interpret> interprets) {
        for (Interpret interpret : interprets) {
            this.interprets.add(interpret);
        }
    }
    public void addAlbums(ArrayList<Album> albums) {
        for (Album album : albums) {
            this.albums.add(album);
        }
    }

}

