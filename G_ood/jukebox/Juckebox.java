import java.util.ArrayList;

public class Juckebox {

    private CDPlayer cdPlayer;
    private int balance;
    private ArrayList<Song> playList;
    private MusicStore musicStore;

    public Juckebox() {
        this.balance = 0;
        this.cdPlayer = new CDPlayer();
        this.playList = new ArrayList<Song>();
        this.musicStore = new MusicStore();
    }


    public void addBalance(int newBalance) {
        this.balance = this.balance + newBalance;
    }

    public void addToPlayList(Song song) {
        this.playList.add(song);
    }

    public void addToPlayList(Album album) {
        for (Song song : album.getSongs()) {
            this.playList.add(song);
        }
    }

    public void addSongs(ArrayList<Song> songs) {
        this.musicStore.addSongs(songs);
    }

    public void addInterprets(ArrayList<Interpret> interprets) {
        this.musicStore.addInterprets(interprets);
    }
    public void addAlbums(ArrayList<Album> albums) {
        this.musicStore.addAlbums(albums);
    }

    public static void main(String[] args) {


        ArrayList<Song> songs = new ArrayList<Song>();
        ArrayList<Interpret> interprets = new ArrayList<Interpret>();
        ArrayList<Album> albums = new ArrayList<Album>();

        // create songs

        // artists
        for (int i = 0; i < 10; i++) {
            Interpret newInterpret = new Interpret("Interpret nr: "+Integer.toString(i));
            interprets.add(newInterpret);

            // albums
            for (int j = 0; j < 3; j++) {
                Album newAlbum = new Album(newInterpret, "Album nr: "+Integer.toString(j)+", Interpret: "+Integer.toString(i));
                newAlbum.addInterpret(newInterpret);
                albums.add(newAlbum);

                // songs
                for (int z = 0; z < 20; z++) {
                    Song newSong = new Song(newInterpret, "Song nr: "+Integer.toString(z)+", Interpret: "+Integer.toString(i)+", Album: "+Integer.toString(j));
                    newAlbum.addSong(newSong);
                    newInterpret.addSong(newSong);
                    newSong.addInterpret(newInterpret);
                    newSong.addAlbum(newAlbum);
                    songs.add(newSong);
                }
                newInterpret.addAlbum(newAlbum);
            }
        }


        Juckebox newJuckeBox = new Juckebox();
        newJuckeBox.addAlbums(albums);
        newJuckeBox.addSongs(songs);
        newJuckeBox.addInterprets(interprets);


        User user = new User();
        user.selectSong(songs.get(5), newJuckeBox);
        

    }
}