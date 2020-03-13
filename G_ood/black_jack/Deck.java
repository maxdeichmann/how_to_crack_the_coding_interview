import java.util.ArrayList;


public class Deck <T extends Card> {
    private ArrayList<T> cards;
    private int dealtlndex = 0;

    public int remainingCards() {
        return cards.size() - dealtlndex;
    }

    public void addCard(T newCard) {
        this.cards.add(newCard);
    }

    @Override
    public String toString() {
        String output = "";
        for (int i = 0; i < cards.size(); i++) {
            output = output + " - " + this.cards.get(i).toString();
        }
        return output;
    }



    // public static void main(String[] args) {
    //     Deck<Card> a = new Deck<Card>();
    // }

}
