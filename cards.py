class Card:
    """The Card class represents a single playing card and is initialized 
        by passing a suit and number."""
    def __init__(self, suit, number):
        """
        Intializes a card object.
        
        Arg:
            suit (str): Represents the suit of the card.
            number (str):  Represents value of the card.

        """
        self._suit = suit
        self._number = number

    def __repr__(self):
        """
        Returns a string version of the card.

        Returns:
            A string of the card number and suit.

        """
        return self._number + " of " + self._suit

    @property
    def suit(self):
        """
        Represents the suit of the card.
        
        Returns:
            A string indicating the suit of the card.
        """
        return self._suit

    @suit.setter
    def suit(self, suit):
        """
        Sets a suit of the card as hearts, clubs, diamonds, or spades.
               
        """
        if suit in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit
        else:
            print("That's not a suit!")

    @property
    def number(self):
        """
        Represents the number value of the card.
        
        Returns:
            A string indicating the number value of the card.
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets a str value of the card from 2 to 11, or letters J, Q, K, or A.
               
        """
        valid = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        if number in valid:
            self._number = number
        else:
            print("That's not a valid number")


class Deck:
    """The Deck class represents the whole deck of cards and is initialized by passing self."""
    def __init__(self):
        self._cards = []
        self.populate()

    def populate(self):
        """Represents the setup of a deck using suits and numbers."""
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        self._cards = [ Card(s, n) for s in suits for n in numbers ]

    def shuffle(self):
        """A description of what the shuffle method does."""
        random.shuffle(self._cards)

    def deal(self, no_of_cards):
        """
        Represents the action of dealing cards from the deck.
        
        Arg:
            no_of_cards (int): Number of cards in a players hand.
            dealt_cards (list): Initiated as an empty list, stores new cards that are dealt.
            dealt_card (str): Represents the new card received.
        
        Returns:
            Returns the all the dealt cards with suits and values.
        
        """
        dealt_cards = []
        for i in range(no_of_cards):
            dealt_card = self._cards.pop(0)
            dealt_cards.append(dealt_card)
        return dealt_cards

    def __repr__(self):
        """
        Returns a string of how many cards are in the deck.

        Returns:
            A string of how many cards are in the deck.      

        """
        cards_in_deck = len(self._cards)
        return "Deck of " + str(cards_in_deck) + " cards"
        
deck = Deck()
print(deck)