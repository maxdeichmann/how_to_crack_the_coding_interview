public abstract class Card {

    private int faceValue = 0;
    private boolean available = true;

    public Card(int faceValue) {
        this.faceValue = faceValue;
    }

    public abstract int value();
    public boolean isAvailable() {return available; }
    public void markUnavailable() {available = false; }
    public void markAvailable() {available = true; }


    @Override
    public String toString() {
        return Integer.toString(this.faceValue);
    }

//     public static void main(String[] args) {
//         Card a = new Card(10);
//         System.out.println(a);
//     }
}



